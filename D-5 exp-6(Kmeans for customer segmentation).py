import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

data = pd.DataFrame({
    'customer_id': range(1, 11),
    'purchase_history': [5, 3, 6, 2, 8, 7, 4, 5, 9, 10],
    'browsing_behavior': [20, 15, 25, 10, 30, 28, 18, 22, 35, 40],
    'age': [25, 34, 45, 23, 35, 40, 30, 28, 50, 60],
    'income': [50000, 60000, 55000, 45000, 70000, 65000, 48000, 52000, 75000, 80000]
})

features = data[['purchase_history', 'browsing_behavior', 'age', 'income']]

scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, random_state=42)
    kmeans.fit(scaled_features)
    wcss.append(kmeans.inertia_)

plt.figure(figsize=(10, 6))
plt.plot(range(1, 11), wcss, marker='o')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.title('Elbow Method for Optimal Number of Clusters')
plt.show()

optimal_clusters = 3
kmeans = KMeans(n_clusters=optimal_clusters, random_state=42)
data['Cluster'] = kmeans.fit_predict(scaled_features)

plt.figure(figsize=(10, 6))
sns.scatterplot(x='purchase_history', y='browsing_behavior', hue='Cluster', data=data, palette='viridis')
plt.xlabel('Purchase History')
plt.ylabel('Browsing Behavior')
plt.title('Customer Segmentation using K-Means')
plt.legend(title='Cluster')
plt.show()

cluster_summary = data.groupby('Cluster').mean()
print(cluster_summary)
