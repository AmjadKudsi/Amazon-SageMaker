# add a prediction endpoint that can receive house data and return price predictions

from fastapi import HTTPException, FastAPI, Request
import pandas as pd
import joblib

# Create FastAPI app
app = FastAPI(title="House Price Prediction API", version="1.0.0")

model = joblib.load('trained_model.joblib')

# TODO: Create a POST endpoint at "/predict" that accepts a Request object
# Hint: Use the @app.post decorator with "/predict" path
# TODO: Create an async function that takes Request as parameter
    # TODO: Parse the JSON body using await request.json()
    # TODO: Return a dictionary with prediction=2.5 and status="success"
    
@app.post("/predict")
async def predict(request: Request):

    features = await request.json()

    input_data = pd.DataFrame([features])
    
    prediction = model.predict(input_data)[0]
    
    # Return a response
    return {
        "prediction": 2.5,
        "status": "success"
        }
            