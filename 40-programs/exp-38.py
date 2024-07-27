import pandas as pd

# Sample dataset
data = {
    'WEATHER_CONDITION': ['Sunny', 'Rainy', 'Cloudy', 'Snowy', 'Windy'],
    'OCCURRENCES': [120, 80, 100, 30, 50]
}
df = pd.DataFrame(data)

frequency_distribution = df.set_index('WEATHER_CONDITION')['OCCURRENCES']
print("Frequency Distribution of Weather Conditions:")
print(frequency_distribution)

most_common_weather = frequency_distribution.idxmax()
most_common_count = frequency_distribution.max()
print(f"\nMost Common Weather Type: {most_common_weather} with {most_common_count} occurrences")
