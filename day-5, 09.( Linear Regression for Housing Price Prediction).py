import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

data = pd.DataFrame({
    'area': [1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400],
    'bedrooms': [3, 3, 3, 4, 4, 4, 5, 5, 5, 5],
    'location': [1, 2, 1, 2, 1, 2, 1, 2, 1, 2],  # 1: Location A, 2: Location B
    'price': [300000, 320000, 340000, 360000, 380000, 400000, 420000, 440000, 460000, 480000]
})

X = data.drop('price', axis=1)
y = data['price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

new_house = pd.DataFrame({
    'area': [2000],
    'bedrooms': [4],
    'location': [1]
})

predicted_price = model.predict(new_house)
print(f'Predicted Price: ${predicted_price[0]:.2f}')
