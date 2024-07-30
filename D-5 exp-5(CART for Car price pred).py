import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor, export_text
from sklearn.metrics import mean_squared_error, r2_score

data = pd.DataFrame({
    'mileage': [15000, 30000, 45000, 60000, 75000, 90000, 105000, 120000, 135000, 150000],
    'age': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'brand': [1, 1, 2, 2, 3, 3, 1, 2, 3, 1],  # 1: Brand A, 2: Brand B, 3: Brand C
    'engine_type': [1, 2, 1, 2, 1, 2, 1, 2, 1, 2],  # 1: Petrol, 2: Diesel
    'price': [20000, 18000, 25000, 22000, 27000, 24000, 19000, 21000, 26000, 23000]
})

X = data.drop('price', axis=1)
y = data['price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
model = DecisionTreeRegressor(random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Mean Squared Error: {mse:.2f}')
print(f'R-squared: {r2:.2f}')
new_car = pd.DataFrame({
    'mileage': [50000],
    'age': [3],
    'brand': [2],  
    'engine_type': [1] 
})

predicted_price = model.predict(new_car)
print(f'Predicted Price for the new car : ${predicted_price}')
