from airflow import DAG #type: ignore
from airflow.operators.python import PythonOperator  #type: ignore 
from hooks.elastic.elastic_hook import ElasticHook #type: ignore
from datetime import datetime
 
def _print_es_info():
    hook = ElasticHook()
    print(hook.info())
 
with DAG('elastic_dag', start_date=datetime(2022, 1, 1), schedule_interval='@daily', catchup=False) as dag:
 
    print_es_info = PythonOperator(
        task_id = 'print_es_info',
        python_callable = _print_es_info
    )
 

















