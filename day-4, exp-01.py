import pandas as pd
import numpy as np
from scipy import stats

# Sample data
data = {
    "product_title": ["Pineapple slicer", "Levis Jeans Pant", "Wallet", "Salwar"],
    "product_category": ["Apparel", "Apparel", "Apparel", "Apparel"],
    "star_rating": [4, 5, 5, 5],
    "review_headline": ["Really good", "Perfect Dress", "Love it", "Awesome"],
    "review_date": ["2013-01-14", "2014-04-22", "2015-07-28", "2015-06-12"]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Filter DataFrame for the 'Apparel' category
apparel_reviews = df[df['product_category'] == 'Apparel']

# Calculate mean rating
mean_rating = apparel_reviews['star_rating'].mean()

# Calculate confidence interval for the mean rating
confidence_level = 0.95
degrees_freedom = len(apparel_reviews) - 1
sample_mean = np.mean(apparel_reviews['star_rating'])
sample_standard_error = stats.sem(apparel_reviews['star_rating'])

confidence_interval = stats.t.interval(
    confidence_level, 
    degrees_freedom, 
    sample_mean, 
    sample_standard_error
)

# Print the results
print(f"Average Rating: {mean_rating}")
print(f"95% Confidence Interval: {confidence_interval}")
