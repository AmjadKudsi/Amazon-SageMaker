import requests
import json

# API endpoint
url = "http://localhost:8000/predict"

# Sample house data for prediction (including engineered feature)
sample_data = {
    "MedInc": 4.8036,
    "HouseAge": 4.0,
    "AveRooms": 3.9246575342465753,
    "AveBedrms": 1.0359589041095891,
    "Population": 1050.0,
    "AveOccup": 1.797945205479452,
    "Latitude": 37.39,
    "Longitude": -122.08,
    "RoomsPerHousehold": 2.182857142857143  # AveRooms / AveOccup
}

# Make prediction request
try:
    # Send POST request with house data as JSON to the /predict endpoint
    response = requests.post(url, json=sample_data)
    
    # Parse the JSON response from the API
    result = response.json()
    
    # Convert predicted value from units of 100,000s to actual dollar amount
    # (Our model was trained on values in hundreds of thousands)
    predicted_value = result['prediction'] * 100000
    
    # Display the response
    print(f"Predicted house value: ${predicted_value:,.2f}")
    print(f"Status: {result['status']}")
except requests.exceptions.ConnectionError:
    print("Error: Could not connect to API. Make sure the server is running on localhost:8000")
except Exception as e:
    print(f"Error: {e}")