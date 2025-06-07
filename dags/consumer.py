from airflow import DAG, Dataset #type: ignore
from airflow.decorators import task #type: ignore
from datetime import datetime

file = Dataset("/tmp/file.txt")
with DAG(
    dag_id="consumer",
    start_date=datetime(2025, 1, 9),
    schedule=[file],
    catchup = False
    ):

    @task                               
    def read_data():
        with open(file.uri, "r") as f:                 # a+ is given we want to add some data
            print(f.read())

    read_data()







