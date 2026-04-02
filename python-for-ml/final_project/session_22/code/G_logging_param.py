import mlflow 

mlflow.set_tracking_uri("sqlite:///D:/01_ENV_AI/DEBI-ONL4/DEBI-ONL4_AIS2_S2/mlflow/mlruns.db")

if __name__ == "__main__":

    mlflow.set_experiment("testing_mlflow_1")

    parameters = {
        "learning_rate": 0.001,
        "epochs": 10,
        "batch_sixe": 100,
        "loss_function" : "mse",
        "optimizer" : "Adam"
    }

    with mlflow.start_run(run_name="logging_param") as run:
        mlflow.log_params(parameters)

        print("run_id: ", run.info.run_id) # 3c5c065180374fd68642af2c6a91113a
        print("experiment_id: ", run.info.experiment_id) # 2

    