def sockMerchant(arr):
    t={}
    count=0
    for i in arr:
        if i in t:
            count+=1
            t.pop(i)
        else:
            t[i]=1
    return count





arr=[]
n=int(input())
e=list(map(int,input().split()))
for i in range (n):
    arr.append(e[i])

print(sockMerchant(arr))
