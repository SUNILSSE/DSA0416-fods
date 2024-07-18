import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
data={
    'cigarettesperday':[0,5,10,15,20,25,30,35,40,45],
    'lungcancerper1000':[1,3,6,8,12,18,25,30,35,45]
    }
df=pd.DataFrame(data)
print("data:")
print(df)
correlation_coefficient,_=pearsonr(df['cigarettesperday'],df['lungcancerper1000'])
print("correlation coefficient")
print(correlation_coefficient)
plt.figure(figsize=(10,6))
plt.scatter(df['cigarettesperday'],df['lungcancerper1000'],color='blue')
plt.title('scatter plot of smoking vs lung cancer incidence')
plt.xlabel('cigarettes smoke per day')
plt.ylabel('lung cancer cases per 1000 individuals')
plt.grid(True)
z=np.polyfit(df['cigarettesperday'],df['lungcancerper1000'], 1)
p=np.poly1d(z)
plt.plot(df['cigarettesperday'],p(df['cigarettesperday']),color='red')
plt.show()
