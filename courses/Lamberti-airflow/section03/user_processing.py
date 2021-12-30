from airflow.models import DAG
from airflow.providers.sqlite.operators.sqlite import SqliteOperator
from airflow.providers.http.sensors.http import HttpSensor
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

import json
import pandas as pd
from pandas import json_normalize
from datetime import datetime

# options/arguments that will be common to all the tasks in the pipeline
default_args = {
    'start_date': datetime(2020, 1, 1)
}

def _processing_user(ti):
    """Extract the required information, save it as a csv file, which will be
    used by the next task to write in the database
    
    Args:
        ti: task instance object to access Xcoms
    """
    # fetch results/ the user that has been extracted from their previous task
    # i.e. the SimpleHttpOperator
    users = ti.xcom_pull(task_ids=['extracting_user'])
    
    if not len(users) or 'results' not in users[0]:
        raise ValueError('User is empty')
    user = users[0]['results'][0]
    processed_user = {
        'firstname': user['name']['first'],
        'lastname': user['name']['last'],
        'country': user['location']['country'],
        'username': user['login']['username'],
        'password': user['login']['password'],
        'email': user['email']
    }
    # create a dataframe from the json
    processed_user: pd.DataFrame = json_normalize(processed_user)
    
    # save as csv
    processed_user.to_csv('/tmp/processed_user.csv', index=None, header=False)
    


with DAG('user_processing',
         schedule_interval='@daily',
         default_args=default_args,
         catchup=False) as dag:
    # Define tasks/operators

    # create a table in SQLite database to store users in the table
    # the task-id must be unique within the pipeline
    _sql_command = '''
        CREATE TABLE IF NOT EXISTS users (
            --  user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            firstname TEXT NOT NULL,
            lastname TEXT NOT NULL,
            country TEXT NOT NULL,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            email TEXT NOT NULL PRIMARY KEY
        );
    '''
    # we need to define the SQLite connection at first
    # in this case, we name it db_sqlite
    # db_sqlite would be used to connect with the SQLite Database
    creating_table = SqliteOperator(
        task_id='creating_table',
        sqlite_conn_id='db_sqlite',
        sql=_sql_command
    )

    
    # check if API is available
    is_api_available = HttpSensor(
        task_id='is_api_available',
        http_conn_id='user_api',
        endpoint='api/' # the endpoint or page to check
    )
    
    # extract users
    _response_lambda = lambda response: json.loads(response.text)
    extracting_user = SimpleHttpOperator(
        task_id='extracting_user',
        http_conn_id='user_api',
        endpoint='api/',
        method='GET',
        response_filter=_response_lambda, # callable to process the response
        log_response=True # allows to see the response in log
    )

    # extract the required data from JSON response
    processing_user = PythonOperator(
        task_id='processing_user',
        python_callable=_processing_user
    )

    # store extracted user in database
    _bash_command='''
    echo -e ".separator ","\n.import /tmp/processed_user.csv users" | sqlite3 ~/airflow/airflow.db
    '''
    storing_user = BashOperator(
        task_id='storing_user',
        bash_command=_bash_command
    )


    # dependencies
    creating_table >> is_api_available >> extracting_user >> processing_user >> storing_user