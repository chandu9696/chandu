list1=[13,4,31,6,32,51,89]
list2=[]
dup=0
for i in list1:
    c=list(map(int,str(i)))
    list2.append(sum(c))
list2.sort()
n=len(list2)
for i in range(0,n-1):
    a=list2[i]
    if j in a:
        dup=dup+1
        print(dup)

#print(list3)
#a=list2[0]
#dup=0
#for i in list2:
    
    #if a==i:
        #dup=dup+1
#print(dup)
    #for j in c:
           
       

