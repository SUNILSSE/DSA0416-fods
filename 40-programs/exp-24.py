import numpy as np

response_times = np.array([120, 150, 200, 250, 300, 350, 400, 450, 500, 550])

percentiles = np.percentile(response_times, [25, 50, 75])
print("25th, 50th, and 75th percentiles of response times:", percentiles)
