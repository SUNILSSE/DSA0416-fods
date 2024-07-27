import pandas as pd
import matplotlib.pyplot as plt

# Sample dataset
data = {
    'OrderID': [202301010001, 202301020002, 202301030003, 202301040004, 202301050005],
    'CustomerID': [101, 102, 103, 104, 102],
    'ProductID': [1001, 1002, 1003, 1004, 1002],
    'Quantity': [2, 1, 5, 3, 4],
    'TotalPrice': [200, 150, 500, 300, 400]
}
df = pd.DataFrame(data)
df['Order Date'] = pd.to_datetime(df['OrderID'].astype(str).str[:8], format='%Y%m%d')

# Filter data for a specific customer
customer_id = 102
customer_orders = df[df['CustomerID'] == customer_id]
print("Orders placed by customer", customer_id)
print(customer_orders)

# Group by 'CustomerID' and calculate total amount spent
total_spent_by_customer = df.groupby('CustomerID')['TotalPrice'].sum()
print("Total amount spent by each customer:")
print(total_spent_by_customer)

# Visualize the distribution of Total Price using a histogram
plt.figure(figsize=(10, 6))
plt.hist(df['TotalPrice'], bins=20, edgecolor='k')
plt.title('Distribution of Total Price')
plt.xlabel('Total Price')
plt.ylabel('Frequency')
plt.show()
