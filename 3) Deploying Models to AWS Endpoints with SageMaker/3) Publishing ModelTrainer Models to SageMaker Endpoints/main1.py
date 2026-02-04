# Add the NameContains parameter to filter for your ModelTrainer jobs, using the sklearn-modeltrainer base job name we used before when creating them
# Call describe_training_job()
# Extract and print the S3 model artifacts URI

import sagemaker

# Create a SageMaker session
sagemaker_session = sagemaker.Session()

# List most recent completed training job
training_jobs = sagemaker_session.sagemaker_client.list_training_jobs(
    SortBy='CreationTime',                 # Sort jobs by creation time
    SortOrder='Descending',                # Newest jobs first
    StatusEquals='Completed',              # Only include completed jobs
    # TODO: Add NameContains parameter to filter for ModelTrainer jobs
    NameContains='sklearn-modeltrainer'
)

# Extract the name of the latest training job
TRAINING_JOB_NAME = training_jobs['TrainingJobSummaries'][0]['TrainingJobName']

# TODO: Get training job details using describe_training_job()
training_job_details = sagemaker_session.describe_training_job(TRAINING_JOB_NAME)

# TODO: Extract and print the model artifacts URI from training job details
model_data = training_job_details['ModelArtifacts']['S3ModelArtifacts']
print(model_data)
