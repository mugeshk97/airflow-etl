from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash_operator import BashOperator

args = {
    'owner': 'airflow',
    'start_date': datetime(2021, 9, 8),
    'retries':1,
    'retry_delay':timedelta(seconds=5)
    }

dag = DAG('dag1', default_args=args, schedule_interval='@daily', catchup=False)

task1 = BashOperator(task_id='task1', bash_command='echo "Hello World"', dag=dag)