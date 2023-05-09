def birthday_Cake_Candles(arr):
    key = c = 0
    for i in range(len(arr)):
        if key < arr[i]:
            key = arr[i]
            c = 0
        if arr[i] == key:
            c += 1
    return c


arr = []
n = int(input())
e = list(map(int, input().split()))
for i in range(n):
    arr.append(e[i])
print(birthday_Cake_Candles(arr))
