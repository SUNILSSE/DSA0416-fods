import numpy as np
import matplotlib.pyplot as plt

smoking_patients = [200, 220, 240, 260, 300]
lung_cancer_patients = [25, 30, 35, 40, 55]
years = [2015, 2016, 2017, 2018, 2019]

correlation_coefficient = np.corrcoef(smoking_patients, lung_cancer_patients)[0, 1]
print(f"The correlation coefficient between smoking patients and lung cancer patients is: {correlation_coefficient:.2f}")

plt.scatter(smoking_patients, lung_cancer_patients)
plt.title('Scatter Plot of Smoking Patients vs Lung Cancer Patients')
plt.xlabel('Number of Smoking Patients')
plt.ylabel('Number of Lung Cancer Patients')
plt.show()
