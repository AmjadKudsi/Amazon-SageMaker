# Initialize a regular SageMaker session for immediate operations
# Create a PipelineSession for building pipeline components
# Set up an SKLearnProcessor with the correct configuration parameters

import sagemaker
from sagemaker.sklearn.processing import SKLearnProcessor
from sagemaker.workflow.pipeline_context import PipelineSession

# TODO: Create a SageMaker session for immediate operations
sagemaker_session = sagemaker.Session()

# TODO: Create a pipeline session for pipeline components
pipeline_session = PipelineSession()

# Retrieve the AWS account ID for constructing resource ARNs
account_id = sagemaker_session.boto_session.client('sts').get_caller_identity()['Account']

# Define the SageMaker execution role
SAGEMAKER_ROLE = f"arn:aws:iam::{account_id}:role/SageMakerDefaultExecution"

# TODO: Create an SKLearnProcessor with:
# - Framework version "1.2-1"
# - The execution role
# - Instance type "ml.m5.large"
# - Instance count 1
# - The pipeline session
processor = SKLearnProcessor(
    framework_version="1.2-1",
    role=SAGEMAKER_ROLE,
    instance_type="ml.m5.large",
    instance_count=1,
    sagemaker_session=pipeline_session
)

# Print processor configuration to verify setup
print(f"Processor role ARN: {processor.role}")
print(f"Processor instance type: {processor.instance_type}")
print(f"Processor instance count: {processor.instance_count}")