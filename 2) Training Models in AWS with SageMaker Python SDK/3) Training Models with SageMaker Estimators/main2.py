# Extract your unique AWS account ID using the Security Token Service
# Construct the complete IAM role ARN 

import sagemaker

# Initialize SageMaker session
sagemaker_session = sagemaker.Session()

# Get the default SageMaker bucket name
default_bucket = sagemaker_session.default_bucket()

# TODO: Extract your AWS account ID using the STS (Security Token Service) client
# Hint: Use boto_session to create an STS client and look for caller identity information
boto_session = sagemaker_session.boto_session
sts_client = boto_session.client("sts")
account_id = sts_client.get_caller_identity()["Account"]

# TODO: Build the SageMaker execution role ARN
# Hint: AWS ARNs follow a pattern with service, account ID, and resource type
role_name = "SageMakerDefaultExecution"  
execution_role_arn = f"arn:aws:iam::{account_id}:role/{role_name}"

# TODO: Display the account ID you extracted
print(f"Account ID: {account_id}")

# TODO: Display the complete execution role ARN you constructed
print(f"Execution Role ARN: {execution_role_arn}")