str1="google"
list2=list(str1)
s=list(dict.fromkeys(list2))
list3=s.reverse()

print("-".join(s))