//create a correlation heatmap using Seaborn to visualize how strongly each feature in the California housing dataset relates to every other feature

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the California housing dataset
df = pd.read_csv('data/california_housing.csv')

# TODO: Calculate the correlation matrix using df.corr()
correlation_matrix = df.corr()

# TODO: Create a heatmap using sns.heatmap() with annot=True, cmap='coolwarm', and center=0
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)

# TODO: Add a title 'Feature Correlation Matrix'
plt.title('Feature Correlation Matrix')

# TODO: Display the plot
plt.tight_layout()