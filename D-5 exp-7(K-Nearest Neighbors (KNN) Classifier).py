import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

data = pd.DataFrame({
    'symptom1': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'symptom2': [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
    'condition': [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
})

X = data.drop('condition', axis=1)
y = data['condition']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

k = 3  
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(X_train_scaled, y_train)

new_patient = pd.DataFrame({
    'symptom1': [5],
    'symptom2': [6]
})

new_patient_scaled = scaler.transform(new_patient)

predicted_condition = knn.predict(new_patient_scaled)
print(f'Predicted Condition: {predicted_condition[0]}')
