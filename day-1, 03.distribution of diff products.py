import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data={
    'category':['category a','category b','category c'],
    'sales':[10000,15000,20000]
    }
df=pd.DataFrame(data)
print("data:")
print(df)
plt.figure(figsize=(10,6))
plt.plot(df['category'], df['sales'], marker='o',linestyle='-',color='b')
plt.title('sales distribtion across product categories')
plt.xlabel('product category')
plt.ylabel('sales')
plt.grid(True)
plt.show()
plt.figure(figsize=(10,6))
plt.scatter(df['category'], df['sales'],color='g', s=100)
plt.title('sale sdistribution across product categories ')
plt.xlabel('product category')
plt.ylabel('sales')
plt.grid(True)
plt.show()
plt.figure(figsize=(10,6))
plt.bar(df['category'], df['sales'], color='c')
plt.title('Sales Distribution Across Product Categories')
plt.xlabel('Product Category')
plt.ylabel('Sales')
plt.grid(True)
plt.show()

