import pandas as pd

# Sample dataset
data = {
    'DISEASE_NAME': ['Common Cold', 'Diabetes', 'Bronchitis', 'Influenza', 'Kidney Stones'],
    'DIAGNOSED_PATIENTS': [320, 120, 100, 150, 60]
}
df = pd.DataFrame(data)

frequency_distribution = df.set_index('DISEASE_NAME')['DIAGNOSED_PATIENTS']
print("Frequency Distribution of Diseases:")
print(frequency_distribution)

most_common_disease = frequency_distribution.idxmax()
most_common_count = frequency_distribution.max()
print(f"\nMost Common Disease: {most_common_disease} with {most_common_count} diagnosed patients")
