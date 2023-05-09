def difference_of_diagonal_matrix(arr):

    n = len(arr)
    rl = ll = 0
    for i in range(n):
        rl += arr[i][i]
        ll += arr[i][n-1-i]
    return (ll-rl)


n = int(input())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))

u = abs(difference_of_diagonal_matrix(arr))
print(u)
