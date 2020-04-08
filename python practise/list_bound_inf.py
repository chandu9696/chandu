list1=[3,2,6,5,1,4,8,9]

i=0
for i in range(0,len(list1)-1):
    if(list1[i]==5):
        k=i #to find the index of element 5
        break
    
m=k+1
x=k+1
#assign next value of 5
num2=""
while(list1[m]!=8):
    s=str(list1[m])
    num2=num2+s #while we not get 8 concantenating
    m=m+1
while(list1[x]!=8):
    list1.pop(x)
list1.pop(x)#pop 8 abd 5
list1.pop(k)
num1=sum(list1)
num22=int(num2)
print("and we are done",num1+num22)