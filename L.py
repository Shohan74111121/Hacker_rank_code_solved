def countApplesAndOranges(s, t, a, b, apples, oranges):
    ap = org = 0
    for i in range(len(apples)):
        if s <= apples[i]+a <= t:
            ap += 1
    for i in range(len(oranges)):
        if s <= oranges[i]+b <= t:
            org += 1
    return ap, org


first_multiple_input = input().rstrip().split()

s = int(first_multiple_input[0])

t = int(first_multiple_input[1])

second_multiple_input = input().rstrip().split()

a = int(second_multiple_input[0])

b = int(second_multiple_input[1])

third_multiple_input = input().rstrip().split()

m = int(third_multiple_input[0])

n = int(third_multiple_input[1])

apples = list(map(int, input().rstrip().split()))

oranges = list(map(int, input().rstrip().split()))

print(*countApplesAndOranges(s, t, a, b, apples, oranges), sep='\n')
