import pandas as pd

data = {
    'City': ['CityA', 'CityA', 'CityA', 'CityB', 'CityB', 'CityB', 'CityC', 'CityC', 'CityC'],
    'Temperature': [30, 32, 31, 25, 27, 26, 20, 22, 21]
}
df = pd.DataFrame(data)

mean_temp = df.groupby('City')['Temperature'].mean()
print("Mean Temperature for each city:")
print(mean_temp)

std_temp = df.groupby('City')['Temperature'].std()
print("\nStandard Deviation of Temperature for each city:")
print(std_temp)

temp_range = df.groupby('City')['Temperature'].apply(lambda x: x.max() - x.min())
print("\nTemperature Range for each city:")
print(temp_range)

highest_range_city = temp_range.idxmax()
print(f"\nCity with the Highest Temperature Range: {highest_range_city}")

most_consistent_city = std_temp.idxmin()
print(f"City with the Most Consistent Temperature: {most_consistent_city}")
