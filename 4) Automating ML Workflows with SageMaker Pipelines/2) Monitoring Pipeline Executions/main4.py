# add step-level monitoring to your existing script

import sagemaker

# Define the pipeline name to monitor
PIPELINE_NAME = "california-housing-preprocessing-pipeline"

# Create a SageMaker session
sagemaker_session = sagemaker.Session()

# Get the SageMaker client from the session
sagemaker_client = sagemaker_session.sagemaker_client

# List pipeline executions sorted by creation time (newest first)
response = sagemaker_client.list_pipeline_executions(
    PipelineName=PIPELINE_NAME,
    SortBy='CreationTime',
    SortOrder='Descending'
)

# Extract the execution summaries from the response
executions = response['PipelineExecutionSummaries']

# Check if any executions exist
if not executions:
    print("No pipeline executions found")
else:
    # Get the latest execution (first item in the list)
    latest_execution = executions[0]
    
    # Extract execution ARN
    execution_arn = latest_execution['PipelineExecutionArn']
    
    # TODO: Retrieve all steps for this specific execution using list_pipeline_execution_steps with the execution ARN
    steps_response = sagemaker_client.list_pipeline_execution_steps(
        PipelineExecutionArn=execution_arn
    )
    
    # TODO: Extract the steps from the response by accessing 'PipelineExecutionSteps'
    steps = steps_response['PipelineExecutionSteps']
    
    # TODO: Iterate through each step in the steps list
        # TODO: Extract the StepName from each step
        # TODO: Extract the StepStatus from each step
        
        # TODO: Print the step name and status in the format "StepName: StepStatus"
    for step in steps:

        step_name = step['StepName']
        step_status = step['StepStatus']
        step_start = step.get('StartTime', 'Not started')
        
        
        print(f"\n{step_name}: {step_status}")
        
        
        if step_start != 'Not started':
            print(f"Started: {step_start}")