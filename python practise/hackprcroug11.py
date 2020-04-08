str1="Hhhknnnasrt"
str2=list(str1)
print(str2)
ad_list={}
ls=[]
ls2=[]
for i in range(len(str2)):

    if str2[i] not in ad_list:
        ad_list[str2[i]]=[]
for i in ad_list:
    ls.append(i)

for i in range(len(str2)-1):
    m=ls[i]
    if ls[i].upper:
        k=ls[i].lower()
        for j in range(i+1,len(str2)):
            if k==ls[j]:
                ls2.append(k)
    else:
        k=ls[i].upper()
        for j in range(i+1,len(ls)):
            if k==ls[j]:
                ls2.append(k)


for i in ls2:
    ad_list.pop(i)
    
  
print(ad_list)