# use your trained model to generate predictions on the training data

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

print("Model training completed!")

# TODO: Use the trained model to make predictions on X_train and store in y_train_pred
y_train_pred = model.predict(X_train)

# TODO: Print the shape of y_train_pred to verify it matches the number of training samples
print("y_train_pred Shape: ", y_train_pred.shape)