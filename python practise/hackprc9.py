import math

ip=int(input())
ip1=ip
list1=[1,2,4,8,16,32]
ind=[]
def covbi():
    while(True):
        if(ip==0):
            break
        if ip in list1:
            index1=list1.index(ip)
            ind.append(index1)
            ip=ip1-ip
            ip1=ip

        else:
            ip=ip-1
    for i in range(len(ind)):

        ind[i]=ind[i]+1

def prime(n):
    if n%2==0:
        return False
    m=int(math.sqrt(n))
    for i in range(2,m,2):
        if(m%i==0):
            return False
    return True
-