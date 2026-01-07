# engineer a powerful new feature called RoomsPerHousehold that combines information from two existing features: AveRooms and AveOccup

import pandas as pd

# Load the California housing dataset
df = pd.read_csv('data/california_housing.csv')

# TODO: Create the new RoomsPerHousehold feature by dividing AveRooms by AveOccup
df['RoomsPerHousehold'] = df['AveRooms'] / df ['AveOccup']

# TODO: Display sample rows showing AveRooms, AveOccup, and the new RoomsPerHousehold feature
print(df[['AveRooms', 'AveOccup', 'RoomsPerHousehold']].head())