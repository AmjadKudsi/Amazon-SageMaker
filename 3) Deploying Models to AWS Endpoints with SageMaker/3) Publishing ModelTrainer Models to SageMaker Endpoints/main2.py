# create the SageMaker model object that will serve as the blueprint for deployment

import sagemaker
from sagemaker.sklearn.model import SKLearnModel
from sagemaker.serverless import ServerlessInferenceConfig

# Create a SageMaker session
sagemaker_session = sagemaker.Session()

# Get account id from the current AWS session
account_id = sagemaker_session.boto_session.client('sts').get_caller_identity()['Account']

# Define the SageMaker execution role ARN using the account id
SAGEMAKER_ROLE = f"arn:aws:iam::{account_id}:role/SageMakerDefaultExecution"

# List most recent completed training job
training_jobs = sagemaker_session.sagemaker_client.list_training_jobs(
    SortBy='CreationTime',                 # Sort jobs by creation time
    SortOrder='Descending',                # Newest jobs first
    StatusEquals='Completed',              # Only include completed jobs
    NameContains='sklearn-modeltrainer'    # Filter to ModelTrainer jobs
)

# Extract the name of the latest training job
TRAINING_JOB_NAME = training_jobs['TrainingJobSummaries'][0]['TrainingJobName']

# Unique name for the SageMaker endpoint to be created
ENDPOINT_NAME = "california-housing-modeltrainer"

try:
    # Get training job details
    training_job_details = sagemaker_session.describe_training_job(TRAINING_JOB_NAME)
    
    # Extract model artifacts location
    model_data = training_job_details['ModelArtifacts']['S3ModelArtifacts']
    
    # TODO: Create a SKLearnModel with the following parameters:
    #   - model_data: Use the model_data variable
    #   - role: Use SAGEMAKER_ROLE
    #   - entry_point: Set to 'entry_point.py'
    #   - framework_version: Set to '1.2-1'
    #   - py_version: Set to 'py3'
    #   - sagemaker_session: Use sagemaker_session
    model = SKLearnModel(
        model_data=model_data,
        role=SAGEMAKER_ROLE,
        entry_point='entry_point.py',
        framework_version='1.2-1',
        py_version='py3',
        sagemaker_session=sagemaker_session
    )
    
    # Print model configuration to verify setup
    print(f"Model data: {model.model_data}")
    print(f"Entry point: {model.entry_point}")
    print(f"Framework version: {model.framework_version}")
    print(f"Python version: {model.py_version}")
    
except Exception as e:
    print(f"Error: {e}")