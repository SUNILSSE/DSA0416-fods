import numpy as np

# Sample input data (4x4 matrix of marks, each row represents a student)
# Assume marks are arranged by subject across columns
marks = np.array([
    [85, 90, 88, 92],
    [75, 82, 80, 78],
    [90, 92, 94, 88],
    [80, 85, 78, 82]
])

# Calculate the average score for each subject (column-wise mean)
subject_averages = np.mean(marks, axis=0)

# Determine the subject with the highest average score
highest_avg_subject_index = np.argmax(subject_averages)
highest_avg_score = subject_averages[highest_avg_subject_index]

# Mapping index to subject names (assuming subjects are numbered 0 to 3)
subject_names = ['Subject A', 'Subject B', 'Subject C', 'Subject D']
highest_avg_subject = subject_names[highest_avg_subject_index]

# Print results
print("Average Scores for Each Subject:")
for i, avg_score in enumerate(subject_averages):
    print(f"{subject_names[i]}: {avg_score:.2f}")

print("\nSubject with the Highest Average Score:")
print(f"{highest_avg_subject} with an average score of {highest_avg_score:.2f}")
