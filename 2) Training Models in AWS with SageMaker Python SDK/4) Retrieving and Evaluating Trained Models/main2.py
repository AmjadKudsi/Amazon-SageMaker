# use the training job name you retrieved to attach to the completed SageMaker training job and extract the S3 location of your model artifacts

import sagemaker
from sagemaker.sklearn.estimator import SKLearn

# Create a SageMaker session
sagemaker_session = sagemaker.Session()

# List most recent completed training job
training_jobs = sagemaker_session.sagemaker_client.list_training_jobs(
    SortBy='CreationTime',                 # Sort jobs by creation time
    SortOrder='Descending',                # Newest jobs first
    StatusEquals='Completed',              # Only include completed jobs
    NameContains='sagemaker-scikit-learn'  # Filter to jobs containing 'sagemaker-scikit-learn' in name
)

# Extract the name of the latest training job of the list
TRAINING_JOB_NAME = training_jobs['TrainingJobSummaries'][0]['TrainingJobName']

# TODO: Attach to the latest completed training job using SKLearn.attach()
estimator = SKLearn.attach(TRAINING_JOB_NAME)

# TODO: Get the model S3 location from the estimator's model_data property
model_s3_uri = estimator.model_data

# TODO: Print the model S3 location
print("Model's S3 location: ", model_s3_uri)