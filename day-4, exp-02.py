# Given dataset
diseases = {
    "Common Cold": 320,
    "Diabetes": 120,
    "Bronchitis": 100,
    "Influenza": 150,
    "Kidney Stones": 60
}

# Calculate the most common disease
most_common_disease = max(diseases, key=diseases.get)

# Print the most common disease
print(f"The most common disease is {most_common_disease} with {diseases[most_common_disease]} diagnosed patients.")
