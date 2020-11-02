from datetime import timedelta

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.utils.dates import days_ago

args = {
    'owner': 'airflow',
}

dag = DAG(
    dag_id='jacobs_bash_operator',
    default_args=args,
    schedule_interval='0 0 * * *',
    start_date=days_ago(2),
    dagrun_timeout=timedelta(minutes=60),
    tags=['example']
)

task1 = DummyOperator(
    task_id='Start',
    dag=dag
)

# [START howto_operator_bash]
task2 = BashOperator(
    task_id='run_after_loop',
    bash_command='echo "run_id={{ run_id }} | dag_run={{ dag_run }}"',
    dag=dag,
)
# [END howto_operator_bash]

task1 >> task2

#if __name__ == "__main__":
#    dag.cli()

# test git
