import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'Temperature': [5, 7, 12, 18, 22, 25, 27, 26, 21, 15, 10, 6],
    'Rainfall': [50, 40, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50]
}
df = pd.DataFrame(data)
print("Sample Data:")
print(df)
plt.figure(figsize=(10, 6))
plt.plot(df['Month'], df['Temperature'], marker='o', linestyle='-', color='b')
plt.title('Monthly Temperature')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(df['Month'], df['Rainfall'], marker='o', linestyle='-', color='g')
plt.title('Monthly Rainfall')
plt.xlabel('Month')
plt.ylabel('Rainfall (mm)')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(df['Temperature'], df['Rainfall'], color='r', s=100)
plt.title('Temperature vs. Rainfall')
plt.xlabel('Temperature (°C)')
plt.ylabel('Rainfall (mm)')
plt.grid(True)
plt.show()
