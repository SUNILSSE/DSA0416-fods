import numpy as np
import pandas as pd

# Sample data: daily temperature readings for each city over a year
data = {
    'City': ['CityA'] * 365 + ['CityB'] * 365 + ['CityC'] * 365,
    'Temperature': np.random.randint(15, 35, size=365).tolist() + 
                   np.random.randint(10, 30, size=365).tolist() + 
                   np.random.randint(20, 40, size=365).tolist()
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate the mean temperature for each city
mean_temps = df.groupby('City')['Temperature'].mean()
print("Mean temperature for each city:")
print(mean_temps)

# Calculate the standard deviation of temperature for each city
std_devs = df.groupby('City')['Temperature'].std()
print("\nStandard deviation of temperature for each city:")
print(std_devs)

# Determine the city with the highest temperature range
temp_ranges = df.groupby('City')['Temperature'].agg(lambda x: x.max() - x.min())
city_highest_range = temp_ranges.idxmax()
print("\nCity with the highest temperature range:", city_highest_range)

# Find the city with the most consistent temperature (lowest standard deviation)
city_most_consistent = std_devs.idxmin()
print("City with the most consistent temperature:", city_most_consistent)
