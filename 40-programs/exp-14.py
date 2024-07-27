import numpy as np

# Sample sales data for four quarters
sales_data = np.array([10000, 15000, 20000, 25000])

# Calculate total sales for the year
total_sales = sales_data.sum()
print("Total sales for the year:", total_sales)

# Calculate percentage increase from Q1 to Q4
percentage_increase = ((sales_data[3] - sales_data[0]) / sales_data[0]) * 100
print("Percentage increase in sales from Q1 to Q4:", percentage_increase)
