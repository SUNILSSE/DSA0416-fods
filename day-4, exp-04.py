import pandas as pd

# Sample sales data for the past month
data = {
    'customer_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'age': [25, 34, 22, 45, 34, 22, 22, 45, 25, 34],
    'purchase_amount': [100, 150, 200, 250, 300, 150, 100, 250, 200, 150]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Calculate the frequency distribution of the ages
age_distribution = df['age'].value_counts()

# Print the frequency distribution
print("Frequency distribution of ages of customers who made a purchase in the past month:")
print(age_distribution)
