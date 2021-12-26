Note that the `dags_folder` as defined in `~/airflow/airflow.cfg` is `/home/airflow/airflow/dags` or `~/airflow/dags`. Hence, any DAGs created will need to be copied over, e.g.
```
cp chapter02/download_rocket_launches.py ~/airflow/dags
```