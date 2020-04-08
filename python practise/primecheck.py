import math
def prime(n):
    if n%2==0:
        return False
    m=int(math.sqrt(n))
    for i in range(2,m,2):
        if(m%i==0):
            return False
    return True

out=prime(28)
print(out)