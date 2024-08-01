import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

data = pd.DataFrame({
    'purchase_history': [5, 3, 6, 2, 8, 7, 4, 5, 9, 10],
    'browsing_behavior': [20, 15, 25, 10, 30, 28, 18, 22, 35, 40],
    'age': [25, 34, 45, 23, 35, 40, 30, 28, 50, 60],
    'income': [50000, 60000, 55000, 45000, 70000, 65000, 48000, 52000, 75000, 80000]
})

features = data[['purchase_history', 'browsing_behavior', 'age', 'income']]

scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

kmeans = KMeans(n_clusters=3, random_state=42)
data['Cluster'] = kmeans.fit_predict(scaled_features)

new_customer = pd.DataFrame({
    'purchase_history': [7],
    'browsing_behavior': [25],
    'age': [30],
    'income': [60000]
})

new_customer_scaled = scaler.transform(new_customer)

predicted_cluster = kmeans.predict(new_customer_scaled)
print(f'Predicted Cluster: {predicted_cluster[0]}')
