def getMoneySpent(keyboards, drives, b):
    combos = []

    for i in keyboards:
        for j in drives:
            if i+j <= b:
                combos.append(i+j)
            else:
                combos.append(-1)
    return max(combos)

bnm = input().split()

b = int(bnm[0])

n = int(bnm[1])

m = int(bnm[2])

keyboards = list(map(int, input().rstrip().split()))

drives = list(map(int, input().rstrip().split()))

moneySpent = getMoneySpent(keyboards, drives, b)

print(moneySpent)