# load the preprocessed California housing training data and separate it into features and target variables

import pandas as pd

# Load training data
train_data = pd.read_csv('data/california_housing_train.csv')

# TODO: Create X_train by dropping the 'MedHouseVal' column from train_data
X_train = train_data.drop('MedHouseVal', axis=1)

# TODO: Create y_train with just the 'MedHouseVal' column from train_data
y_train = train_data['MedHouseVal']

# TODO: Print the shape of X_train to verify it contains the features
print("X_train shape: ", X_train.shape)

# TODO: Print the shape of y_train to verify it contains the target values
print("y_train shape: ", y_train.shape)