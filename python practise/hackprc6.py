ip=list(map(int,input().split()))
ip.sort()
ip.reverse()
sum1=sum(ip)
sum2=sum1//2
bobs=0
i=0
bobl=[]
while(sum2>bobs):
    bobs=bobs+ip[i]
    bobl.append(ip[i])
    i=i+1
print(bobs)
print(bobl)

