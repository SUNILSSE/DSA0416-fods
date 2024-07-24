import numpy as np

# Assuming the response_times array is as follows:
response_times = np.array([120, 150, 200, 250, 300, 350, 400, 450, 500, 550])

# Calculate the 25th, 50th, and 75th percentiles
percentile_25 = np.percentile(response_times, 25)
percentile_50 = np.percentile(response_times, 50)
percentile_75 = np.percentile(response_times, 75)

print("25th percentile of response times:", percentile_25)
print("50th percentile of response times:", percentile_50)
print("75th percentile of response times:", percentile_75)
