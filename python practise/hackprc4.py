list1=[10,9,4,5,7,2,8,20,21]
num=15
list2=[]
for i in range(len(list1)-1):
    a=list1[i]
    for j in range(i+1,len(list1)):
        ad=a+list1[j]
        list2.append(ad)
count=0
for e in list2:
    if(e%num==0):
        count=count+1
print(count)