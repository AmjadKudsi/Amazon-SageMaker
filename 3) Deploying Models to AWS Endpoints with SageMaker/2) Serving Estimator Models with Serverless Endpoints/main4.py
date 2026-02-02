# set the ENDPOINT_NAME to "california-housing-estimator" to connect to the deployed estimator endpoint

import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score
from sagemaker.serializers import CSVSerializer
from sagemaker.deserializers import CSVDeserializer
from sagemaker.predictor import Predictor

# TODO: Set the endpoint name to "california-housing-estimator"
ENDPOINT_NAME = "california-housing-estimator"

# Path to the test dataset CSV file
TEST_DATA_FILE = "data/california_housing_test.csv"

try:
    # Connect to the deployed SageMaker endpoint for inference
    predictor = Predictor(endpoint_name=ENDPOINT_NAME)

    # Set the serializer to convert input data (numpy arrays, pandas DataFrames) to CSV format for the endpoint
    predictor.serializer = CSVSerializer()

    # Set the deserializer to convert the CSV response from the endpoint back to Python objects (e.g., numpy arrays)
    predictor.deserializer = CSVDeserializer()
    
    # Load and split test data into features and target variable
    test_df = pd.read_csv(TEST_DATA_FILE)
    X_test = test_df.drop("MedHouseVal", axis=1)
    y_test = test_df["MedHouseVal"]

    # Make predictions on entire test set
    predictions = predictor.predict(X_test.values)
    
    # Evaluate the model
    test_r2 = r2_score(y_test, predictions)
    test_rmse = np.sqrt(mean_squared_error(y_test, predictions))

    # Print the results
    print(f"R² Score: {test_r2:.4f}")
    print(f"RMSE: {test_rmse:.4f}")

except Exception as e:
    print(f"Error: {e}")