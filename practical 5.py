n = int(input("Enter number of students: "))

students = []

for i in range(n):

    roll = input("Enter Roll No: ")
    name = input("Enter Name: ")

    marks = []

    for j in range(5):
        mark = int(input("Enter marks: "))
        marks.append(mark)

    total = sum(marks)
    percentage = total / 5

    # Grade
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    students.append([roll, name, total, percentage, grade])


# Sort students according to total marks
students.sort(key=lambda x: x[2], reverse=True)


# Assign ranks
for i in range(n):

    if i > 0 and students[i][2] == students[i - 1][2]:
        rank = students[i - 1][5]
    else:
        rank = i + 1

    students[i].append(rank)


print("\nRank  Roll No  Name  Total  Percentage  Grade")

for student in students:
    print(student[5], student[0], student[1],
          student[2], student[3], student[4])