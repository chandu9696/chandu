import re as r
str1="abc@1244"
li1=list(str1)
lst=[]
for i in li1:
    if i.isdigit():
        lst.append(i)
print(lst)
lst.sort()
lst.reverse()
print("".join(lst))