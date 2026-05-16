from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import subprocess
import sys

#Default arguments for the DAG
default_args = {
    'owner': 'Hans Raaj',
    'depends_on_past':False,
    'email_on_failure':False,
    'email_on_retry':False,
    'retries':1,
    'retry_delay': timedelta(minutes=5),
}

# import your ETL functions
sys.path.insert(0,"/Users/hansraaj/Documents/learning/etl-covid-pipeline")
from extract import extract_data
from transform import transform_data
from load import load_data

def run_extract():
    import os
    os.chdir('/Users/hansraaj/Documents/learning/etl-covid-pipeline')
    print("🚀 Starting Extract...")
    extract_data()
    print("✅ Extract done!")

def run_transform():
    import os
    os.chdir('/Users/hansraaj/Documents/learning/etl-covid-pipeline')
    print("🚀 Starting Transform...")
    transform_data()
    print("✅ Transform done!")

def run_load():
    import os
    os.chdir('/Users/hansraaj/Documents/learning/etl-covid-pipeline')
    print("🚀 Starting Load...")
    load_data()
    print("✅ Load done!")

def run_dbt():
    print('Starting dbt models...')
    result = subprocess.run(
        ['dbt','run','--project-dir','/Users/hansraaj/Documents/learning/dbt_covid_transform'],
        capture_output = True,
        text = True
    )
    print(result.stdout)
    if result.returncode != 0:
        raise Exception(f"dbt run failed: {result.stderr}")
    print("dbt model done!")

# define the DAG
with DAG(
    'covid_etl_pipeline',
    default_args=default_args,
    description='Automated COVID-19 ETL Pipeline',
    schedule='@daily',
    start_date = datetime(2026, 5, 6),
    catchup=False,
    tags=['covid','etl','dbt'],
) as dag:

    extract_task = PythonOperator(
        task_id = 'extract',
        python_callable = run_extract,
    )

    transform_task = PythonOperator(
        task_id = 'transform',
        python_callable = run_transform
    )

    load_task = PythonOperator(
        task_id = 'load',
        python_callable = run_load,
    )

    dbt_task = PythonOperator(
        task_id = 'dbt_run',
        python_callable = run_dbt,
    )

    # define the order of tasks
    extract_task >> transform_task >> load_task >> dbt_task