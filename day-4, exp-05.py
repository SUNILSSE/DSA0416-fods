import pandas as pd

# Sample dataset containing user interaction data
data = {
    'post_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'likes': [100, 150, 100, 200, 150, 200, 100, 300, 150, 100]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Calculate the frequency distribution of likes
likes_distribution = df['likes'].value_counts()

# Print the frequency distribution
print("Frequency distribution of likes among the posts:")
print(likes_distribution)
