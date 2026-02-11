# The code already handles finding and retrieving pipeline executions, but you need to complete two key tasks
# Extract three key pieces of information from the latest_execution dictionary and Print the extracted values in a user-friendly format

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
    
    # TODO: Extract the PipelineExecutionArn from latest_execution
    # TODO: Extract the PipelineExecutionStatus from latest_execution
    # TODO: Extract the StartTime from latest_execution
    execution_arn = latest_execution['PipelineExecutionArn']
    status = latest_execution['PipelineExecutionStatus']
    start_time = latest_execution['StartTime']

    # TODO: Display the extracted details from the latest execution
    print(f"Latest Execution ARN: {execution_arn}")
    print(f"Status: {status}")
    print(f"Start Time: {start_time}")
