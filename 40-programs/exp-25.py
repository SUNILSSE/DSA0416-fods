import numpy as np

recovery_times = np.array([5, 7, 9, 10, 12, 15, 18, 20, 22, 25])

percentiles = np.percentile(recovery_times, [10, 50, 90])
print("10th, 50th, and 90th percentiles of recovery times:", percentiles)
