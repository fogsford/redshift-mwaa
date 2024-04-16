import os
from airflow import DAG
from airflow.providers.amazon.aws.operators.redshift_data import RedshiftDataOperator
from airflow.providers.amazon.aws.operators.redshift_sql import RedshiftSQLOperator
default_args = {
    "start_date": "2023-03-01",
}


DAG_ID = os.path.basename(__file__).replace('_dag.py', '')
dag = DAG(
    f'{DAG_ID}',
    default_args=default_args,
    schedule="0 0 1,15 * *",
    catchup=False
)

try:
    # rd = 
    
    rd = RedshiftSQLOperator(
        task_id='setup__create_table',
        sql="""
            CREATE TABLE IF NOT EXISTS fruit (
            fruit_id INTEGER,
            name VARCHAR NOT NULL,
            color VARCHAR NOT NULL
            );
        """,
    )

    rd
    
except Exception as msg:
    print(msg)