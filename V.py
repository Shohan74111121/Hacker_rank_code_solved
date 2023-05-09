def hurdleRace(k, height):
    # Write your code here
    maxi = max(height)
    race = maxi-k
    if race < 0:
        return 0
    return race


first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

k = int(first_multiple_input[1])

height = list(map(int, input().rstrip().split()))

result = hurdleRace(k, height)

print(result)
