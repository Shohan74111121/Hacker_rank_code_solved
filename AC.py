def findDigits(n):
    k = n
    c = 0
    while k != 0:
        r = k % 10
        if r != 0 and n % r == 0:
            c += 1
        k = k//10
    print(c)


t = int(input().strip())

for i in range(t):
    n = int(input().strip())
    findDigits(n)
