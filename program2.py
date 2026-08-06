# Missing Roll Number
# Roll numbers should be from 1 to N.
# One roll number is missing.
# Find the missing roll number without sorting.




n = int(input("Enter total students: "))

roll = []

for i in range(n - 1):
    r = int(input("Enter roll number: "))
    roll.append(r)

for i in range(1, n + 1):

    found = False

    for j in roll:
        if i == j:
            found = True
            break

    if found == False:
        print("Missing Roll Number:", i)
