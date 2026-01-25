# complete the script that connects to AWS SageMaker and discovers your default storage location

import sagemaker

# TODO: Initialize SageMaker session
sagemaker_session = sagemaker.Session()

# TODO: Get the default SageMaker bucket name
default_bucket = sagemaker_session.default_bucket()

# TODO: Print the default bucket name
print(f"Default Sagemaker bucket: {default_bucket}")