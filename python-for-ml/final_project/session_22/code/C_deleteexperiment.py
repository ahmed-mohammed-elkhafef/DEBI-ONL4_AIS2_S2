import mlflow 
mlflow.set_tracking_uri("sqlite:///D:/01_ENV_AI/DEBI-ONL4/DEBI-ONL4_AIS2_S2/mlflow/mlruns.db")
mlflow.delete_experiment(experiment_id='1')
