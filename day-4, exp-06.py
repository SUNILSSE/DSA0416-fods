import pandas as pd
from collections import Counter
import re

# Sample dataset containing customer reviews
data = {
    'review_id': [1, 2, 3, 4, 5],
    'review': [
        "The product is great! I loved it.",
        "Very poor quality, not satisfied.",
        "Excellent product. Exceeded my expectations!",
        "Not bad, but could be better.",
        "I am extremely happy with this purchase!"
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Function to clean and split the reviews into words
def tokenize(text):
    # Convert to lowercase
    text = text.lower()
    # Remove punctuation and non-alphabetic characters
    text = re.sub(r'[^a-z\s]', '', text)
    # Split into words
    words = text.split()
    return words

# Tokenize all reviews
all_words = []
for review in df['review']:
    all_words.extend(tokenize(review))

# Calculate the frequency distribution of words
word_frequency = Counter(all_words)

# Print the frequency distribution
print("Frequency distribution of words in the customer reviews:")
for word, freq in word_frequency.items():
    print(f"{word}: {freq}")
