// create a histogram that displays the distribution of house values in the California housing dataset

import pandas as pd
import matplotlib.pyplot as plt

# Load the California housing dataset
df = pd.read_csv('data/california_housing.csv')

# TODO: Create a histogram of MedHouseVal with bins=50 and alpha=0.7
plt.hist(df['MedHouseVal'], bins=50, alpha=0.7)

# TODO: Add a title 'Distribution of House Values'
plt.title('Distribution of House Values')

# TODO: Add x-axis label 'Median House Value'
plt.xlabel('Median House Values')

# TODO: Add y-axis label 'Frequency'
plt.ylabel('Frequency')

# TODO: Display the plot
plt.show()