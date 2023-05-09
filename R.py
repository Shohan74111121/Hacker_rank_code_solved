def countingValleys(path):
    count = vally = 0
    for i in path:
        if i == "U":
            vally += 1
            if vally == 0:
                count += 1
        elif i == "D":
            vally -= 1
    return count


steps = int(input().strip())

path = input()

print(countingValleys(path))
