import matplotlib.pyplot as plt
import numpy as np
import datetime

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
sales = [1500, 1800, 1700, 1600, 2000, 2100, 1900, 2200, 2300, 2400, 2500, 2600]

plt.figure(figsize=(10, 6))
plt.plot(months, sales, marker='o', linestyle='-', color='b')

plt.title('Monthly Sales Data')
plt.xlabel('Month')
plt.ylabel('Sales ($)')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

dates = [
    '2023-01-01', '2023-02-01', '2023-03-01', '2023-04-01', '2023-05-01', '2023-06-01',
    '2023-07-01', '2023-08-01', '2023-09-01', '2023-10-01', '2023-11-01', '2023-12-01'
]

dates = np.array(dates, dtype='datetime64[D]')

days_between_months = np.diff(dates)

for i, days in enumerate(days_between_months):
    print(f"Days between {dates[i]} and {dates[i+1]}: {days}")
