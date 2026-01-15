# evaluate your linear regression model using two important metrics

import pandas as pd
from sklearn.linear_model import LinearRegression
# TODO: Import mean_squared_error and r2_score from sklearn.metrics
from sklearn.metrics import mean_squared_error, r2_score

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

# Make predictions on training data
y_train_pred = model.predict(X_train)

# TODO: Calculate Mean Squared Error using mean_squared_error function
train_mse = mean_squared_error(y_train, y_train_pred)

# TODO: Calculate R-squared score using r2_score function
train_r2 = r2_score(y_train, y_train_pred)

# TODO: Display the evaluation metrics
print(f"Training MSE: {train_mse:.2f}") 
print(f"Training R²: {train_r2:.4f}")