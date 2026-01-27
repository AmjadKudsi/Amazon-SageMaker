# create an instance of the SKLearn class with the correct parameters

import sagemaker
from sagemaker.sklearn.estimator import SKLearn

# Initialize SageMaker session
sagemaker_session = sagemaker.Session()

# Get the default SageMaker bucket name
default_bucket = sagemaker_session.default_bucket()

# Get account ID
account_id = sagemaker_session.boto_session.client('sts').get_caller_identity()['Account']

# S3 data URI where the training data is stored
S3_TRAIN_DATA_URI = f"s3://{default_bucket}/datasets/california_housing_train.csv"

# Type of instance to use for training
INSTANCE_TYPE = "ml.m5.large"
# Number of instances to use for training
INSTANCE_COUNT = 1
# SageMaker execution role
SAGEMAKER_ROLE = f"arn:aws:iam::{account_id}:role/SageMakerDefaultExecution"
# Custom output location
MODEL_OUTPUT_PATH = f"s3://{default_bucket}/models/california-housing/"

# TODO: Create the SKLearn estimator
# - Set entry_point to 'train.py' (the Python script with our training code)
# - Use SAGEMAKER_ROLE for the IAM permissions
# - Configure compute resources with INSTANCE_TYPE and INSTANCE_COUNT
# - Set framework_version to '1.2-1' and py_version to 'py3'
# - Enable script_mode=True for modern SageMaker training
# - Include sagemaker_session and MODEL_OUTPUT_PATH as output_path
sklearn_estimator = SKLearn(
    entry_point="train.py",
    role=SAGEMAKER_ROLE,
    instance_type=INSTANCE_TYPE,
    instance_count=INSTANCE_COUNT,
    framework_version="1.2-1",
    py_version="py3",
    script_mode=True,
    sagemaker_session=sagemaker_session,
    output_path=MODEL_OUTPUT_PATH,
)

# TODO: Print the output_path property from the sklearn_estimator to show where model artifacts will be saved

print(sklearn_estimator.output_path)
