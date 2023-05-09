from collections import Counter

def beautifulTriplets(d, arr):
    c = 0
    m = Counter(arr)
    for i in arr:
        if m[i+d]!=0 and m[i+d+d]!=0:
            c += 1
    return c


first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

d = int(first_multiple_input[1])

arr = list(map(int, input().rstrip().split()))

result = beautifulTriplets(d, arr)

print(result)
