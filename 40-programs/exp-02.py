import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Smoking': [20, 15, 5, 25, 30, 10, 18, 22, 8, 12],
    'LungCancer': [5, 4, 1, 6, 8, 2, 3, 7, 1, 2]
}

df = pd.DataFrame(data)
correlation = df['Smoking'].corr(df['LungCancer'])
print(f'Correlation Coefficient: {correlation}')
plt.scatter(df['Smoking'], df['LungCancer'])
plt.title('Scatter Plot of Smoking vs Lung Cancer')
plt.xlabel('Smoking (cigarettes per day)')
plt.ylabel('Lung Cancer Cases')
plt.show()
