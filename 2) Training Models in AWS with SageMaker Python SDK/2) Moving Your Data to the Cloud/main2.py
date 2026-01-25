# complete the data upload process

import sagemaker

# Initialize SageMaker session
sagemaker_session = sagemaker.Session()

# Get the default SageMaker bucket name
default_bucket = sagemaker_session.default_bucket()

# Local file path
TRAIN_DATA_PATH = "data/california_housing_train.csv"

# TODO: Create a S3 prefix variable and set it to "datasets"
DATA_PREFIX = "datasets"

try:
    # TODO: Upload the training data using the upload_data() method
    train_s3_uri = sagemaker_session.upload_data(
        path=TRAIN_DATA_PATH,
        bucket=default_bucket,
        key_prefix=DATA_PREFIX
    )
    
    # TODO: Print a success message showing where the data was uploaded
    print(f"Successfully uploaded training data to {train_s3_uri}")
    
except Exception as e:
    print(f"Error: {e}")