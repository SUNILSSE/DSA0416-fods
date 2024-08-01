import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

data = pd.DataFrame({
    'usage_minutes': [200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100],
    'contract_duration': [12, 24, 12, 24, 12, 24, 12, 24, 12, 24],
    'churn': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
})

X = data.drop('churn', axis=1)
y = data['churn']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = LogisticRegression(random_state=42)
model.fit(X_train_scaled, y_train)

new_customer = pd.DataFrame({
    'usage_minutes': [750],
    'contract_duration': [12]
})

new_customer_scaled = scaler.transform(new_customer)

predicted_churn = model.predict(new_customer_scaled)
print(f'Predicted Churn: {predicted_churn[0]}')
