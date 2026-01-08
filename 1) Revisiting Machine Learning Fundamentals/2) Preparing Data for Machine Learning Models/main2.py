# calculate the 95th percentile values for each numeric feature (except geographic coordinates) using only the training set

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

# TODO: Select features to cap (all numeric except Latitude and Longitude)
features_to_cap = X_train.select_dtypes(include=['float64']).columns.drop(['Latitude', 'Longitude'])

# Dictionary to store capping thresholds
cap_values = {}

# TODO: For each feature in features_to_cap, calculate the 95th percentile from X_train and store in cap_values
for feature in features_to_cap:
    cap_values[feature] = X_train[feature].quantile(0.95)

# TODO: Print out each feature and its calculated 95th percentile threshold to verify
for feature, threshold in cap_values.items():
    print(f"{feature}: 95th percentile = {threshold}")
