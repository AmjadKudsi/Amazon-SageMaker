# complete the ProcessingStep definition by filling in all the missing parameters

import sagemaker
from sagemaker.workflow.steps import ProcessingStep
from sagemaker.sklearn.processing import SKLearnProcessor
from sagemaker.workflow.pipeline_context import PipelineSession

# Create a SageMaker session for immediate operations
sagemaker_session = sagemaker.Session()

# Create a pipeline session for pipeline components
pipeline_session = PipelineSession()

# Retrieve the AWS account ID for constructing resource ARNs
account_id = sagemaker_session.boto_session.client('sts').get_caller_identity()['Account']

# Get the default S3 bucket
default_bucket = sagemaker_session.default_bucket()

# Define the SageMaker execution role
SAGEMAKER_ROLE = f"arn:aws:iam::{account_id}:role/SageMakerDefaultExecution"

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
    name="ProcessData",                             # TODO: Set the step name 
    processor=processor,                           # TODO: Assign the processor we created above
    inputs=[
        sagemaker.processing.ProcessingInput(
            source=f"s3://{default_bucket}/datasets/california_housing.csv", # TODO: Point to the S3 path f"s3://{default_bucket}/datasets/california_housing.csv"
            destination="/opt/ml/processing/input" # TODO: Mount the data at "/opt/ml/processing/input" inside the container
        )
    ],
    outputs=[
        sagemaker.processing.ProcessingOutput(
            output_name="train_data", # TODO: Name this output "train_data"
            source="/opt/ml/processing/train" # TODO: Tell SageMaker to look for files at "/opt/ml/processing/train"
        ),
        sagemaker.processing.ProcessingOutput(
            output_name="test_data", # TODO: Name this output "test_data"
            source="/opt/ml/processing/test" # TODO: Tell SageMaker to look for files at "/opt/ml/processing/test"
        ),
    ],
    code="data_processing.py" # TODO: Specify the script filename "data_processing.py"
)


# Print configuration details to verify setup
print(f"Input source: {processing_step.inputs[0].source}")
print(f"Input destination: {processing_step.inputs[0].destination}")
print(f"Train output name: {processing_step.outputs[0].output_name}")
print(f"Train output source: {processing_step.outputs[0].source}")
print(f"Test output name: {processing_step.outputs[1].output_name}")
print(f"Test output source: {processing_step.outputs[1].source}")
print(f"Processing script: {processing_step.code}")