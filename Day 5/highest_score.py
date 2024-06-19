student_score = input().split()
for n in range(0, len(student_score)):
    student_score[n] = int(student_score[n])  # converts string into integer

highest_score = 0
for score in student_score:
    if score > highest_score:
        highest_score = score
print("Highest score : ", highest_score)
