#!/usr/bin/env python3

# List of student scores
student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

# Highest score function
def highest_score():

    student_scores.sort(reverse=True)
    high_score = student_scores[0]
    return high_score

# Output
print(f"The highest score in the class is: {highest_score()}")
