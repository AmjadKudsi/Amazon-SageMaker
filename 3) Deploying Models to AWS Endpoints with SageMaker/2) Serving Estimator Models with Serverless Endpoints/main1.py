# complete the code that searches for sklearn estimator training jobs by adding the missing filter parameter

import sagemaker

# Create a SageMaker session
sagemaker_session = sagemaker.Session()

# List most recent completed training job
training_jobs = sagemaker_session.sagemaker_client.list_training_jobs(
    SortBy='CreationTime',                 # Sort jobs by creation time
    SortOrder='Descending',                # Newest jobs first
    StatusEquals='Completed',              # Only include completed jobs
    # TODO: Add the NameContains parameter to filter for sklearn estimator training jobs
    NameContains='sagemaker-scikit-learn'
)

# Extract the name of the latest training job of the list
TRAINING_JOB_NAME = training_jobs['TrainingJobSummaries'][0]['TrainingJobName']

# Print the retrieved training job name
print(f"Latest sklearn estimator training job: {TRAINING_JOB_NAME}")