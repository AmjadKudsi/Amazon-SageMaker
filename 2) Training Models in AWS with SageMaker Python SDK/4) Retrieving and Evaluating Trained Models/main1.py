# write the code that finds and displays the name of your most recently completed SageMaker training job

import sagemaker

# Create a SageMaker session
sagemaker_session = sagemaker.Session()

# TODO: Get the most recent completed scikit-learn training jobs 
# - Sort jobs by creation time
# - Get newest jobs first
# - Only include completed jobs
# - Filter jobs containing 'sagemaker-scikit-learn' in name

training_jobs = sagemaker_session.sagemaker_client.list_training_jobs(
    SortBy='CreationTime',
    SortOrder='Descending',
    StatusEquals='Completed',
    NameContains='sagemaker-scikit-learn'
)

# TODO: Extract the name of the latest training job of the list
TRAINING_JOB_NAME = training_jobs['TrainingJobSummaries'][0]['TrainingJobName']

# TODO: Print the retrieved training job name
print("Latest training job: ", TRAINING_JOB_NAME)