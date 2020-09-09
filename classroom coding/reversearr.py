ls=[1,2,3,4]
ls1=[]
ls=[ls1.append(ls[i]) for i in range(len(ls)-1,-1,-1)]
print(ls1)