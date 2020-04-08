for i in range(4):
    for j in range(4-i-1):
        print(end=" ")
    for k in range(i+1):
        print("*",end=" ")
    print()
for i in range(3):
    for k in range(i+1):
        print(end=" ")
    for j in range(3-i):
        print("*",end=" ")
    print()
