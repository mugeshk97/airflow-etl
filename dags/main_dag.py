from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.mysql_operator import MySqlOperator



def print_hello():
    for i in range(1, 10):
        print("Hello world")

args = {
    'owner': 'mugesh',
    'start_date': datetime(2021, 9, 8),
    'retries':1,
    'retry_delay':timedelta(seconds=5)
    }

with DAG('ETL', default_args=args, schedule_interval='@daily', catchup=False) as dag:

    task1 = BashOperator(task_id='hello', bash_command='echo "Hello World"')

    task2 = PythonOperator(task_id='hello_python', python_callable=print_hello)

    task1 >> task2