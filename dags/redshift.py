import os
from airflow import DAG
from airflow.providers.amazon.aws.operators.redshift_data import RedshiftDataOperator

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
    rd = RedshiftDataOperator(
        task_id="run_this",
        dag=dag,
        database="dev",
        workgroup_name="adhoc-cluster",
        sql="select current_user;",
        # aws_conn_id="aws_default",
        wait_for_completion=True,
        return_sql_result=True
    )

    rd
    
except Exception as msg:
    print(msg)