def utopianTree(n):
    height = 0
    for i in range(n+1):
        if i % 2 == 0:
            height += 1
        else:
            height *= 2
    return height




t = int(input().strip())

for t_itr in range(t):
    n = int(input().strip())

    result = utopianTree(n)
    print(result)


