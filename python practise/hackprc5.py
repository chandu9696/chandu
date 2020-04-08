arr=[1,2,3,4,5]
m=3
intl=max(arr)
endl=sum(arr)+1
k=intl

while(True):
    cur_sum=arr[0]
    subs=1
    flag=True
    for i in range(1,len(arr)):
        if arr[i]+cur_sum>k:
            cur_sum=arr[i]
            subs=subs+1
        else:
            cur_sum=arr[i]+cur_sum
        if subs>m:
            flag=False
            break
    if(flag):
        print(k)
        break
    k=k+1


    