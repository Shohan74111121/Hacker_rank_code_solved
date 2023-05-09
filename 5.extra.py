# # def difference_of_diagonal_matrix(arr):
# #     n=len(arr)
# #     a=b=0
# #     for i in range(n):
# #         a =+ arr[i][i]
# #         b =+ arr[i][n-i-1]
# #     print(a-b)

# def difference_of_diagonal_matrix(mat):
#     n=len(mat)
#     principal = 0
#     secondary = 0;
#     for i in range(0, n):
#         for j in range(0, n):

#             # Condition for principal diagonal
#             if (i == j):
#                 principal += mat[i][j]

#             # Condition for secondary diagonal
#             if ((i + j) == (n - 1)):
#                 secondary += mat[i][j]

#     print("Principal Diagonal:", principal)
#     print("Secondary Diagonal:", secondary)
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
    a = list(map(int, input().split()))
    for i in range(n):
        arr.append(a[i])
print(arr[2][1])
# difference_of_diagonal_matrix(arr)
