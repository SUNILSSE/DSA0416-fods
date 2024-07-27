import pandas as pd

data = {
    'Order ID': [1, 2, 3, 4, 5],
    'Customer ID': [101, 102, 103, 104, 105],
    'Product ID': [1001, 1002, 1003, 1001, 1002],
    'Quantity': [2, 1, 5, 3, 4],
    'Total Price': [200, 150, 500, 300, 400]
}

df = pd.DataFrame(data)

print("First few rows of the dataset:")
print(df.head())

total_sales = df['Total Price'].sum()
print(f'Total Sales: {total_sales}')

average_quantity = df['Quantity'].mean()
print(f'Average Quantity: {average_quantity}')

top_selling_products = df.groupby('Product ID')['Quantity'].sum().sort_values(ascending=False)
print("Top-selling products:")
print(top_selling_products.head())
