import mlflow 

mlflow.set_tracking_uri("sqlite:///D:/01_ENV_AI/DEBI-ONL4/DEBI-ONL4_AIS2_S2/mlflow/mlruns.db")

if __name__ == "__main__":
    experiment_id = mlflow.create_experiment(
        name = "testing_mlflow_1",
        artifact_location= "file:///D:/01_ENV_AI/DEBI-ONL4/DEBI-ONL4_AIS2_S2/mlflow/testing_mlflow_artifact",
        tags = {"env":"dev", "version":"1.0.0"}
          
     )
    
    experiment = mlflow.get_experiment(experiment_id=experiment_id)
    print("Name: {}".format(experiment.name))
    with mlflow.start_run(run_name="testing", experiment_id=experiment.experiment_id) as run:

        mlflow.log_param("learning_rant", 0.0000001)

        print("run_id: {}".format(run.info.run_id)) # 13a0c0c8a27a4ae8853991941fff562c
        print("experment_id: {}".format(run.info.experiment_id)) #2
        print("status: {}".format(run.info.status))
        print("start_time: {}".format(run.info.start_time))
        print("end_time: {}".format(run.info.end_time))
        print("lifecycle_stage: {}".format(run.info.lifecycle_stage))
