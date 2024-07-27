import numpy as np

# Sample house data (number of bedrooms, square footage, sale price)
house_data = np.array([
    [3, 2000, 300000],
    [5, 3500, 500000],
    [4, 2500, 400000],
    [6, 4000, 600000],
    [5, 3000, 450000]
])

# Filter houses with more than four bedrooms
houses_with_more_than_four_bedrooms = house_data[house_data[:, 0] > 4]

# Calculate the average sale price of the filtered houses
average_sale_price = houses_with_more_than_four_bedrooms[:, 2].mean()
print("Average sale price of houses with more than four bedrooms:", average_sale_price)
