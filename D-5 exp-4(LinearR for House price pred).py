import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

data = pd.DataFrame({
    'house_size': [1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400],
    'price': [300000, 320000, 340000, 360000, 380000, 400000, 420000, 440000, 460000, 480000]
})

plt.figure(figsize=(10, 6))
sns.scatterplot(x='house_size', y='price', data=data)
plt.title('House Size vs. Price')
plt.xlabel('House Size (sq ft)')
plt.ylabel('Price ($)')
plt.show()

X = data[['house_size']]
y = data['price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Mean Squared Error: {mse:.2f}')
print(f'R-squared: {r2:.2f}')

plt.figure(figsize=(10, 6))
sns.scatterplot(x='house_size', y='price', data=data)
plt.plot(X_test, y_pred, color='red', linewidth=2)
plt.title('House Size vs. Price with Regression Line')
plt.xlabel('House Size (sq ft)')
plt.ylabel('Price ($)')
plt.show()
