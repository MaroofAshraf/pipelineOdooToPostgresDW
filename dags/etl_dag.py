from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from scripts.extract.extract_customers import extract_customers
from scripts.transform.transform_customers import transform_customers
from scripts.load.load_customers import load_customers
from scripts.extract.extract_invoices import extract_invoices
from scripts.transform.transform_invoices import transform_invoices
from scripts.load.load_invoices import load_invoices

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
    'retries': 1
}

dag = DAG(
    'odoo_etl_dag',
    default_args=default_args,
    description='An ETL pipeline for Odoo data',
    schedule_interval='@daily'
)

def etl_customers():
    customers_df = extract_customers()
    transformed_customers_df = transform_customers(customers_df)
    load_customers(transformed_customers_df)

def etl_invoices():
    invoices_df = extract_invoices()
    transformed_invoices_df = transform_invoices(invoices_df)
    load_invoices(transformed_invoices_df)

etl_customers_task = PythonOperator(
    task_id='etl_customers',
    python_callable=etl_customers,
    dag=dag
)

etl_invoices_task = PythonOperator(
    task_id='etl_invoices',
    python_callable=etl_invoices,
    dag=dag
)

etl_customers_task >> etl_invoices_task
