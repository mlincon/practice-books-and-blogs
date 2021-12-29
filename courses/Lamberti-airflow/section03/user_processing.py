from airflow.models import DAG
from airflow.providers.sqlite.operators.sqlite import SqliteOperator
from airflow.providers.http.sensors.http import HttpSensor

from datetime import datetime

# options/arguments that will be common to all the tasks in the pipeline
default_args = {
    'start_date': datetime(2020, 1, 1)
}


with DAG('user_processing',
         schedule_interval='@daily',
         default_args=default_args,
         catchup=False) as dag:
    # Define tasks/operators

    # create a table in SQLite database to store users in the table
    # the task-id must be unique within the pipeline
    sql_command = '''
        CREATE TABLE users (
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
    creating_table = SqliteOperator(task_id='creating_table',
                                    sqlite_conn_id='db_sqlite',
                                    sql=sql_command)

    
    # check if API is available
    is_api_available = HttpSensor(task_id='is_api_available',
                                  http_conn_id='user_api',
                                  endpoint='api/') # the endpoint or page to check
    
    