list1=[1,2,3,4,5]
list2=[]

for i in range(0,len(list1)):
    mult=1
    k=list1[i]
    list1[i]=1
    for e in list1:
        mult=mult*e
    list1[i]=k
    list2.append(mult)
print(list2)