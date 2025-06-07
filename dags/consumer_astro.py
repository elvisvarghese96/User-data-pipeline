from airflow import DAG, Dataset # type: ignore
from airflow.decorators import task  # type: ignore
from datetime import datetime

file = Dataset("/tmp/file.txt")


with DAG(
    dag_id = "consumer_astro",
    schedule = [file],
    start_date = datetime(2025, 1, 1),
    catchup = False
    ) as dag:

    @task()
    def readFile():
        with open(file.uri, "r") as f:
            print(f.read)
    readFile()







