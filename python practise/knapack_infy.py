list1=[1.01,1.99,2.5,1.5,1.01]
list1.sort(reverse=True)
print(list1)
list2=[]
k=0
for i in range(len(list1)-1):
    for j in range(i+1,len(list1)):
        if list1[i]+list1[j]<=3:
            list1.append(list1[i])
            list1.append(list1[j])

    else:
        list2.append(list1[i])



print(list2)