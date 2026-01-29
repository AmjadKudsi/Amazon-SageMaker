# create the three essential configuration objects that ModelTrainer uses to organize your training setup

import sagemaker
from sagemaker.modules.train import ModelTrainer
from sagemaker.modules.configs import SourceCode, Compute, OutputDataConfig

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

# Define the scikit-learn training image URI
sklearn_image = sagemaker.image_uris.retrieve(
    framework="sklearn",         # Specify the ML framework (scikit-learn)
    region=region,               # AWS region for the image
    version="1.2-1",             # scikit-learn version to use
    py_version="py3",            # Python version for the container
    instance_type=INSTANCE_TYPE  # Instance type for compatibility (required by image_uris.retrieve)
)

# TODO: Create the source code configuration using SourceCode class
# - Set source_dir="." for the current directory
# - Set entry_script="train.py" for the main training script
source_code = SourceCode(
    source_dir=".",
    entry_script="train.py"
)

# TODO: Create the compute configuration using Compute class
# - Set instance_type=INSTANCE_TYPE for the EC2 instance type
# - Set instance_count=INSTANCE_COUNT for the number of instances
# - Set volume_size_in_gb=VOLUME_SIZE_GB for the EBS volume size
compute_config = Compute(
    instance_type=INSTANCE_TYPE,
    instance_count=INSTANCE_COUNT,
    volume_size_in_gb=VOLUME_SIZE_GB
)

# TODO: Create the output data configuration using OutputDataConfig class
# - Set s3_output_path=MODEL_OUTPUT_PATH for the model output location
output_config = OutputDataConfig(
    s3_output_path=MODEL_OUTPUT_PATH
)

# TODO: Create the ModelTrainer instance with the following parameters:
# - training_image=sklearn_image for the Docker container image
# - source_code=source_code for the source code configuration
# - base_job_name="sklearn-modeltrainer" for the training job name prefix
# - role=SAGEMAKER_ROLE for the IAM role
# - compute=compute_config for the compute configuration
# - output_data_config=output_config for the output configuration
model_trainer = ModelTrainer(
    training_image=sklearn_image,
    source_code=source_code,
    base_job_name="sklearn-modeltrainer",
    role=SAGEMAKER_ROLE,
    compute=compute_config,
    output_data_config=output_config
)