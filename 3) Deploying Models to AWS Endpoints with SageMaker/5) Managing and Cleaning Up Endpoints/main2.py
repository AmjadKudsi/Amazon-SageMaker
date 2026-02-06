# extend the existing loop to also gather and display configuration information for each endpoint

import json
import sagemaker

# Create a SageMaker session 
sagemaker_session = sagemaker.Session()

try:
    # Get list of all endpoints from SageMaker
    endpoints_response = sagemaker_session.sagemaker_client.list_endpoints()
    
    # Extract the endpoints array from the response
    endpoints = endpoints_response['Endpoints']
    
    for endpoint in endpoints:
        # Print the name and status of each endpoint
        print(f"- {endpoint['EndpointName']} ({endpoint['EndpointStatus']})")
        
        # TODO: Get the endpoint name from the endpoint object
        endpoint_name = endpoint['EndpointName']
        
        # TODO: Use describe_endpoint() to get endpoint details
        endpoint_details = sagemaker_session.describe_endpoint(endpoint_name)
        
        # TODO: Extract the EndpointConfigName from the endpoint details
        config_name = endpoint_details['EndpointConfigName']
        
        # TODO: Use describe_endpoint_config() to get the full configuration details
        config_details = sagemaker_session.sagemaker_client.describe_endpoint_config(
            EndpointConfigName=config_name
        )
        
        # TODO: Display the configuration details as formatted JSON using json.dumps()
        EndpointConfigName=config_name
        print(json.dumps(config_details, indent=2, default=str))
    
except Exception as e:
    print(f"Error: {e}")