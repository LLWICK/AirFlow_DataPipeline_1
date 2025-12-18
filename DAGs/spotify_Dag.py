from datetime import timedelta, datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from spotify_etl import run_spotify_etl
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(1),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

dag = DAG(
    dag_id='spotify_dag',
    default_args=default_args,
    description='My first ETL',
    schedule_interval='@daily',
    catchup=False,
)

run_etl = PythonOperator(
    task_id='complete_spotify_etl',
    python_callable=run_spotify_etl,
    dag=dag,
)

run_etl