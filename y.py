def saveThePrisoner(n, m, s):
    # Write your code here
    r = m % n
    if (r+s-1) % n == 0:
        return n
    else:
        return (r+s-1) % n


t = int(input().strip())

for t_itr in range(t):
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    s = int(first_multiple_input[2])

    result = saveThePrisoner(n, m, s)

    print(result)
