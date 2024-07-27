import numpy as np
sales = [200, 220, 210, 230, 240, 250, 260]
advertising_spend = [20, 22, 21, 23, 24, 25, 26]

correlation_coefficient = np.corrcoef(sales, advertising_spend)[0, 1]
print(f"Correlation Coefficient between Sales and Advertising: {correlation_coefficient:.2f}")
