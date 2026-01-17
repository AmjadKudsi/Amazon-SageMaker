# calculate the Mean Squared Error (MSE) between your model's predictions and the actual house values from the test set

import pandas as pd
import joblib
from sklearn.metrics import mean_squared_error

# Load test data
test_data = pd.read_csv('data/california_housing_test.csv')
X_test = test_data.drop('MedHouseVal', axis=1)
y_test = test_data['MedHouseVal']

# Load the trained model
model = joblib.load('trained_model.joblib')

# Make predictions
y_pred = model.predict(X_test)

# TODO: Calculate Mean Squared Error using mean_squared_error function
mse = mean_squared_error(y_test, y_pred)

# TODO: Print the MSE result
print(f"Mean Squared Error: {mse:.2f}")