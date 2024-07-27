import numpy as np

# Sample fuel efficiency data for different car models
fuel_efficiency = np.array([25, 30, 35, 40, 45, 50])

# Calculate average fuel efficiency
average_fuel_efficiency = fuel_efficiency.mean()
print("Average fuel efficiency:", average_fuel_efficiency)

# Calculate percentage improvement in fuel efficiency between two car models
initial_efficiency = fuel_efficiency[0]
final_efficiency = fuel_efficiency[-1]
percentage_improvement = ((final_efficiency - initial_efficiency) / initial_efficiency) * 100
print("Percentage improvement in fuel efficiency:", percentage_improvement)
