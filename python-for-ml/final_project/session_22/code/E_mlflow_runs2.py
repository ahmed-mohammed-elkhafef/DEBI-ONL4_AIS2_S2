import mlflow 

mlflow.set_tracking_uri("sqlite:///D:/01_ENV_AI/DEBI-ONL4/DEBI-ONL4_AIS2_S2/mlflow/mlruns.db")

if __name__ == "__main__":

    with mlflow.start_run(run_name="mlflow_runs") as run :
        mlflow.log_param("learning_rate", 0.01)
        print("Run ID")
        print(run.info.run_id)

        print(run.info)