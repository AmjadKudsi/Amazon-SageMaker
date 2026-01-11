# Combine the split features and targets back together into complete training and test datasets using pd.concat()
# Print the shape of both datasets to verify they're properly formed
# Save both datasets as CSV files in the /data folder without including the index

import pandas as pd
from sklearn.model_selection import train_test_split

# Load the California housing dataset
df = pd.read_csv('data/california_housing.csv')

# Create a new feature: average number of rooms per household
df['RoomsPerHousehold'] = df['AveRooms'] / df['AveOccup']

# Select relevant features for modeling
feature_columns = [
    'MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 
    'AveOccup', 'Latitude', 'Longitude', 'RoomsPerHousehold'
]
X = df[feature_columns]
y = df['MedHouseVal']

# Split the data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Cap numeric features at their 95th percentiles using ONLY training data
features_to_cap = X_train.select_dtypes(include=['float64']).columns.drop(['Latitude', 'Longitude'])

# Calculate capping thresholds from training data only
cap_values = {}
for feature in features_to_cap:
    cap_values[feature] = X_train[feature].quantile(0.95)

# Apply capping to both training and test sets using training-derived thresholds
for feature in features_to_cap:
    X_train[feature] = X_train[feature].clip(upper=cap_values[feature])
    X_test[feature] = X_test[feature].clip(upper=cap_values[feature])

# TODO: Combine features and target for saving
train_data = pd.concat([X_train, y_train], axis=1)
test_data = pd.concat([X_test, y_test], axis=1)

# TODO: Print the shape of both datasets to verify they're properly formed
print(f"\nTraining data shape: {train_data.shape}")
print(f"Test data shape: {test_data.shape}")

# TODO: Save the train data to 'data/california_housing_train.csv' without the index
train_data.to_csv('data/california_housing_train.csv', index=False)

# TODO: Save the test data to 'data/california_housing_test.csv' without the index
test_data.to_csv('data/california_housing_test.csv', index=False)