# use the SKLearn.attach() method to reconnect to your completed training job and examine the key properties that make deployment possible

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

# TODO: Use SKLearn.attach() to connect to the training job and store the result in an estimator variable
estimator = SKLearn.attach(TRAINING_JOB_NAME)

# TODO: Print the framework version
print("Framework version:", estimator.framework_version)

# TODO: Print the model data S3 location
print("Model data S3 URI:", estimator.model_data)

# TODO: Print the container image URI
print("Training image URI:", estimator.training_image_uri())