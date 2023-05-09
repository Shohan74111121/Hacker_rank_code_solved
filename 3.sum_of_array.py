def sum(a):
    s=0
    for i in range(len(a)):
         s=s+a[i]
    
    return s

arr=[]
n=int(input())
a=list(map(int,input().split()))
for i in range (n):
    arr.append(a[i])

print(sum(arr))