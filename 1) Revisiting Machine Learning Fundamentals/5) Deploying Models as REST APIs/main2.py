# add a prediction endpoint that can receive house data and return price predictions

import requests
import json

# TODO: Set the API endpoint URL to point to the /predict endpoint
url = "http://localhost:8000/predict"

# Sample house data for prediction (including engineered feature)
# This data represents a real house from the California housing dataset
sample_data = {
    "MedInc": 4.8036,                        # Median income in block group (in tens of thousands)
    "HouseAge": 4.0,                         # Median house age in block group
    "AveRooms": 3.9246575342465753,          # Average number of rooms per household
    "AveBedrms": 1.0359589041095891,         # Average number of bedrooms per household
    "Population": 1050.0,                    # Block group population
    "AveOccup": 1.797945205479452,           # Average number of household members
    "Latitude": 37.39,                       # Block group latitude
    "Longitude": -122.08,                    # Block group longitude
    "RoomsPerHousehold": 2.182857142857143   # Engineered feature: AveRooms / AveOccup
}

# Make prediction request to our API
try:
    # TODO: Send a POST request to the API with sample_data as JSON
    # Hint: Use requests.post(url, json=sample_data)
    response = requests.post(url, json=sample_data)
    
    # Parse the JSON response from the API
    result = response.json()
    
    # TODO: Extract and convert predicted value from units of 100,000s to actual dollar amount
    # Hint: Multiply result['prediction'] by 100000
    predicted_value = result['prediction'] * 100000
    
    # TODO: Print the predicted value in a user-friendly format
    print(f"Predicted house value: ${predicted_value:,.2f}")
    
    # TODO: Print the status from the API response
    # Hint: Use result['status']
    print(f"Status: {result['status']}")
        
# Handle the case where we can't connect to the API server
except requests.exceptions.ConnectionError:
    print("Error: Could not connect to API. Make sure the server is running on localhost:8000")
# Handle any other unexpected errors that might occur
except Exception as e:
    print(f"Error: {e}")