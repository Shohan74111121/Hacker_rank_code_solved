def plusMinus  (arr):
    n=len(arr)
    m=z=p=0
    for i in range (n):
        if arr[i]<0:
            m+=1
        elif arr[i]==0:
            z+=1
        else:
            p+=1
    print(p/n)
    print(m/n)     
    print(z/n)



# print(f"{(p/n):.6f}")
            
        
arr=[]
n=int(input())
e=list(map(int,input().split()))
for i in range (n):
    arr.append(e[i])
plusMinus (arr)


