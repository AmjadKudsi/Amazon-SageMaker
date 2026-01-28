# complete the model retrieval workflow by downloading the compressed model file from S3, extracting its contents, and loading the trained model into memory

import tarfile
import joblib
import numpy as np
import pandas as pd
from sagemaker.sklearn.estimator import SKLearn
import sagemaker
from sagemaker.s3 import S3Downloader
from sklearn.metrics import mean_squared_error, r2_score

# Create a SageMaker session
sagemaker_session = sagemaker.Session()

# List most recent completed training job
training_jobs = sagemaker_session.sagemaker_client.list_training_jobs(
    SortBy='CreationTime',                 # Sort jobs by creation time
    SortOrder='Descending',                # Newest jobs first
    StatusEquals='Completed',              # Only include completed jobs
    NameContains='sagemaker-scikit-learn'  # Filter to jobs containing 'sagemaker-scikit-learn' in name
)

# Extract the name of the latest training job of the list
TRAINING_JOB_NAME = training_jobs['TrainingJobSummaries'][0]['TrainingJobName']

# Path to test data
TEST_DATA_FILE = "data/california_housing_test.csv"

try:
    # Attach to the latest completed training job
    estimator = SKLearn.attach(TRAINING_JOB_NAME)

    # Get model S3 location from the estimator
    model_s3_uri = estimator.model_data

    # TODO: Download the model artifact from S3 using S3Downloader.download() with model_s3_uri and current directory "."
    S3Downloader.download(model_s3_uri, ".")
    
    # TODO: Extract the downloaded "model.tar.gz" file using tarfile.open() with 'r:gz' mode and extractall()
    with tarfile.open("model.tar.gz", 'r:gz') as tar:
        tar.extractall(".")
    
    # TODO: Load the extracted "model.joblib" file using joblib.load()
    model = joblib.load("model.joblib")
    
    # TODO: Print the model's coefficients (coef_) and intercept (intercept_)
    print("Model's coefficients: ", model.coef_)
    print("Model's Intercepts: ", model.intercept_)

except Exception as e:
    print(f"Error: {e}")