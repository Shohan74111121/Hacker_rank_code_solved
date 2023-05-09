def bigSorting(l):
    l.sort(key=lambda i:(len(i),i))
    return l
    


n = int(input().strip())

unsorted = []

for _ in range(n):
    unsorted_item = input()
    unsorted.append(unsorted_item)

result = bigSorting(unsorted)
print (*result,sep='\n')