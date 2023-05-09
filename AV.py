def equalizeArray(arr):
    a = maxi = 0
    for i in arr:
        a = arr.count(i)
        if maxi < a:
            maxi = a
    return len(arr)-maxi


n = int(input().strip())

arr = list(map(int, input().rstrip().split()))

print(equalizeArray(arr))
