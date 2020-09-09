ls=[1,2,3,4]
ls1=[7,8,9,4]
flag=True
for i in ls:
    if i in ls1:
        flag=False
print(flag)