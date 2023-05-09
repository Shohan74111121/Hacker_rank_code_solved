def jumpingOnClouds(c, k):
    e = 100
    j = k % n
    if c[j] == 1:
        e = e-2
    e = e-1
    while j != 0:
        j = (j+k) % n
        if c[j] == 1:
            e = e-2
        e = e-1

    return e


nk = input().split()

n = int(nk[0])

k = int(nk[1])

c = list(map(int, input().rstrip().split()))

result = jumpingOnClouds(c, k)

print(result)