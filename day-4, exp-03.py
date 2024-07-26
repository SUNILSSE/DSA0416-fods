# Given dataset
weather_conditions = {
    "Sunny": 120,
    "Rainy": 150,
    "Cloudy": 100,
    "Snowy": 30,
    "Windy": 60,
    "Foggy": 40,
    "Stormy": 20
}

# Calculate the most common weather type
most_common_weather = max(weather_conditions, key=weather_conditions.get)

# Print the most common weather type
print(f"The most common weather type is {most_common_weather} with {weather_conditions[most_common_weather]} occurrences.")
