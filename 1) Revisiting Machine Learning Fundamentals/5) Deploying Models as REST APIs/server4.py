# add robust error handling to both sides of your API

from fastapi import FastAPI, HTTPException, Request
import joblib
import pandas as pd

# Load the trained model
model = joblib.load('trained_model.joblib')

# Create FastAPI app
app = FastAPI(title="House Price Prediction API", version="1.0.0")

@app.post("/predict")
async def predict(request: Request):
    # TODO: Add try block here
    try:
        # Parse JSON body directly
        features = await request.json()
        # Convert to DataFrame
        input_data = pd.DataFrame([features])
        # Make prediction
        prediction = model.predict(input_data)[0]
        # Return a response
        return {
            "prediction": float(prediction),
            "status": "success"
        }
    
    # TODO: Add except block that catches Exception as e and raises HTTPException with status_code=400 and detail=str(e)
    # Hint: Use "raise HTTPException(status_code=400, detail=str(e))" to return a proper error response
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))