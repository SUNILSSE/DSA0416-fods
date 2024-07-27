import pandas as pd
import matplotlib.pyplot as plt

# Sample dataset
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Sales': [1500, 1800, 1700, 1600, 2000, 2100, 1900, 2200, 2300, 2400, 2500, 2600]
}

# Create DataFrame
df = pd.DataFrame(data)

# Line plot for sales
plt.figure(figsize=(10, 6))
plt.plot(df['Month'], df['Sales'], marker='o', linestyle='-', color='b')
plt.title('Monthly Sales')
plt.xlabel('Month')
plt.ylabel('Sales ($)')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Scatter plot for sales
plt.figure(figsize=(10, 6))
plt.scatter(df['Month'], df['Sales'], color='g')
plt.title('Monthly Sales')
plt.xlabel('Month')
plt.ylabel('Sales ($)')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Bar plot for sales
plt.figure(figsize=(10, 6))
plt.bar(df['Month'], df['Sales'], color='c')
plt.title('Monthly Sales')
plt.xlabel('Month')
plt.ylabel('Sales ($)')
plt.xticks(rotation=45)
plt.show()
