# Set up a basic FastAPI application

from fastapi import FastAPI
import joblib

# TODO: Create FastAPI app with title "House Price Prediction API" and version "1.0.0"
model = joblib.load('trained_model.joblib')

app = FastAPI(title="House Price Prediction API", version="1.0.0")