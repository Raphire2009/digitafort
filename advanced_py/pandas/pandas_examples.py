# Python Pandas Example
# To run this example:
# 1. Install the required packages: pip install -r requirements.txt
# 2. Run the script: python pandas_examples.py

import pandas as pd
import matplotlib.pyplot as plt

# Creating a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}

df = pd.DataFrame(data)

# Displaying the DataFrame
print("DataFrame:")
print(df)
print("-" * 20)

# Basic DataFrame operations
print("Basic Info:")
print(df.info())
print("-" * 20)

print("Descriptive Statistics:")
print(df.describe())
print("-" * 20)

# Selecting data
print("Selecting the 'Name' column:")
print(df['Name'])
print("-" * 20)

print("Selecting multiple columns:")
print(df[['Name', 'City']])
print("-" * 20)

# Filtering data
print("Filtering people older than 30:")
print(df[df['Age'] > 30])
print("-" * 20)

# Data Visualization
df.plot(kind='bar', x='Name', y='Age', title='Age of People')
plt.show()
