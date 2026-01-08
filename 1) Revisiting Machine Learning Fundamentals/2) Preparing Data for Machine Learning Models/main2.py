// split your dataset into training and testing portions to ensure proper model validation and avoid data leakage when we handle outliers in the next steps

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

# TODO: Separate features (X) from the target variable (y)
X = df[feature_columns]
y = df['MedHouseVal']

# TODO: Split the data using train_test_split with test_size=0.2 and random_state=42
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# TODO: Print the shape of X_train
# TODO: Print the shape of X_test
# TODO: Print the shape of y_train
# TODO: Print the shape of y_test
print("X_train shape:", X_train.shape)
print("X_test shape:", X_test.shape)
print("y_train shape:", y_train.shape)
print("y_test shape:", y_test.shape)