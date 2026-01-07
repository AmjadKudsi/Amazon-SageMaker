# complete a comprehensive data quality assessment by implementing the two key methods

import pandas as pd

# Load the California housing dataset
df = pd.read_csv('data/california_housing.csv')

pd.set_option('display.max_columns', None)

# TODO: Generate statistical summary using df.describe()
# Remember to set pandas to display all columns first!
print("Statistical summary:", df.describe())

# TODO: Check for missing values using df.isnull().sum()
print("\nMissing values:", df.isnull().sum())