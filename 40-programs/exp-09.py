import pandas as pd
import matplotlib.pyplot as plt

# Sample dataset
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Temperature': [30, 32, 35, 40, 42, 45, 43, 40, 38, 35, 32, 30],
    'Rainfall': [50, 40, 30, 20, 10, 5, 10, 20, 30, 40, 50, 60]
}

# Create DataFrame
df = pd.DataFrame(data)

# Line plot for temperature
plt.figure(figsize=(10, 6))
plt.plot(df['Month'], df['Temperature'], marker='o', linestyle='-', color='b')
plt.title('Monthly Temperature')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Scatter plot for rainfall
plt.figure(figsize=(10, 6))
plt.scatter(df['Month'], df['Rainfall'], color='g')
plt.title('Monthly Rainfall')
plt.xlabel('Month')
plt.ylabel('Rainfall (mm)')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
