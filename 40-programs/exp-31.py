import numpy as np
expenses = np.array([
    [2000, 2200, 2100],
    [2300, 2400, 2500],
    [2600, 2700, 2800]
])

variance_expenses = np.var(expenses, axis=0)
print("Variance of Monthly Expenses for each department:")
print(variance_expenses)

covariance_matrix = np.cov(expenses, rowvar=False)
print("\nCovariance Matrix of Monthly Expenses:")
print(covariance_matrix)
