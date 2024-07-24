import numpy as np

# Step 1: Initialize the fuel efficiency data
fuel_efficiency = np.array([25, 30, 35, 40, 32, 28, 36, 45, 38, 42])

# Step 2: Calculate the average fuel efficiency
average_fuel_efficiency = np.mean(fuel_efficiency)

# Step 3: Determine the percentage improvement in fuel efficiency between two car models
model1_efficiency = fuel_efficiency[0]  # Fuel efficiency of the first car model
model2_efficiency = fuel_efficiency[-1]  # Fuel efficiency of the last car model

percentage_improvement = ((model2_efficiency - model1_efficiency) / model1_efficiency) * 100

# Step 4: Output the results
print("Average Fuel Efficiency:", average_fuel_efficiency)
print("Percentage Improvement in Fuel Efficiency from Model 1 to Model 2:", percentage_improvement)
