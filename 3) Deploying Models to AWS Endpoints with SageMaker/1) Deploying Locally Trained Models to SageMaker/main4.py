# create a Predictor object that acts as your gateway to the deployed SageMaker endpoint

from sagemaker.predictor import Predictor

# Name of the deployed SageMaker endpoint to connect to
ENDPOINT_NAME = "california-housing-local-model"

try:
    # TODO: Create a Predictor object using the endpoint_name parameter
    predictor = Predictor(endpoint_name=ENDPOINT_NAME)
    
    # TODO: Call the endpoint_context() method on the predictor to get the endpoint context
    context = predictor.endpoint_context()
    
    # TODO: Extract the properties attribute from the context object
    properties = context.properties
    
    # TODO: Print the properties to verify the endpoint connection
    print(properties)
    
except Exception as e:
    print(f"Error: {e}")