from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator


def extract_telemetry():
    print("Extracting Tesla telemetry data...")


def transform_telemetry():
    print("Transforming Tesla telemetry data...")


def load_telemetry():
    print("Loading Tesla telemetry data into Snowflake...")


default_args = {
    "owner": "data-engineering",
    "retries": 1,
}


with DAG(
    dag_id="tesla_telemetry_etl",
    default_args=default_args,
    description="ETL pipeline for Tesla vehicle telemetry data",
    schedule="@daily",
    start_date=datetime(2026, 1, 1),
    catchup=False,
    tags=["tesla", "telemetry", "etl"],
) as dag:

    extract_task = PythonOperator(
        task_id="extract_telemetry",
        python_callable=extract_telemetry,
    )

    transform_task = PythonOperator(
        task_id="transform_telemetry",
        python_callable=transform_telemetry,
    )

    load_task = PythonOperator(
        task_id="load_telemetry",
        python_callable=load_telemetry,
    )

    extract_task >> transform_task >> load_task
