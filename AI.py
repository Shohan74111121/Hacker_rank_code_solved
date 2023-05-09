import random
import array

# def solve(p):
#     count = 0
#     d=np.array[p]
#     p.sort()
#     while p != d:
#         random.shuffle(d) 
#         count += 1
#     return(f"{count}.000000")


def solve(p):
    count = 1
    arr=[]
    for i in p:
        arr.append(i)
    p.sort()
    while p != arr:
        n=len(arr)-1
        for i in range(n):
            random_index = random.randint(0, n)
            temp = arr.pop(random_index)
            arr.append(temp)
        count+=1
    return (f"{count}.000000")

P_count = int(input().strip())
P = list(map(int, input().rstrip().split()))
r=solve(P)
print(r)
