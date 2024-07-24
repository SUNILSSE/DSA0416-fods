import numpy as np

# Sample input data (3x3 matrix of sales data, each row represents a different product)
# Assume prices are arranged by product across columns
sales_data = np.array([
    [100, 120, 95],   # Product 1 prices
    [80, 90, 85],     # Product 2 prices
    [110, 105, 115]   # Product 3 prices
])
# Calculate the average price of all products (overall mean)
average_price = np.mean(sales_data)

# Print the average price
print(f"Average price of all products sold in the past month: ${average_price:.2f}")
