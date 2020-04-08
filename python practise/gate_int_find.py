list1=[3,2,-1,-2,1,5,2,0,4,7,11]
list1.sort()
for i in range(0,len(list1)):
    if(list1[i]>0):
        k=i
        break

del list1[0:k]
list1=list(dict.fromkeys(list1))#duplicate delection
k=1
for e in list1:
    if(e==k):
        pass
    else:
        print(k)
        break
    k=k+1
