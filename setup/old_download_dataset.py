import os
import pandas as pd
from sklearn.datasets import fetch_california_housing

# Create a directory named 'data'
os.makedirs("data", exist_ok=True)

# Load and convert the dataset to a DataFrame
data = fetch_california_housing(as_frame=True).frame

# Save the DataFrame as a CSV file
data.to_csv("data/california_housing.csv", index=False)
