# Remove the ServerlessInferenceConfig import and replace it with real-time configuration variables
# Delete the serverless configuration section, and add INSTANCE_TYPE set to "ml.m5.large" and INSTANCE_COUNT set to 1
# Update the model.deploy() method to use the initial_instance_count and instance_type parameters instead of serverless_inference_config

import sagemaker
from sagemaker.sklearn.model import SKLearnModel
# TODO: Remove the ServerlessInferenceConfig import and add real-time configuration variables
#from sagemaker.serverless import ServerlessInferenceConfig

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

# TODO: Remove the serverless configuration and replace it with variables for instance type and instance count for a real-time endpoint
# serverless_config = ServerlessInferenceConfig(
#     memory_size_in_mb=2048,
#     max_concurrency=10
# )

# Real time endpoint configuration
INSTANCE_TYPE = "ml.m5.large"
INSTANCE_COUNT = 1

try:
    # Get training job details to find model artifacts location
    training_job_details = sagemaker_session.describe_training_job(TRAINING_JOB_NAME)
    model_data = training_job_details['ModelArtifacts']['S3ModelArtifacts']
    
    # Create a SKLearnModel with the inference script
    model = SKLearnModel(
        model_data=model_data,               # S3 location of trained model artifacts
        role=SAGEMAKER_ROLE,                 # IAM role for SageMaker
        entry_point='entry_point.py',        # Inference script
        framework_version='1.2-1',           # scikit-learn version
        py_version='py3',                    # Python version
        sagemaker_session=sagemaker_session  # SageMaker session
    )
    
    # TODO: Replace the serverless_inference_config parameter with initial_instance_count and instance_type parameters
    # Deploying to a real time endpoint (not serverless)
    predictor = model.deploy(
        initial_instance_count=INSTANCE_COUNT,
        instance_type=INSTANCE_TYPE,
        endpoint_name=ENDPOINT_NAME,
        wait=False
    )
    
    # Retrieve detailed information about the specified SageMaker endpoint
    endpoint_description = sagemaker_session.sagemaker_client.describe_endpoint(EndpointName=ENDPOINT_NAME)

    # Extract the current status of the endpoint from the response
    status = endpoint_description['EndpointStatus']

    # Display the endpoint's status
    print(f"Endpoint status: {status}")
    
except Exception as e:
    print(f"Error: {e}")