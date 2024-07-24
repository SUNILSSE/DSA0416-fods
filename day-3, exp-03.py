import numpy as np
from scipy import stats

# Assuming the purchase_amounts array is as follows:
purchase_amounts = np.array([20, 35, 50, 20, 75, 50, 20, 100, 50, 20])

# Calculate the mean (average) purchase amount
mean_purchase_amount = np.mean(purchase_amounts)

# Identify the mode of the purchase amounts
mode_purchase_amount = stats.mode(purchase_amounts)

print("Mean (average) purchase amount:", mean_purchase_amount)
print("Mode (most frequently occurring) purchase amount:", mode_purchase_amount)
