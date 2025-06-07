from airflow import DAG, Dataset  # type: ignore
from airflow.decorators import task  # type: ignore

from datetime import datetime

file = Dataset("/tmp/file.txt")

with DAG(
    dag_id = "producer_astro",
    schedule = "@daily",
    start_date = datetime(2025, 1, 1),
    catchup = False
    ) as dag:

    @task(outlets = [file])
    def update_file():
        with open(file.uri, "a+") as f:
            f.write("updated producer")

    update_file()





