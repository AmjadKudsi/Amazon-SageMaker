# time to see how models actually get stored in SageMaker's Model Registry for future deployment.

import sagemaker
from sagemaker.workflow.pipeline import Pipeline
from sagemaker.workflow.steps import ProcessingStep, TrainingStep
from sagemaker.workflow.step_collections import RegisterModel
from sagemaker.workflow.properties import PropertyFile
from sagemaker.workflow.pipeline_context import PipelineSession
from sagemaker.sklearn.estimator import SKLearn
from sagemaker.sklearn.processing import SKLearnProcessor
from sagemaker.sklearn.model import SKLearnModel

# Create a SageMaker session for pipeline management
sagemaker_session = sagemaker.Session()

# Create a pipeline session for pipeline components
pipeline_session = PipelineSession()

# Retrieve the AWS account ID for constructing resource ARNs
account_id = sagemaker_session.account_id()

# Get the default S3 bucket
default_bucket = sagemaker_session.default_bucket()

# Define the SageMaker execution role
SAGEMAKER_ROLE = f"arn:aws:iam::{account_id}:role/SageMakerDefaultExecution"

# Set a name for the SageMaker Pipeline
PIPELINE_NAME = "california-housing-conditional-pipeline"

# Define the model package group name for organizing registered models
MODEL_PACKAGE_GROUP_NAME = "california-housing-pipeline-models"

# Step 1: Data Processing
processor = SKLearnProcessor(
    framework_version="1.2-1",
    role=SAGEMAKER_ROLE,
    instance_type="ml.m5.large",
    instance_count=1,
    sagemaker_session=pipeline_session
)

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

# Step 2: Model Training
estimator = SKLearn(
    entry_point="train.py",
    role=SAGEMAKER_ROLE,
    instance_type="ml.m5.large",
    instance_count=1,
    framework_version="1.2-1",
    py_version="py3",
    sagemaker_session=pipeline_session
)

training_step = TrainingStep(
    name="TrainModel",
    estimator=estimator,
    inputs={
        "train": sagemaker.inputs.TrainingInput(
            s3_data=processing_step.properties.ProcessingOutputConfig.Outputs["train_data"].S3Output.S3Uri
        )
    }
)

# Step 3: Model Evaluation
evaluation_processor = SKLearnProcessor(
    framework_version="1.2-1",
    role=SAGEMAKER_ROLE,
    instance_type="ml.m5.large",
    instance_count=1,
    sagemaker_session=pipeline_session
)

# Define property file for evaluation metrics
evaluation_report_property = PropertyFile(
    name="EvaluationReport",
    output_name="evaluation",
    path="evaluation.json"
)

evaluation_step = ProcessingStep(
    name="EvaluateModel",
    processor=evaluation_processor,
    inputs=[
        sagemaker.processing.ProcessingInput(
            source=training_step.properties.ModelArtifacts.S3ModelArtifacts,
            destination="/opt/ml/processing/model"
        ),
        sagemaker.processing.ProcessingInput(
            source=processing_step.properties.ProcessingOutputConfig.Outputs["test_data"].S3Output.S3Uri,
            destination="/opt/ml/processing/test"
        )
    ],
    outputs=[
        sagemaker.processing.ProcessingOutput(
            output_name="evaluation",
            source="/opt/ml/processing/evaluation"
        )
    ],
    code="evaluation.py",
    property_files=[evaluation_report_property]
)

# Step 4: Model Registration

# Create a serving model object with a minimal inference script
inference_model = SKLearnModel(
    role=SAGEMAKER_ROLE,
    model_data=training_step.properties.ModelArtifacts.S3ModelArtifacts,
    entry_point="entry_point.py",
    framework_version="1.2-1",
    py_version="py3",
    sagemaker_session=pipeline_session
)

# TODO: Define the name for the SageMaker Model Package Group where versioned models will be stored
MODEL_PACKAGE_GROUP_NAME = "california-housing-pipeline-models"

# TODO: Create a RegisterModel step with:
# - Set a name for the step
# - Use the inference_model object as the model parameter
# - Set content_types to ["text/csv"] for input data format
# - Set response_types to ["text/csv"] for output data format
# - Set inference_instances to ["ml.m5.large"] for real-time inference
# - Set transform_instances to ["ml.m5.large"] for batch inference
# - Use MODEL_PACKAGE_GROUP_NAME for the model_package_group_name parameter
# - Set approval_status to "Approved" for automatic deployment eligibility
register_step = RegisterModel(
    name="RegisterModel",
    model=inference_model,
    content_types=["text/csv"],
    response_types=["text/csv"],
    inference_instances=["ml.m5.large"],
    transform_instances=["ml.m5.large"],
    model_package_group_name=MODEL_PACKAGE_GROUP_NAME,
    approval_status="Approved"
)

# TODO: Add the register_step to the pipeline steps list after evaluation_step
pipeline = Pipeline(
    name=PIPELINE_NAME,
    steps=[processing_step, training_step, evaluation_step, register_step],
    sagemaker_session=sagemaker_session
)

try:
    # Create or update pipeline (upsert = update if exists, create if not)
    pipeline.upsert(role_arn=SAGEMAKER_ROLE)
    
    # Start pipeline execution and get execution object for monitoring
    execution = pipeline.start()

    # Print the unique ARN identifier for this execution
    print(f"Pipeline execution ARN: {execution.arn}")

    # Get detailed information about the execution
    execution_details = execution.describe()

    # Display the current status of the pipeline execution
    print(f"Status: {execution_details['PipelineExecutionStatus']}")
    
except Exception as e:
    print(f"Error: {e}")