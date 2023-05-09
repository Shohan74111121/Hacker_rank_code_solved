def runningTime(arr):
    s = 0
    for i in range(1, len(arr)):
        d = arr[i]
        j = i-1

        while j >= 0 and d < arr[j]:
            s += 1
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = d

    return s


arr = []
n = int(input())
e = list(map(int, input().split()))
for i in range(n):
    arr.append(e[i])

print(runningTime(arr))
