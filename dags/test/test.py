from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
import sys
import os
from datetime import datetime, timedelta

os.system("cd /opt/airflow/dags/test")
sys.path.append('dags/test')


default_args = {
        'owner': 'TRAVELOKA_V1',
        'start_date': datetime(2019, 5, 24)
        }
dag = DAG('TRAVELOKA_V1', default_args=default_args, schedule_interval='@daily', catchup=False)
t1 = BashOperator(
    task_id='crawl_data',
    bash_command='cd /opt/airflow/dags/test && scrapy crawl hotel',
    dag=dag)



t1
