# apply the outlier thresholds consistently to both the training and test sets

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

# TODO: Loop over each feature in features_to_cap
    # TODO: Cap X_train[feature] using .clip(upper=cap_values[feature])
    # TODO: Cap X_test[feature] using the same threshold
for features in features_to_cap:
    X_train[feature] = X_train[feature].clip(upper=cap_values[feature])
    X_test[feature] = X_test[feature].clip(upper=cap_values[feature])

# TODO: Show summary statistics of X_train after preprocessing
print(X_train.describe())