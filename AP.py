def breakingRecords(scores):
    maxi=mini=scores[0]
    max_count=min_count=0
    for i in scores:
        if maxi<i:
            maxi=i
            max_count+=1
        if mini>i:
            mini=i
            min_count+=1
    return max_count,min_count
            

n = int(input().strip())

scores = list(map(int, input().rstrip().split()))

print(*breakingRecords(scores),sep=' ')