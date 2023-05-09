
def appendAndDelete(s, t, k):
    c = 0
    m = min(len(s), len(t))
    for i in range(m):
        if s[i] != t[i]:
            break
        c = c+1

    total = len(s)+len(t)
    if total <= 2*c+k and total % 2 == k % 2:
        return ("Yes")
    elif total <= 2*c+k and total < k:
        return ("Yes")
    else:
        return ("No")


s = input()

t = input()

k = int(input().strip())

r = appendAndDelete(s, t, k)
print(r)
