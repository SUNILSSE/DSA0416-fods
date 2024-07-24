import numpy as np

# Sample dataset
house_data = np.array([
	[1, 3, 1200, 200000],  # 1 bedroom, 1200 sqft, $200,000
	[2, 4, 1500, 300000],  # 2 bedrooms, 1500 sqft, $300,000
	[3, 5, 1800, 400000],  # 3 bedrooms, 1800 sqft, $400,000
	[4, 6, 2000, 500000],  # 4 bedrooms, 2000 sqft, $500,000
	[5, 7, 2500, 600000],  # 5 bedrooms, 2500 sqft, $600,000
	[6, 8, 3000, 700000],  # 6 bedrooms, 3000 sqft, $700,000
])

# Find average sale price of houses with more than 4 bedrooms
houses_with_more_than_4_bedrooms = house_data[house_data[:, 1] > 4]
sale_prices = houses_with_more_than_4_bedrooms[:, 3]
average_sale_price = np.mean(sale_prices)

print("Average sale price of houses with more than 4 bedrooms:", average_sale_price)
