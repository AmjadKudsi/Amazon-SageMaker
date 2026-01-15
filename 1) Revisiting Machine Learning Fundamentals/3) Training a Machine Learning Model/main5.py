# implement model persistence by saving your trained linear regression model to a file

import joblib
import pandas as pd
from sklearn.linear_model import LinearRegression

# Load training data
train_data = pd.read_csv('data/california_housing_train.csv')
X_train = train_data.drop('MedHouseVal', axis=1)
y_train = train_data['MedHouseVal']

print(f"Training with {len(X_train)} samples")
print(f"Features: {list(X_train.columns)}")

# Create and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# TODO: Save the trained model to 'trained_model.joblib' using joblib.dump()
joblib.dump(model, 'trained_model.joblib')

# TODO: Print a success message confirming the model was saved
print("Model successfully saved to 'trained_model.joblib'")