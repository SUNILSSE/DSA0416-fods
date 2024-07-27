import pandas as pd
import numpy as np
from scipy import stats

# Sample dataset
data = {
    'product_title': ['Pineapple slicer', 'Levis Jeans Pant', 'Wallet', 'Salwar'],
    'product_category': ['Apparel', 'Apparel', 'Apparel', 'Apparel'],
    'star_rating': [4, 5, 5, 5],
    'review_headline': ['Really good', 'Perfect Dress', 'Love it', 'Awesome'],
    'review_date': ['2013-01-14', '2014-04-22', '2015-07-28', '2015-06-12']
}
df = pd.DataFrame(data)

mean_rating = df['star_rating'].mean()
print(f"Mean Rating: {mean_rating:.2f}")

confidence_level = 0.95
degrees_freedom = len(df['star_rating']) - 1
sample_mean = np.mean(df['star_rating'])
sample_standard_error = stats.sem(df['star_rating'])
confidence_interval = stats.t.interval(confidence_level, degrees_freedom, sample_mean, sample_standard_error)

print(f"95% Confidence Interval for the Mean Rating: {confidence_interval}")
