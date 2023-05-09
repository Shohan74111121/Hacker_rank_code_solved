def difference_of_diagonal_matrix(arr):
    n = len(arr)
    rl = ll = 0
    for i in range(n):
        rl += arr[i][i]
        ll += arr[i][n-1-i]
    return (ll-rl)


arr = []
n = int(input())
for i in range(n):
    arr[i] = list(map(int, input().split()))
u = difference_of_diagonal_matrix(arr)

print(u)
