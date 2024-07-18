import pandas as pd
import matplotlib.pyplot as plt
data = {
    'OrderID': [1, 2, 3, 4, 5],
    'CustomerID': [101, 102, 101, 103, 102],
    'ProductID': [1001, 1002, 1003, 1001, 1002],
    'Quantity': [2, 1, 5, 2, 3],
    'TotalPrice': [200, 150, 500, 200, 450]
}
df = pd.DataFrame(data)
print("Dataset Head:\n", df.head())
print("\nDataset Info:\n")
df.info()
print("\nMissing Values:\n", df.isnull().sum())
print("\nSummary Statistics:\n", df.describe())

# Total Orders per Customer
orders_per_customer = df.groupby('CustomerID')['OrderID'].count()
print("\nTotal Orders per Customer:\n", orders_per_customer)

# Total Revenue per Customer
revenue_per_customer = df.groupby('CustomerID')['TotalPrice'].sum()
print("\nTotal Revenue per Customer:\n", revenue_per_customer)

# Most Popular Products
popular_products = df.groupby('ProductID')['Quantity'].sum().sort_values(ascending=False)
print("\nMost Popular Products:\n", popular_products)

# Plot total orders per customer
orders_per_customer.plot(kind='bar')
plt.title('Total Orders per Customer')
plt.xlabel('CustomerID')
plt.ylabel('Number of Orders')
plt.show()

# Plot total revenue per customer
revenue_per_customer.plot(kind='bar')
plt.title('Total Revenue per Customer')
plt.xlabel('CustomerID')
plt.ylabel('Total Revenue')
plt.show()
