import pandas as pd
import numpy as np
from scipy import stats

data = pd.DataFrame({
    'group': ['A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B'],
    'conversion_rate': [0.10, 0.12, 0.11, 0.13, 0.14, 0.15, 0.16, 0.14, 0.17, 0.18]
})

group_A = data[data['group'] == 'A']['conversion_rate']
group_B = data[data['group'] == 'B']['conversion_rate']

t_stat, p_value = stats.ttest_ind(group_A, group_B)

print(f'T-statistic: {t_stat:.2f}')
print(f'P-value: {p_value:.4f}')

alpha = 0.05

if p_value < alpha:
    print("There is a statistically significant difference in the mean conversion rates between website design A and website design B.")
else:
    print("There is no statistically significant difference in the mean conversion rates between website design A and website design B.")
