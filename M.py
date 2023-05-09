def getTotalX(a, b):
    count = 0
    for i in range(1, 101):
        rcm = 0
        for j in a:
            if (i % j != 0):
                rcm = 1
                break
        if (rcm == 0):
            lcm = 0
            for k in b:
                if (k % i != 0):
                    lcm = 1
                    break
            if (lcm == 0):
                count += 1
    return (count)




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

arr = list(map(int, input().rstrip().split()))

brr = list(map(int, input().rstrip().split()))

print(getTotalX(arr, brr))

    
