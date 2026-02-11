# Your code has all the foundational pieces ready — sessions, processor, and processing step are configured
# You need to assemble them into a working pipeline and set it in motion

import sagemaker
from sagemaker.workflow.pipeline import Pipeline
from sagemaker.workflow.steps import ProcessingStep
from sagemaker.sklearn.processing import SKLearnProcessor
from sagemaker.workflow.pipeline_context import PipelineSession

# Create a SageMaker session for pipeline management
sagemaker_session = sagemaker.Session()

# Create a pipeline session for pipeline components
pipeline_session = PipelineSession()

# Retrieve the AWS account ID for constructing resource ARNs
account_id = sagemaker_session.boto_session.client('sts').get_caller_identity()['Account']

# Get the default S3 bucket
default_bucket = sagemaker_session.default_bucket()

# Define the SageMaker execution role
SAGEMAKER_ROLE = f"arn:aws:iam::{account_id}:role/SageMakerDefaultExecution"

# Set a name for the SageMaker Pipeline
PIPELINE_NAME = "california-housing-preprocessing-pipeline"

# Create a processor that will run our data preprocessing script
processor = SKLearnProcessor(
    framework_version="1.2-1",
    role=SAGEMAKER_ROLE,
    instance_type="ml.m5.large",
    instance_count=1,
    sagemaker_session=pipeline_session
)

# Define the processing step with inputs, outputs, and the script to run
processing_step = ProcessingStep(
    name="ProcessData",
    processor=processor,
    inputs=[
        sagemaker.processing.ProcessingInput(
            source=f"s3://{default_bucket}/datasets/california_housing.csv",
            destination="/opt/ml/processing/input"
        )
    ],
    outputs=[
        sagemaker.processing.ProcessingOutput(
            output_name="train_data",
            source="/opt/ml/processing/train"
        ),
        sagemaker.processing.ProcessingOutput(
            output_name="test_data",
            source="/opt/ml/processing/test"
        )
    ],
    code="data_processing.py"
)

# TODO: Create a pipeline with name, steps, and sagemaker session
pipeline = Pipeline(
    name=PIPELINE_NAME,
    steps=[processing_step],
    sagemaker_session=sagemaker_session
)

try:
    # TODO: Create or update pipeline using upsert with the role ARN
    pipeline.upsert(role_arn=SAGEMAKER_ROLE)
    
    # TODO: Start pipeline execution and store the execution object
    execution = pipeline.start()

    # TODO: Print the unique ARN identifier for this execution
    print(f"Pipeline execution ARN: {execution.arn}")

    # TODO: Get detailed information about the execution using describe method
    execution_details = execution.describe()

    # TODO: Display the current status of the pipeline execution
    print(f"Status: {execution_details['PipelineExecutionStatus']}")
    
except Exception as e:
    print(f"Error: {e}")