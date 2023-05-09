def viralAdvertising(n):
    share = 5
    liked = count = 0
    for i in range(1, n+1):
        liked = share//2
        share = liked*3
        count += liked
    return count


n = int(input().strip())

print(viralAdvertising(n))
