import numpy as np

# Assuming the sales_data array is as follows:
# Each element represents the sales amount for a specific quarter.
sales_data = np.array([10000, 15000, 20000, 25000])

# Calculate the total sales for the year
total_sales = np.sum(sales_data)

# Calculate the percentage increase in sales from the first quarter to the fourth quarter
percentage_increase = ((sales_data[3] - sales_data[0]) / sales_data[0]) * 100

print("Total sales for the year:", total_sales)
print("Percentage increase in sales from the first quarter to the fourth quarter:", percentage_increase)
