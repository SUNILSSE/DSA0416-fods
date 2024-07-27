import pandas as pd
import matplotlib.pyplot as plt

# Sample dataset
data = {
    'Category': ['Electronics', 'Clothing', 'Home & Kitchen', 'Books', 'Toys', 'Sports', 'Beauty', 'Automotive', 'Grocery', 'Health'],
    'Sales': [15000, 12000, 18000, 8000, 9000, 11000, 7000, 6000, 13000, 14000]
}
df = pd.DataFrame(data)
plt.figure(figsize=(10, 6))
plt.plot(df['Category'], df['Sales'], marker='o')
plt.title('Sales Distribution Across Product Categories (Line Plot)')
plt.xlabel('Category')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(df['Category'], df['Sales'])
plt.title('Sales Distribution Across Product Categories (Scatter Plot)')
plt.xlabel('Category')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.bar(df['Category'], df['Sales'])
plt.title('Sales Distribution Across Product Categories (Bar Plot)')
plt.xlabel('Category')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.show()
