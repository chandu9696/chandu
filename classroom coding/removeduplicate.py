ls=[1,2,3,4,4]
ls1=[]
for i in ls:
    if i not in ls1:
        ls1.append(i)
print(ls1)