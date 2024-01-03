#!/usr/bin/env python3

# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

sum_count = 0
student_count = 0
for i in student_heights:
  sum_count += i
  
for i in student_heights:
  student_count += 1

average_height = round((sum_count/student_count))

print(f"total height = {sum_count}")
print(f"number of students = {student_count}")
print(f"average height = {average_height}")

