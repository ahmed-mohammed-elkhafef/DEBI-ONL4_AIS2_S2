import mlflow

if __name__ == "__main__":
    mlflow.set_tracking_uri("sqlite:///D:/01_ENV_AI/DEBI-ONL4/DEBI-ONL4_AIS2_S2/mlflow/mlruns.db")
    
    
    experiment_id = mlflow.create_experiment(
    name="testing_mlflow",
    artifact_location="file:///D:/01_ENV_AI/DEBI-ONL4/DEBI-ONL4_AIS2_S2/mlflow/testing_mlflow_artifact",
    tags={"env": "dev", "version": "1.0.0"}
        ) 
    print(experiment_id) # 1
    
    
       