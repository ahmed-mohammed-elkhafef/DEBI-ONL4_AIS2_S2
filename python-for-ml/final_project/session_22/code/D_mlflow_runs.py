import mlflow
mlflow.set_tracking_uri("sqlite:///D:/01_ENV_AI/DEBI-ONL4/DEBI-ONL4_AIS2_S2/mlflow/mlruns.db")
mlflow.set_experiment("testing_mlflow")
if __name__ == "__main__":
    mlflow.start_run()

    mlflow.log_param("learning_rate", 0.001)

    mlflow.end_run()