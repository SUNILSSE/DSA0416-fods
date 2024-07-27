import pandas as pd

# Sample employee data
data = {
    'Employee ID': [1, 2, 3, 4, 5],
    'Department': ['HR', 'Engineering', 'HR', 'Engineering', 'Sales'],
    'Salary': [50000, 80000, 60000, 75000, 55000],
    'Joining Date': ['2020-01-15', '2019-03-10', '2021-06-25', '2018-07-30', '2020-11-05']
}

# Create DataFrame
df = pd.DataFrame(data)

# Convert 'Joining Date' to datetime
df['Joining Date'] = pd.to_datetime(df['Joining Date'])

# Determine the highest and lowest salaries in each department
salary_stats = df.groupby('Department')['Salary'].agg(['max', 'min'])
print("Highest and lowest salaries in each department:")
print(salary_stats)

# Calculate tenure in days
df['Tenure'] = (pd.to_datetime('today') - df['Joining Date']).dt.days

# Calculate average tenure
average_tenure = df['Tenure'].mean()
print("Average tenure of employees (in days):", average_tenure)

# Specific date
specific_date = '2020-01-01'

# Filter employees who joined before the specific date
employees_before_date = df[df['Joining Date'] < specific_date]
print("Employees who joined before", specific_date)
print(employees_before_date)
