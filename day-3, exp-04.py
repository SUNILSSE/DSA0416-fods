import numpy as np

# Sample data: monthly expenses of different departments (rows are departments, columns are months)
expenses = np.array([
    [2000, 2200, 2100, 2500, 2400],  # Department 1
    [1800, 1900, 1950, 2050, 2000],  # Department 2
    [2300, 2350, 2200, 2400, 2450],  # Department 3
    [2500, 2600, 2700, 2800, 2750]   # Department 4
])

# Calculate variance of each department's monthly expenses
variances = np.var(expenses, axis=1)
print("Variances of monthly expenses for each department:")
print(variances)

# Calculate covariance matrix of the monthly expenses
covariance_matrix = np.cov(expenses)
print("\nCovariance matrix of the monthly expenses:")
print(covariance_matrix)
