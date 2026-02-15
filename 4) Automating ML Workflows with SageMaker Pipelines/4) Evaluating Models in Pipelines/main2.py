# to create a ProcessingStep called EvaluateModel that brings together all the pieces you've been building

import sagemaker
from sagemaker.workflow.pipeline import Pipeline
from sagemaker.workflow.steps import ProcessingStep, TrainingStep
from sagemaker.workflow.pipeline_context import PipelineSession
from sagemaker.sklearn.estimator import SKLearn
from sagemaker.sklearn.processing import SKLearnProcessor
from sagemaker.workflow.properties import PropertyFile

# Create a SageMaker session
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
PIPELINE_NAME = "california-housing-evaluation-pipeline"

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

# Create a processor for running the evaluation script
evaluation_processor = SKLearnProcessor(
    framework_version="1.2-1",
    role=SAGEMAKER_ROLE,
    instance_type="ml.m5.large",
    instance_count=1,
    sagemaker_session=pipeline_session
)

# Define property file for evaluation metrics
evaluation_report_property = PropertyFile(
    name="EvaluationReport",     # Unique identifier for this property file within the pipeline
    output_name="evaluation",    # Must match the output_name in the evaluation step's ProcessingOutput
    path="evaluation.json"       # Path to the JSON file within the evaluation output directory
)

# TODO: Create a ProcessingStep named "EvaluateModel" that includes:
# - Use evaluation_processor as the processor
# - Add first input: model artifact from training_step with destination "/opt/ml/processing/model"
# - Add second input: test data from processing_step with destination "/opt/ml/processing/test" 
# - Add one output: output_name="evaluation", source="/opt/ml/processing/evaluation"
# - Set code="evaluation.py"
# - Include evaluation_report_property in property_files list
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

# Print configuration details to verify setup
print(f"Input source: {evaluation_step.inputs[0].source.expr}")
print(f"Input destination: {evaluation_step.inputs[0].destination}")
print(f"Train output name: {evaluation_step.outputs[0].output_name}")
print(f"Train output source: {evaluation_step.outputs[0].source}")
print(f"Processing script: {evaluation_step.code}")