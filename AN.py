def minimumDistances(a):
    for i in range(1, n):
        for j in range(n-i):
            if a[j+i] == a[j]:
                return i

    return -1


n = int(input().strip())

a = list(map(int, input().rstrip().split()))

print(minimumDistances(a))
