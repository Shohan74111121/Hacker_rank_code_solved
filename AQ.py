def birthday(s, d, m):
    c = 0
    j = 0
    for i in range(n-m+1):
        if sum(s[j:j+m]) == d:
            c += 1
        j = j+1
    return c


n = int(input().strip())

s = list(map(int, input().rstrip().split()))

first_multiple_input = input().rstrip().split()

d = int(first_multiple_input[0])

m = int(first_multiple_input[1])

print(birthday(s, d, m))
