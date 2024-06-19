# Taking input of student heights as a single string and splitting it into a list
student_height = input("Enter the heights of students separated by spaces: ").split()

# Converting each height from string to integer
for n in range(0, len(student_height)):
    student_height[n] = int(student_height[n])

# Calculating the total height
total_height = 0
for height in student_height:
    total_height += height
print("Total height:", total_height)

# Calculating the number of students
number_of_students = 0
for student in student_height:
    number_of_students += 1
print("Number of students:", number_of_students)

# Calculating the average height
average_height = round(total_height / number_of_students)
print("Average height:", average_height)
