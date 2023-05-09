def bonAppetit(bill, k, b):
    t = sum(bill)-bill[k]
    half = t//2
    if half == b:
        return 'Bon Appetit'
    return abs(half-b)


first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

k = int(first_multiple_input[1])

bill = list(map(int, input().rstrip().split()))

b = int(input().strip())

print(bonAppetit(bill, k, b))
