# modify the upload script to use a nested prefix

import sagemaker

# Initialize SageMaker session
sagemaker_session = sagemaker.Session()

# Get the default SageMaker bucket name
default_bucket = sagemaker_session.default_bucket()

# Local file path
TRAIN_DATA_PATH = "data/california_housing_train.csv"

# TODO: Change the prefix from "datasets" to "datasets/california_housing"
DATA_PREFIX = "datasets/california_housing"

try:
    # Upload the training data using SageMaker session
    train_s3_uri = sagemaker_session.upload_data(
        path=TRAIN_DATA_PATH,
        bucket=default_bucket,
        key_prefix=DATA_PREFIX
    )
    
    # Print success message
    print(f"Successfully uploaded training data to {train_s3_uri}")
    
except Exception as e:
    print(f"Error: {e}")