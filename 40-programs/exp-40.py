import pandas as pd

# Sample dataset
data = {
    'CustomerID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Age': [25, 30, 22, 40, 35, 30, 25, 22, 40, 35],
    'PurchaseAmount': [100, 150, 200, 250, 300, 150, 100, 200, 250, 300]
}
df = pd.DataFrame(data)

age_frequency = df['Age'].value_counts().sort_index()
print("Frequency Distribution of Customer Ages:")
print(age_frequency)
