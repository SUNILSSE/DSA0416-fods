import numpy sa np
daily_temperatures = [30, 32, 31, 25, 27, 26, 20, 22, 21, 50]  

variance_temp = np.var(daily_temperatures)
print(f"Variance of Daily Temperatures: {variance_temp:.2f}")

z_scores = np.abs(stats.zscore(daily_temperatures))
outliers = np.where(z_scores > 2)
print("Potential Outliers in Daily Temperatures:", daily_temperatures[outliers[0]])
