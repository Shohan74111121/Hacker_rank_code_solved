def acmTeam(topic):
    t=count=0
    for i in range(n):
        for j in range(i,n):
            s=0
            for k,l in zip(topic[i],topic[j]):
                if k=='1' or l =='1':
                    s+=1 
            if s>t:
                t=s
                count=1
            elif s==t:
                count+=1
    return(t,count)
                



first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

topic = []

for _ in range(n):
    topic_item = input()
    topic.append(topic_item)

result = acmTeam(topic)

print(*result,sep='\n')