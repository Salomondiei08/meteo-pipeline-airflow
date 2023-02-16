from airflow import DAG
from datetime import timedelta
from airflow.operators.python import PythonOperator
from datetime import datetime
from meteo_etl import run_meteo_etl

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2020, 11, 8),
    'email': ['salomondiei08@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

meteo_dag = DAG(
    'twitter_dag',
    default_args=default_args,
    description='Our first DAG with ETL process!',
    schedule=timedelta(days=1),
)

run_etl = PythonOperator(
    task_id='complete_meteo_etl',
    python_callable=run_meteo_etl,
    dag=meteo_dag,
)

run_etl

