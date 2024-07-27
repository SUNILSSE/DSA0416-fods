import numpy as np

# Sample sales data (3 products, 3 sales transactions each)
sales_data = np.array([
    [100, 150, 200],
    [120, 180, 240],
    [130, 170, 210]
])

# Calculate the average price of all products sold
average_price = sales_data.mean()
print("Average price of all products sold:", average_price)
