# complete a Python script that retrieves and displays basic information about all SageMaker endpoints in your AWS account

import sagemaker

# Create a SageMaker session 
sagemaker_session = sagemaker.Session()

try:
    # TODO: Call the list_endpoints() method on the SageMaker client to get all endpoints
    endpoints_response = sagemaker_session.sagemaker_client.list_endpoints()
    
    # TODO: Extract the 'Endpoints' array from the response
    endpoints = endpoints_response['Endpoints']
    
    # TODO: Iterate through each endpoint and print its name and status
    print('SageMaker Endpoints:')
    for endpoint in endpoints:
        print(f"- {endpoint['EndpointName']} ({endpoint['EndpointStatus']})")
    
except Exception as e:
    print(f"Error: {e}")