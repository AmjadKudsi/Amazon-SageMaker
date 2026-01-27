# set up three essential configuration constants

import sagemaker

# Initialize SageMaker session
sagemaker_session = sagemaker.Session()

# Get the default SageMaker bucket name
default_bucket = sagemaker_session.default_bucket()

# Get account ID
account_id = sagemaker_session.boto_session.client('sts').get_caller_identity()['Account']

# S3 data URI where the training data is stored
S3_TRAIN_DATA_URI = f"s3://{default_bucket}/datasets/california_housing_train.csv"

# SageMaker execution role
SAGEMAKER_ROLE = f"arn:aws:iam::{account_id}:role/SageMakerDefaultExecution"

# TODO: Set the instance type to "ml.m5.large" for training compute
INSTANCE_TYPE = "ml.m5.large"

# TODO: Set the instance count to 1 for single-instance training
INSTANCE_COUNT = 1

# TODO: Construct the model output path by combining default_bucket with "models/california-housing/" using S3 URI format
MODEL_OUTPUT_PATH = f"s3://{default_bucket}/models/california-housing/"

# TODO: Print the instance type to verify the compute configuration
print("Instance type: ", INSTANCE_TYPE)

# TODO: Print the instance count to verify the scaling configuration
print("Instance count: ", INSTANCE_COUNT)

# TODO: Print the model output path to verify the storage location
print("Model output path: ", MODEL_OUTPUT_PATH)