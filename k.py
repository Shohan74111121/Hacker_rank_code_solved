def gradingStudents(grades):
    arr = []
    for num in grades:
        if num > 37:
            add = num % 5
            if add >= 3:
                num = num+(5-add)
        arr.append(num)
    return arr


total = int(input())

grades = []

for _ in range(total):
    grade = int(input().strip())
    grades.append(grade)

result = gradingStudents(grades)
print(*result, sep='\n')
