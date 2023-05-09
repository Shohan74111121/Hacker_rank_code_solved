def jumpingOnClouds(c):
    jump = 0
    n = len(c)
    i = 0
    while i < n-1:
        if i+2 < n and c[i+2] == 0:
            i += 2
            jump += 1
        else:
            jump += 1
            i += 1
    return jump


n = int(input().strip())

c = list(map(int, input().rstrip().split()))

result = jumpingOnClouds(c)

print(result)
