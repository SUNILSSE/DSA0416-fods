import numpy as np
import matplotlib.pyplot as plt

# Sample dataset
data = {
    'TrafficCongestion': [70, 80, 60, 85, 90, 75, 78, 82, 65, 68],
    'AirPollutionLevel': [55, 60, 50, 65, 70, 58, 62, 67, 48, 52]
}

traffic_congestion = np.array(data['TrafficCongestion'])
air_pollution_level = np.array(data['AirPollutionLevel'])

correlation_coefficient = np.corrcoef(traffic_congestion, air_pollution_level)[0, 1]
print(f"The correlation coefficient between traffic congestion and air pollution levels is: {correlation_coefficient:.2f}")

plt.scatter(traffic_congestion, air_pollution_level)
plt.title('Scatter Plot of Traffic Congestion vs Air Pollution Levels')
plt.xlabel('Traffic Congestion')
plt.ylabel('Air Pollution Level')
plt.show()
