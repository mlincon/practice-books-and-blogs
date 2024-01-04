import json
import pathlib

import requests
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.utils import dates

# instantiate a DAG object
# this wilöl be the starting point of thw workflow
dag = DAG(
    dag_id="download_rocket_launches",
    start_date=dates.days_ago(14),
    schedule_interval=None,
)  # dag will not run automatically


# use Bash command to download the URL response with curl
curl_cmd = """
curl -o /tmp/launches.json -L 'https://ll.thespacedevs.com/2.0.0/launch/upcoming'
"""
download_launches = BashOperator(
    task_id="download_launches", bash_command=curl_cmd, dag=dag
)


# another Bash operator to notify how many images have been downloaded
notify_cmd = """
echo "There are now $(ls /tmp/images/ | wc -l) images."
"""
notify = BashOperator(task_id="notify", bash_command=notify_cmd, dag=dag)


def _get_pictures():
    """Python function to parse response and download all rocket pictures
        from the json response.
    The response JSON has an array named "results". Each item in the array are
    key-value objects. The following keys are available:
    "id", "url", "launch_library_id", "name", "net", "window_end", "window_start",
    "image", "inforgraphic" and many more. We are interested only in key "image".
    """
    # ensure directory exists
    pathlib.Path("/tmp/images").mkdir(parents=True, exist_ok=True)

    # download all pictures in launches.json
    with open("/tmp/launches.json") as f:
        launches = json.load(f)["results"]
        image_urls = [launch["image"] for launch in launches]
        for image_url in image_urls:
            try:
                response = requests.get(image_url)
                # the name of the image is at the very end of the URL
                image_filename = image_url.split("/")[-1]
                # save image
                target_file = f"/tmp/images/{image_filename}"
                with open(target_file, "wb") as pf:
                    pf.write(response.content)
                print(f"Download {image_url} to {target_file}")
            except requests.exceptions.MissingSchema:
                print(f"{image_url} appears to be an invalid URL")
            except requests.exceptions.ConnectionError:
                print(f"Could not connect to {image_url}")


# Python function to download picture
get_pictures = PythonOperator(
    task_id="get_pictures", python_callable=_get_pictures, dag=dag
)


# set the execution order
download_launches >> get_pictures >> notify
