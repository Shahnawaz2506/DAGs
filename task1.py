from airflow import DAG
from airflow.operators.bash import BashOperator

from datetime import datetime
with DAG('extract_stars', schedule_interval='@daily', start_date=datetime(2022,1,1), catchup=False) as dag:
	get_date = BashOperator(task_id="get_date",bash_command="date")
