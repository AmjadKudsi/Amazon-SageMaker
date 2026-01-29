# work with the sagemaker.image_uris.retrieve() function
# see how ModelTrainer requires you to explicitly specify which Docker container to use for training, rather than letting SageMaker automatically select one based on the framework version as Estimators do

import sagemaker
from sagemaker import image_uris

# Initialize SageMaker session and get configuration
sagemaker_session = sagemaker.Session()
default_bucket = sagemaker_session.default_bucket()
account_id = sagemaker_session.boto_session.client('sts').get_caller_identity()['Account']
region = sagemaker_session.boto_region_name

# Configuration constants
S3_TRAIN_DATA_URI = f"s3://{default_bucket}/datasets/california_housing_train.csv"
SAGEMAKER_ROLE = f"arn:aws:iam::{account_id}:role/SageMakerDefaultExecution"
MODEL_OUTPUT_PATH = f"s3://{default_bucket}/models/california-housing/"
INSTANCE_TYPE = "ml.m5.large"
INSTANCE_COUNT = 1
VOLUME_SIZE_GB = 30

# TODO: Use sagemaker.image_uris.retrieve() to get the sklearn container image URI
# - Set framework="sklearn" to specify the ML framework
# - Set region=region to specify the AWS region for the image
# - Set version="1.2-1" to specify the scikit-learn version
# - Set py_version="py3" to specify the Python version for the container
# - Set instance_type=INSTANCE_TYPE for compatibility (required by image_uris.retrieve)
sklearn_image = image_uris.retrieve(
    framework="sklearn",
    region=region,
    version="1.2-1",
    py_version="py3",
    instance_type=INSTANCE_TYPE
)

# TODO: Print the complete image URI
print("Scikit-learn image URI:", sklearn_image)