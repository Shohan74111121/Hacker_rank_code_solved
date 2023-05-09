def compareTriplets (a,b):
    alice=bob=0;
    for i in range(3):
      if a[i]>b[i]:
        alice=alice+1
      elif a[i]<b[i]:
        bob=bob+1
    
    return [alice,bob] 
    
    
  
# Alice=input().split()
# Bob=input().split()
# map(int,Alice)
# map(int,Bob)

a=list(map(int,input().split()))
b=list(map(int,input().split()))

print(*compareTriplets(a,b))
