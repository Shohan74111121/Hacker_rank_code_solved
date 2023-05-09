def repeatedString(s, n):
    d = n // len(s)
    r = n % len(s)
    count_1 = s.count('a')*d
    count_2 = s[:r].count('a')
    return count_1+count_2


s = input()

n = int(input().strip())

print(repeatedString(s, n))
