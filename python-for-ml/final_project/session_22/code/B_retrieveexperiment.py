import mlflow

mlflow.set_tracking_uri("sqlite:///D:/01_ENV_AI/DEBI-ONL4/DEBI-ONL4_AIS2_S2/mlflow/mlruns.db")

experiment_name = "testing_mlflow"

experiment = mlflow.get_experiment_by_name(experiment_name)

if experiment is not None:
    print("--- Experiment Metadata ---")
    print(f"Name: {experiment.name}")
    print(f"Experiment ID: {experiment.experiment_id}")
    print(f"Artifact Location: {experiment.artifact_location}")
    print(f"Lifecycle Stage: {experiment.lifecycle_stage}") # Outputs 'active' or 'deleted'
    print("-" * 27)
else:
    print(f"Experiment '{experiment_name}' does not exist.")

