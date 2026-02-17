# complete the model registry query implementation using the SageMaker client's list_model_packages method

import sagemaker

# Create a SageMaker session
sagemaker_session = sagemaker.Session()

# Get the SageMaker client from the session
sagemaker_client = sagemaker_session.sagemaker_client

# Define the model package group name where versioned models are stored
MODEL_PACKAGE_GROUP_NAME = "california-housing-pipeline-models"

try:
    # TODO: Use the SageMaker client to list model packages from the MODEL_PACKAGE_GROUP_NAME
    response = sagemaker_client.list_model_packages(
        ModelPackageGroupName="california-housing-pipeline-models",
        ModelApprovalStatus='Approved',
        SortBy='CreationTime',
        SortOrder='Descending'
    )    
    
    # TODO: Extract the model package list from the response using the 'ModelPackageSummaryList' key
    model_packages = response.get('ModelPackageSummaryList', [])
    
    # TODO: Extract the ModelPackageArn from the first model package in the list
    model_package_arn = model_packages[0]['ModelPackageArn']
    
    # TODO: Print the found model package ARN
    print(f"Found approved model: {model_package_arn}")
    
except Exception as e:
    print(f"Error: {e}")