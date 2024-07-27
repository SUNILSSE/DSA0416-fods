import pandas as pd

# Data for student scores
data = {
    'Math': [85, 90, 75],
    'Science': [92, 88, 95],
    'English': [78, 85, 80]
}

# Student IDs as index labels
index_labels = ['Student1', 'Student2', 'Student3']

# Create DataFrame
df = pd.DataFrame(data, index=index_labels)

# Display the DataFrame
print(df)
