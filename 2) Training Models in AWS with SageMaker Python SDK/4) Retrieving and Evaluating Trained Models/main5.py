# use your loaded model to predict the value of a specific house and format that prediction as a readable dollar amount

import joblib
import pandas as pd

try:
    # Load the trained model
    model = joblib.load("model.joblib")

    # Sample DataFrame with feature values representing a single house
    sample = pd.DataFrame({
        'MedInc': [4.8036],
        'HouseAge': [4.0],
        'AveRooms': [3.9246575342465753],
        'AveBedrms': [1.0359589041095891],
        'Population': [1050.0],
        'AveOccup': [1.797945205479452],
        'Latitude': [37.39],
        'Longitude': [-122.08],
        'RoomsPerHousehold': [2.182857142857143]
    })

    # TODO: Make prediction using model.predict() on the sample data
    prediction = model.predict(sample)
    
    # TODO: Print the predicted house value by extracting the first value from the prediction array, multiplying it by 100000, and formatting it as currency
    print(f"Predicted house value: ${prediction[0] * 100000:,.2f}")
    
except Exception as e:
    print(f"Error: {e}")