import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import scipy.stats as stats

# Data
data = {
    'Age': [23, 23, 27, 27, 39, 41, 47, 49, 50, 52, 54, 54, 57, 58, 58, 60, 61],
    '%Fat': [9.5, 20.5, 7.6, 17.8, 31.4, 25.0, 27.1, 27.2, 31.2, 31.6, 42.5, 28.8, 33.4, 30.2, 31.2, 34.9, 41.2, 35.7]
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate mean, median, and standard deviation
mean_age = df['Age'].mean()
median_age = df['Age'].median()
std_age = df['Age'].std()

mean_fat = df['%Fat'].mean()
median_fat = df['%Fat'].median()
std_fat = df['%Fat'].std()

print(f"Mean Age: {mean_age}, Median Age: {median_age}, Std Age: {std_age}")
print(f"Mean %Fat: {mean_fat}, Median %Fat: {median_fat}, Std %Fat: {std_fat}")

# Boxplots
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
sns.boxplot(y=df['Age'])
plt.title('Boxplot of Age')

plt.subplot(1, 2, 2)
sns.boxplot(y=df['%Fat'])
plt.title('Boxplot of %Fat')

plt.tight_layout()
plt.show()

# Scatter plot
plt.figure(figsize=(6, 6))
plt.scatter(df['Age'], df['%Fat'])
plt.xlabel('Age')
plt.ylabel('%Fat')
plt.title('Scatter Plot of Age vs %Fat')
plt.show()

# Q-Q plot
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
stats.probplot(df['Age'], dist="norm", plot=plt)
plt.title('Q-Q Plot of Age')

plt.subplot(1, 2, 2)
stats.probplot(df['%Fat'], dist="norm", plot=plt)
plt.title('Q-Q Plot of %Fat')

plt.tight_layout()
plt.show()
