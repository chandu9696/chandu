list1=[2,4,7,8,9]
k=17
for i in range(0,len(list1)-1):
    x=list1[0]+list1[i+1]
    if(x==k):
        print("True")
for i in range(1,len(list1)-1):
    z=list1[1]+list1[i+1]
    if(z==k):
        print("True")
for i in range(1,len(list1)-1):
    m=list1[2]+list1[i+1]
    if(m==k):
        print("True")
for i in range(1,len(list1)-1):
    n=list1[3]+list1[i+1]
    if(n==k):
        print("True")
    