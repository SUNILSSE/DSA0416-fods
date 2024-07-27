import pandas as pd

data = {
    'Property ID': [1, 2, 3, 4, 5],
    'Location': ['Location A', 'Location B', 'Location A', 'Location C', 'Location B'],
    'Number of Bedrooms': [3, 5, 4, 6, 2],
    'Area (sq ft)': [2000, 3500, 2500, 4000, 1500],
    'Listing Price': [300000, 500000, 400000, 600000, 250000]
}

property_data = pd.DataFrame(data)

average_price_by_location = property_data.groupby('Location')['Listing Price'].mean()
print("Average listing price of properties in each location:")
print(average_price_by_location)

properties_with_more_than_four_bedrooms = (property_data['Number of Bedrooms'] > 4).sum()
print("Number of properties with more than four bedrooms:", properties_with_more_than_four_bedrooms)

largest_area_property = property_data.loc[property_data['Area (sq ft)'].idxmax()]
print("Property with the largest area:")
print(largest_area_property)
