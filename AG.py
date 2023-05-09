def cutTheSticks(arr):
    while len(arr) != 0:
        print(len(arr))
        mini = min(arr)
        for i in arr:
            i -= mini
        for k in range(arr.count(mini)):
            arr.remove(mini)


n = int(input().strip())

arr = list(map(int, input().rstrip().split()))

cutTheSticks(arr)
