import numpy as np
from scipy import stats

purchase_amounts = [50, 20, 30, 20, 50, 70, 20, 50, 30, 50]

mean_purchase = np.mean(purchase_amounts)
print(f"Mean (Average) Purchase Amount: ${mean_purchase:.2f}")

mode_purchase = stats.mode(purchase_amounts)
print(f"Mode (Most Frequent) Purchase Amount: ${mode_purchase.mode[0]} (Frequency: {mode_purchase.count[0]})")
