import pandas as pd

# Sample order data
data = {
    'Customer ID': [1, 2, 1, 3, 2, 1, 3, 2],
    'Order Date': ['2023-01-15', '2023-02-10', '2023-03-05', '2023-04-20', '2023-05-25', '2023-06-30', '2023-07-15', '2023-08-10'],
    'Product Name': ['Product A', 'Product B', 'Product A', 'Product C', 'Product B', 'Product A', 'Product C', 'Product B'],
    'Order Quantity': [2, 1, 3, 2, 4, 1, 5, 2]
}

# Create DataFrame
order_data = pd.DataFrame(data)

# Convert 'Order Date' to datetime
order_data['Order Date'] = pd.to_datetime(order_data['Order Date'])

# Total number of orders made by each customer
total_orders_by_customer = order_data.groupby('Customer ID').size()
print("Total number of orders made by each customer:")
print(total_orders_by_customer)

# Average order quantity for each product
average_order_quantity_by_product = order_data.groupby('Product Name')['Order Quantity'].mean()
print("Average order quantity for each product:")
print(average_order_quantity_by_product)

# Earliest and latest order dates
earliest_order_date = order_data['Order Date'].min()
latest_order_date = order_data['Order Date'].max()
print("Earliest order date:", earliest_order_date)
print("Latest order date:", latest_order_date)
