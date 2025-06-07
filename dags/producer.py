from airflow import DAG, Dataset #type: ignore
from airflow.decorators import task #type: ignore
from datetime import datetime

file = Dataset("/tmp/file.txt")

with DAG(

    dag_id="producer",
    start_date=datetime(2025, 1, 9),
    schedule_interval="@daily",
    catchup=False
    ):

    @task(outlets=[file])                                  # indicate airflow that these tasks update my file
    def update_data():
        with open(file.uri, "a+") as f:                 # a+ is given we want to add some data
            f.write("producer update")

    update_data()


