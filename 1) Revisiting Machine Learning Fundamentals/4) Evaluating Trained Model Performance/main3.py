# Calculate RMSE by taking the square root of the already computed MSE using np.sqrt()
# Calculate MAE using the mean_absolute_error function
# Calculate the R² Score using the r2_score function

import pandas as pd
import joblib
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import numpy as np

# Load test data
test_data = pd.read_csv('data/california_housing_test.csv')
X_test = test_data.drop('MedHouseVal', axis=1)
y_test = test_data['MedHouseVal']

# Load the trained model
model = joblib.load('trained_model.joblib')

# Make predictions
y_pred = model.predict(X_test)

# Calculate Mean Squared Error
mse = mean_squared_error(y_test, y_pred)

# TODO: Calculate Root Mean Squared Error using numpy's sqrt function
rmse = np.sqrt(mse)

# TODO: Calculate Mean Absolute Error
mae = mean_absolute_error(y_test, y_pred)

# TODO: Calculate R² Score
r2 = r2_score(y_test, y_pred)

# Print Mean Squared Error
print(f"Mean Squared Error: {mse:.2f}")

# TODO: Print Root Mean Squared Error
print(f"Root Mean Squared Error: {rmse:.2f}")

# TODO: Print Mean Absolute Error
print(f"Mean Absolute Error: {mae:.2f}")

# TODO: Print R² Score
print(f"R² Score: {r2:.4f}")
