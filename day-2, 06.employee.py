import pandas as pd
from datetime import datetime

# Sample data
data = {
    'Employee ID': [1, 2, 3, 4, 5],
    'Department': ['HR', 'IT', 'HR', 'Finance', 'IT'],
    'Salary': [50000, 60000, 55000, 70000, 65000],
    'Joining Date': ['2020-01-15', '2019-03-10', '2021-06-25', '2018-07-30', '2020-11-05']
}

# Create DataFrame
df = pd.DataFrame(data)

# Convert 'Joining Date' to datetime
df['Joining Date'] = pd.to_datetime(df['Joining Date'])

# Determine the highest and lowest salaries in each department
salary_stats = df.groupby('Department')['Salary'].agg(['max', 'min']).reset_index()
print("Highest and lowest salaries in each department:")
print(salary_stats)

# Calculate the average tenure of employees in the company
current_date = datetime.now()
df['Tenure'] = (current_date - df['Joining Date']).dt.days / 365
average_tenure = df['Tenure'].mean()
print("\nAverage tenure of employees in the company:", average_tenure)

# Identify employees who joined before a specific date
specific_date = '2020-01-01'
employees_before_date = df[df['Joining Date'] < specific_date]
print("\nEmployees who joined before", specific_date, ":")
print(employees_before_date)
