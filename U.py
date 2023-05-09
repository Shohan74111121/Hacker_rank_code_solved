def pickingcountbers(a):
    a.sort()
    maxi = start = count = 0
    for i in range(len(a)):
        if a[i]-a[start] >= 2:
            count = 1
            maxi = max(maxi, i-start)
            start = i
        else:
            count += 1
    return max(maxi, count)


n = int(input().strip())

a = list(map(int, input().rstrip().split()))

result = pickingcountbers(a)
print(result)
