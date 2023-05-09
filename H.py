arr=[]
e=list(map(int,input().split()))
for i in range (len(e)):
    arr.append(e[i])
n=len(arr)
total=sum(arr)
maximun=max(arr)
minimum=min(arr)
print(total-maximun,total-minimum)
# print(f"{sum(arr[:n-1])} {sum(arr[1:])}")
