# The script already has the basic setup code, you need to fill in the missing pieces to make it work properly

import sagemaker

# Define the pipeline name to monitor
PIPELINE_NAME = "california-housing-preprocessing-pipeline"

# Create a SageMaker session
sagemaker_session = sagemaker.Session()

# Get the SageMaker client from the session
sagemaker_client = sagemaker_session.sagemaker_client

# TODO: Complete the required parameters to list only the latest executions of the pipeline
response = sagemaker_client.list_pipeline_executions(
    PipelineName=PIPELINE_NAME,
    SortBy='CreationTime',
    SortOrder='Descending'
)

# TODO: Extract the PipelineExecutionSummaries from the response
executions = response['PipelineExecutionSummaries']

# TODO: Add an if/else condition to check if executions list is empty
    # If empty, print "No pipeline executions found"
    # If not empty, print the count of how many executions were retrieved
if not executions:
    print("No pipeline executions found")
else:
    print(f"Retrieved {len(executions)} pipeline execution(s)")