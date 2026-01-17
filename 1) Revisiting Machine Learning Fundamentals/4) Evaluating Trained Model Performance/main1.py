# load the saved model from the file using the joblib library, then use it to make predictions on all the test data

import pandas as pd
import joblib

# Load test data
test_data = pd.read_csv('data/california_housing_test.csv')
X_test = test_data.drop('MedHouseVal', axis=1)
y_test = test_data['MedHouseVal']

# TODO: Load the trained model from 'trained_model.joblib'
model = joblib.load('trained_model.joblib')

# TODO: Make predictions on the test data
y_pred = model.predict(X_test)

# TODO: Print the shape of the predictions array
print("Shape of Pred array: ", y_pred.shape)