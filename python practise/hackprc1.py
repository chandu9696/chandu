# google remove duplicate and reverse
str1="prerana"
list2=[]
list1=list(str1)
list3=[]
#def dele1(dup1):
    #list1.remove(dup1)
    #return

for i in range(0,len(list1)-1):
    dup=list1[i]
    for j in range(i+1,len(list1)):
        if(dup==list1[j]):
            #dele1(dup)
            list2.append(i)
            break
        else: 
            pass

for j in range(len(list2)):
    ind=int(list2[j])
    list1.pop(ind)
    for i in range(len(list2)):
        list2[i]=list2[i]-1
for j in range(len(list1)-1,-1,-1):
    list3.append(list1[j])


print("".join(list3))

    
