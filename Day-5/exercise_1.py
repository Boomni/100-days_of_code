""" 
You are going to write a program that calculates the average student height from a List of heights.

Important You should not use the sum() or len() functions in your answer. You should try to replicate their functionality using what you have learnt about for loops.

Example Input
156 178 165 171 187
In this case, student_heights would be a list that looks like: [156, 178, 165, 171, 187]

Example Output
171
"""

#  🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

count = 0
sum = 0

for heights in student_heights:
  sum += heights
  count += 1

average = sum / count
print(round(average))
