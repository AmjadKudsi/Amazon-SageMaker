# Your training data has already been uploaded to S3 at a specific location in your default SageMaker bucket
# download this data and verify its integrity by inspecting it with pandas

import sagemaker
import pandas as pd

# Initialize SageMaker session
sagemaker_session = sagemaker.Session()

# Get the default SageMaker bucket name
default_bucket = sagemaker_session.default_bucket()

# S3 prefix where the data is stored
DATA_PREFIX = "datasets"

# TODO: Download the file from S3
# Use sagemaker_session.download_data() with these parameters:
# - path: "downloaded_data" (local directory to save the file)
# - bucket: default_bucket (the S3 bucket to download from)
# - key_prefix: f"{DATA_PREFIX}/california_housing_train.csv" (the S3 file path)

sagemaker_session.download_data(
    path="downloaded_data",
    bucket=default_bucket,
    key_prefix=f"{DATA_PREFIX}/california_housing_train.csv"
)

# TODO: Read the downloaded CSV file with pandas and display the first five rows
df = pd.read_csv("downloaded_data/california_housing_train.csv")

print(df.head())