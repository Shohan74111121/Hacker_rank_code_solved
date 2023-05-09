def timeConversion(s):
    if 'PM' in s and s[:2] != '12':
        s = str(12+int(s[:2]))+s[2:]
    if 'AM' in s and s[:2] == '12':
        s = str('00'+s[2:])
    return (s[:-2])


s = input()
print(timeConversion(s))
