# create a professional scatter plot that compares your model's predictions against the actual house values from the test set

import pandas as pd
import joblib
import matplotlib.pyplot as plt

# Load test data
test_data = pd.read_csv('data/california_housing_test.csv')
X_test = test_data.drop('MedHouseVal', axis=1)
y_test = test_data['MedHouseVal']

# Load the trained model
model = joblib.load('trained_model.joblib')

# Make predictions
y_pred = model.predict(X_test)


# TODO: Set up the figure with size (10, 8)
# TODO: Create a scatter plot of y_test vs y_pred with alpha=0.5
# TODO: Add the red dashed reference line from min to max values with line width 2
# TODO: Add x-axis label 'Actual Values'
# TODO: Add y-axis label 'Predicted Values'
# TODO: Add title 'Predictions vs Actual Values'
# TODO: Add grid with alpha=0.3
# TODO: Show the plot

plt.figure(figsize=(10, 8))
plt.scatter(y_test, y_pred, alpha=0.5)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')
plt.title('Predictions vs Actual Values')
plt.grid(True, alpha=0.3)
plt.show()