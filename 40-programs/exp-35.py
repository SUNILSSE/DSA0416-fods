import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Age': [22, 25, 39, 45, 33],
    'Salary': [40000, 45000, 150000, 200000, 120000]
}
df = pd.DataFrame(data)

correlation_matrix = df.corr()
print("Correlation Matrix:")
print(correlation_matrix)

covariance = df.cov()
print("\nCovariance:")
print(covariance)

sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix Heatmap')
plt.show()

sns.pairplot(df)
plt.show()
