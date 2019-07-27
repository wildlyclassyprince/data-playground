'''
311_service_requests.py

311 Service Requests Data Pipeline
-------------------------------

This repository is a data pipeline of 311 Service Requests from 2010 to
present. The information from `data.cityofnewyork.us` is updated daily.
We would like to be able to obtain a daily update of this data and store
it in a local database for analysis.

Workflow manager:
- Airflow

Task scheduler:
- Airflow

File default location:
- ~/airflow/dags

'''

# Imports
# Data processing
import json
import psycopg2
import pandas as pd

# Task scheduling
import airflow
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

#==============================================================================
# Defaults and setup
default_args = {
    'owner': 'wildlyclassyprince',
    'depends_on_past': False,
    'start_date': datetime(2019, 7, 21),
    'email': ['lihtumb@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 5,
    'retry_delay': timedelta(minutes=1),
}

# DAG
dag = DAG('311_service_requests',
          default_args=default_args,
          schedule_interval=timedelta(days=1))

# Datapath
raw_data_path = '~/airflow/mydata/311-service-requests/raw-data/'
clean_data_path = '~/airflow/mydata/311-service-requests/clean-data/'
#==============================================================================

#==============================================================================
# Operators
# Read data
def read_311():
    print('Reading 311 Service Requests Data')
    data = pd.read_json(
         'https://data.cityofnewyork.us/resource/fhrw-4uyv.json')
    # Save
    data.to_csv(raw_data_path+'311servicerequests.csv', index=False)

# Transform data
def transform():
    print('Transforming Data')
    # Read data
    data = pd.read_csv(raw_data_path+'311servicerequests.csv')
    
    # Drop columns
    def _drop_cols():
        cols = list()
        for column_name in data.columns:
            if ':@' in column_name:
                cols.append(column_name)
        return cols
                
    # Date columns
    def _date_cols():
        cols = list()
        for column_name in data.columns:
            if 'date' in column_name:
                cols.append(column_name)
        return cols
    
    # Dropping
    data.drop(_drop_cols(), axis=1, inplace=True)

    # Formating dates
    for column in _date_cols():
        data[column] = pd.to_datetime(data[column], yearfirst=True)
        
    # Column order
        
    # Save
    data.to_csv(clean_data_path+'clean311servicerequests.csv', index=False)

# Load data
def load():
    print('Load Data to DB')
    
    # Credentials
    with open('config/postgresql-credentials.json') as creds:
        credentials = load(creds)
        
    try:
        # Connect to DB
        conn = psycopg2.connect(user=credentials['user'],
                                password=credentials['password'],
                                host=credentials['host'],
                                port=credentials['port'],
                                database=credentials['database'])
        cursor = conn.cursor()
        with open(clean_data_path+'clean311servicerequests.csv', 'r') as file:
            next(file)
            cursor.copy_from(file)
            conn.commit()
        print(f'{cursor.rowcount} records successfully committed')
        if conn:
            cursor.close()
            conn.close()
    except (Exception, psycopg2.error) as error:
        print(f'Failed to insert record {cursor.rowcount}: {error}')
        
        

# Tasks
t1 = PythonOperator(task_id='read_311_data',
                    python_callable=read_311,
                    dag=dag)

t2 = PythonOperator(task_id='transform_data',
                    python_callable=transform,
                    dag=dag)

t3 = PythonOperator(task_id='load_to_db',
                    python_callable=load,
                    dag=dag)

t1.set_downstream(t2)
t2.set_downstream(t3)

if __name__ == '__main__':
    dag.cli()
