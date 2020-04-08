import math

low=int(input())

high=int(input())
luck=[]
for i in range(low,high+1):
    root=math.sqrt(i)
    if int(root+0.5)**2==i:
        pass
    else:
        luck.append(i)

print(luck)