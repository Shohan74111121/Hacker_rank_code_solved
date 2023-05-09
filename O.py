def migratoryBirds(arr):
    # Write your code here
    b = [0]*len(arr)
    for i in arr:
        b[i] += 1
    return b.index(max(b))


arr_count = int(input().strip())

arr = list(map(int, input().rstrip().split()))

result = migratoryBirds(arr)

print(result)
