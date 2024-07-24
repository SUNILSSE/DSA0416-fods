import numpy as np

# Assuming the temperatures array is as follows:
temperatures = np.array([30, 32, 31, 29, 35, 36, 28, 40, 42, 33, 34, 30, 31, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13])

# Calculate the variance of the temperatures
variance = np.var(temperatures)
print("Variance of temperatures:", variance)

# Calculate the mean and standard deviation of the temperatures
mean_temp = np.mean(temperatures)
std_dev_temp = np.std(temperatures)

# Identify potential outliers (e.g., more than 2 standard deviations away from the mean)
outliers = temperatures[(temperatures > mean_temp + 2 * std_dev_temp) | (temperatures < mean_temp - 2 * std_dev_temp)]
print("Potential outliers indicating unusual weather conditions:", outliers)
