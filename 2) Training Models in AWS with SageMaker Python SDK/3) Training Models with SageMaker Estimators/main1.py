# construct the complete URI by combining the default_bucket variable with the correct path structure

import sagemaker

# Initialize SageMaker session
sagemaker_session = sagemaker.Session()

# Get the default SageMaker bucket name
default_bucket = sagemaker_session.default_bucket()

# TODO: Construct the S3 URI by combining the default_bucket with "datasets/california_housing_train.csv"
S3_TRAIN_DATA_URI = f"s3://{default_bucket}/datasets/california_housing_train.csv"

# TODO: Print the constructed S3 URI to verify it's correct
print("S3 URI: ", S3_TRAIN_DATA_URI)