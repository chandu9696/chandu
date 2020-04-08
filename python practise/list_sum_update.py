list1=[2,3,7,9,33]
k=66
def check(arr,m):
    for i in arr:
        if m-i in list1:
            if(i==m):
                print("true")
                break;
check(list1,k)