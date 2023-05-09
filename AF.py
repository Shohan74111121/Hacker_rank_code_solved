def libraryf(d1, m1, y1, d2, m2, y2):
    if y1 > y2:
        f = 10000
    elif y1 == y2 and m1 > m2:
        f = (m1-m2)*500
    elif y1 == y2 and m1 == m2 and d1 > d2:
        f = (d1-d2)*15
    else:
        f = 0
    return f


first_multiple_input = input().rstrip().split()

d1 = int(first_multiple_input[0])

m1 = int(first_multiple_input[1])

y1 = int(first_multiple_input[2])

second_multiple_input = input().rstrip().split()

d2 = int(second_multiple_input[0])

m2 = int(second_multiple_input[1])

y2 = int(second_multiple_input[2])

print(libraryf(d1, m1, y1, d2, m2, y2))
