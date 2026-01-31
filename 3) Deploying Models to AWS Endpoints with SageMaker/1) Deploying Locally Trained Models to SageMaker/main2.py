# instantiate an SKLearnModel object that combines your S3-stored model artifacts with the inference logic defined in the provided entry_point.py file

import sagemaker
from sagemaker.sklearn.model import SKLearnModel

# Create a SageMaker session
sagemaker_session = sagemaker.Session()

# Get the default bucket
default_bucket = sagemaker_session.default_bucket()

# Get account id from the current AWS session
account_id = sagemaker_session.boto_session.client('sts').get_caller_identity()['Account']

# S3 URI where the locally trained model artifact is stored
MODEL_ARTIFACTS_S3 = f"s3://{default_bucket}/models/local-trained/model.tar.gz"

# Define the SageMaker execution role ARN using the account id
SAGEMAKER_ROLE = f"arn:aws:iam::{account_id}:role/SageMakerDefaultExecution"

# TODO: Create a SKLearnModel with the following parameters:
# - model_data: Use MODEL_ARTIFACTS_S3
# - role: Use SAGEMAKER_ROLE
# - entry_point: Set to 'entry_point.py'
# - framework_version: Set to '1.2-1'
# - py_version: Set to 'py3'
# - sagemaker_session: Use sagemaker_session
model = SKLearnModel(
    model_data=MODEL_ARTIFACTS_S3,
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