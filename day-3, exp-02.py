import numpy as np

# Assuming the recovery_times array is as follows:
recovery_times = np.array([5, 7, 8, 10, 12, 15, 18, 20, 22, 25, 30, 35, 40, 45, 50])

# Calculate the 10th, 50th, and 90th percentiles
percentile_10 = np.percentile(recovery_times, 10)
percentile_50 = np.percentile(recovery_times, 50)
percentile_90 = np.percentile(recovery_times, 90)

print("10th percentile of recovery times:", percentile_10)
print("50th percentile of recovery times:", percentile_50)
print("90th percentile of recovery times:", percentile_90)
