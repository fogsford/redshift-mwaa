import os
from airflow import DAG
from airflow.providers.amazon.aws.operators.redshift_data import RedshiftDataOperator
from airflow.providers.amazon.aws.operators.redshift_sql import RedshiftSQLOperator
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
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
        redshift_conn_id="redshift_default",
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
    

    #https://blog.beachgeek.co.uk/using-redshift-with-mwaa/