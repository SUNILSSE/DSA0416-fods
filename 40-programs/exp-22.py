import pandas as pd

# Sample sales data
data = {
    'Product Name': ['Product A', 'Product B', 'Product A', 'Product C', 'Product B', 'Product A', 'Product D', 'Product E', 'Product C', 'Product B'],
    'Order Quantity': [2, 1, 3, 2, 4, 1, 5, 2, 3, 2]
}

sales_data = pd.DataFrame(data)

product_sales = sales_data.groupby('Product Name')['Order Quantity'].sum()

sorted_product_sales = product_sales.sort_values(ascending=False)

top_5_products = sorted_product_sales.head(5)
print("Top 5 products sold the most:")
print(top_5_products)
