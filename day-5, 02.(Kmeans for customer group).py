import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

data = pd.DataFrame({
    'customer_id': range(1, 11),
    'total_amount_spent': [200, 150, 300, 250, 350, 400, 280, 320, 450, 500],
    'frequency_of_visits': [5, 4, 8, 7, 9, 10, 6, 7, 11, 12]
})
features = data[['total_amount_spent', 'frequency_of_visits']]

scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

inertia = []
for n_clusters in range(1, 11):
    kmeans = KMeans(n_clusters=n_clusters, random_state=0)
    kmeans.fit(scaled_features)
    inertia.append(kmeans.inertia_)

plt.figure(figsize=(8, 6))
plt.plot(range(1, 11), inertia, marker='o')
plt.xlabel('Number of clusters')
plt.ylabel('Inertia')
plt.title('Elbow Method for Optimal Number of Clusters')
plt.show()

optimal_clusters = 3
kmeans = KMeans(n_clusters=optimal_clusters, random_state=0)
data['Cluster'] = kmeans.fit_predict(scaled_features)

plt.figure(figsize=(10, 8))
sns.scatterplot(x='total_amount_spent', y='frequency_of_visits', hue='Cluster', data=data, palette='viridis')
plt.xlabel('Total Amount Spent')
plt.ylabel('Frequency of Visits')
plt.title('Customer Segmentation using K-Means')
plt.legend(title='Cluster')
plt.show()

cluster_summary = data.groupby('Cluster').mean()
print(cluster_summary)
