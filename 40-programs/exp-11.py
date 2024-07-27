import numpy as np

# Sample student scores (4 students, 4 subjects)
student_scores = np.array([
    [85, 90, 78, 92],
    [88, 76, 85, 80],
    [90, 88, 82, 85],
    [70, 75, 80, 78]
])

# Subjects
subjects = ['Math', 'Science', 'English', 'History']

# Calculate average scores for each subject
average_scores = student_scores.mean(axis=0)
print("Average scores for each subject:", average_scores)

# Find the subject with the highest average score
highest_avg_subject_index = np.argmax(average_scores)
highest_avg_subject = subjects[highest_avg_subject_index]
print("Subject with the highest average score:", highest_avg_subject)
