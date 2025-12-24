from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import mlflow
import mlflow.sklearn
import pandas as pd
import numpy as np
from implicit.als import AlternatingLeastSquares
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score

mlflow.set_tracking_uri("http://mlflow:5000")
default_args = {"start_date": datetime(2025, 12, 24)}

dag = DAG(
    "ml_pipeline", default_args=default_args, schedule_interval="@daily", catchup=False
)
