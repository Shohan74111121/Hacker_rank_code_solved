def kangaroo(x1, v1, x2, v2):
    if v1 > v2:
        r = (x1-x2) % (v1-v2)
        if r == 0:
            return 'YES'
        else:
            return 'NO'
    return 'NO'


first_multiple_input = input().rstrip().split()

x1 = int(first_multiple_input[0])

v1 = int(first_multiple_input[1])

x2 = int(first_multiple_input[2])

v2 = int(first_multiple_input[3])

print(kangaroo(x1, v1, x2, v2))
