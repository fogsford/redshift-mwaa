import os
from airflow import DAG
from airflow.providers.amazon.aws.operators.redshift_data import RedshiftDataOperator
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from datetime import datetime

default_args = {
    "start_date": datetime(2023, 3, 1),
    "owner": "airflow"
}

DAG_ID = os.path.basename(__file__).replace('_dag.py', '')

dag = DAG(
    dag_id=DAG_ID,
    default_args=default_args,
    schedule_interval="0 0 1,15 * *",
    catchup=False
)

# # Task 1 using SQLExecuteQueryOperator
# task1_sql_exec_query = SQLExecuteQueryOperator(
#     task_id='execute_query_using_sql_operator',
#     sql="SELECT usename, usesysid, usesuper FROM pg_user WHERE usename=current_user;",
#     conn_id="redshift_default",  # Make sure to configure this connection in Airflow
#     dag=dag
# )

# Task 2 using RedshiftDataOperator
task2_redshift_data = RedshiftDataOperator(
    task_id='execute_query_using_redshift_operator',
    sql="""
    CREATE SCHEMA IF NOT EXISTS mwaa;
    CREATE TABLE IF NOT EXISTS mwaa.users (
        user_id INT,
        user_name VARCHAR(100)
    );
    """,
    database="dev",
    workgroup_name = "mwaa",
    dag=dag,
    return_sql_result = True
)

# Define task order
## task1_sql_exec_query >> task2_redshift_data
