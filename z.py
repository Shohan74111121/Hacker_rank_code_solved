def circularArrayRotation(a, k, queries):
    # Write your code here
    arr = []
    k = k % n
    for i in queries:
        arr.append(a[(n-k+i) % n])

    return arr


first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

k = int(first_multiple_input[1])

q = int(first_multiple_input[2])

a = list(map(int, input().rstrip().split()))

queries = []

for _ in range(q):
    queries_item = int(input().strip())
    queries.append(queries_item)

result = circularArrayRotation(a, k, queries)

print(*result, sep='\n')
