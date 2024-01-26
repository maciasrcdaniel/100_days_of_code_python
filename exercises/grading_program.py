#!/usr/bin/env python3

# student score dictionary
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}

# Store an empty dictionary
student_grades = {}

# Take the student score and replace the score based off of
for x_value, y_value in student_scores.items():
    if 90 < y_value < 101:
        student_scores[x_value] = "Outstanding"
        student_grades = student_scores
    elif 80 < y_value < 91:
        student_scores[x_value] = "Exceeds Expectations"
        student_grades = student_scores
    elif 70 < y_value < 81:
        student_scores[x_value] = "Acceptable"
        student_grades = student_scores
    elif 71 < y_value:
        student_scores[x_value] = "Fail"
        student_grades = student_scores


print(student_grades)