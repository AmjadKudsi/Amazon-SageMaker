# your endpoint returns a hardcoded value of 2.5, but you have a trained linear regression model sitting in the trained_model.joblib file just waiting to be used
# Load the trained model using joblib at the top of your server file
# Make a prediction using the loaded model

from fastapi import FastAPI, Request
import joblib
import pandas as pd

# TODO: Load the trained model from 'trained_model.joblib'
model = joblib.load('trained_model.joblib')

# Create FastAPI app
app = FastAPI(title="House Price Prediction API", version="1.0.0")

@app.post("/predict")
async def predict(request: Request):
    # Parse JSON body directly
    features = await request.json()

    # TODO: Convert features to DataFrame (wrap features in a list first)
    input_data = pd.DataFrame([features])

    # TODO: Make prediction using the loaded model
    prediction = model.predict(input_data)[0]

    # TODO: Replace hardcoded prediction with real prediction from model
    return {
        "prediction": float(prediction),
        "status": "success"
    }