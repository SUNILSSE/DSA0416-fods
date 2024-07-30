import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report
data = pd.DataFrame({
    'age': [25, 45, 35, 50, 23, 34, 67, 29, 40, 55],
    'gender': [1, 0, 1, 0, 1, 0, 0, 1, 0, 1],  
    'blood_pressure': [120, 140, 130, 150, 110, 125, 160, 115, 135, 145],
    'cholesterol': [200, 240, 220, 260, 180, 210, 270, 190, 230, 250],
    'outcome': ['Good', 'Bad', 'Good', 'Bad', 'Good', 'Good', 'Bad', 'Good', 'Bad', 'Bad']
})

data['outcome'] = data['outcome'].map({'Good': 1, 'Bad': 0})

X = data.drop('outcome', axis=1)
y = data['outcome']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train_scaled, y_train)

y_pred = knn.predict(X_test_scaled)

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print(f'Accuracy: {accuracy:.2f}')
print(f'Precision: {precision:.2f}')
print(f'Recall: {recall:.2f}')
print(f'F1-score: {f1:.2f}')
conf_matrix = confusion_matrix(y_test, y_pred)
print('\nConfusion Matrix:')
print(conf_matrix)
