# from airflow import DAG #type: ignore
# from airflow.operators.bash import BashOperator  #type: ignore
# from datetime import datetime
# from airflow.operators.subdag import SubDagOperator #type:ignore 
# #from subdags.subDag_downloads import subdag_downloads #type: ignore
# #from subdags.subDag_transform import subDag_transform #type: ignore
# from airflow.operators.dummy import DummyOperator #type: ignore
# from airflow.utils.task_group import TaskGroup #type: ignore


# with DAG(
#     dag_id = 'group_dag', 
#     start_date = datetime(2025, 1, 1), 
#     schedule_interval = '@daily', 
#     catchup = False) as dag:
 
#     args = {'start_date': dag.start_date, 'schedule_interval': dag.schedule_interval, 'catchup': dag.catchup }
    

#     downloads = SubDagOperator(
#         task_id = 'downloads',
#         subdag = subdag_downloads(dag.dag_id, 'downloads', args)
#     )
 
#     check_files = BashOperator(
#         task_id='check_files',
#         bash_command='sleep 10'
#     )

#     transform = SubDagOperator(
#         task_id = 'transform',
#         subdag = subDag_transform(dag.dag_id, 'transform', args)
#     )


#     downloads >> check_files >> transform

from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime
from airflow.utils.task_group import TaskGroup

with DAG(
    dag_id='group_dag',
    start_date=datetime(2025, 1, 1),
    schedule_interval='@daily',
    catchup=False
) as dag:

    # Download tasks group
    with TaskGroup(group_id='downloads') as downloads:
        download_a = BashOperator(
            task_id='download_a',
            bash_command='sleep 5'
        )
        download_b = BashOperator(
            task_id='download_b',
            bash_command='sleep 5'
        )

        download_c = BashOperator(
            task_id = 'download_c',
            bash_command = "sleep 5" 
        )
        # Define dependencies within the group if needed
        #download_a >> download_b 

    check_files = BashOperator(
        task_id='check_files',
        bash_command='sleep 10'
    )

    # Transform tasks group
    with TaskGroup(group_id='transform') as transform:
        transform_a = BashOperator(
            task_id='transform_a',
            bash_command='sleep 10'
        )
        transform_b = BashOperator(
            task_id='transform_b',
            bash_command='sleep 10'
        )
        transform_c = BashOperator(
            task_id='transform_c',
            bash_command='sleep 10'
        )
        # Define dependencies within the group
        #transform_a >> transform_b >> transform_c

    # Set the overall DAG dependencies
    downloads >> check_files >> transform





