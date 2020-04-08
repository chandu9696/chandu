low=2
high=11
def prime(k):
    sum=1
    for i in range(2,k+1):
        if(k%i==0):
            sum=sum+i
    if(sum==k+1):
        return True
    else:
        return False
def low_prime(k1):
    for i in range(k1-1,0,-1):
        ot=prime(i)
        if(ot):
            return i
            
def high_prime(k2):
    k2=k2+1
    while(True):
        ot1=prime(k2)
        if(ot1):
            return k2
            
        k2=k2+1
stp=[]
for i in range(low,high+1):
    if(i==2):
        continue
    
    out_=prime(i)
    if(out_):
        lower=low_prime(i)
        high=high_prime(i)
        if(2*i>lower+high):
            stp.append(i)
print(stp)

