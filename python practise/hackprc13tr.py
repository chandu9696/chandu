class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key



        
no=int(input("enter number of nodes"))

m=1
for i in range(no-1):
    pair=list(map(int,input().split()))
    if(i==0):
        root=Node(pair[0])
        root.left=Node(pair[1])
        temp=root
    else:
        while(True):
            if(root.val==pair[0]):
                if not root.left:
                    root.left=Node(pair[1])
                    break
                if not root.right:
                    root.right=Node(pair[1])
                    break
                m=1
                

            else:
                if(m==1):
                    root=root.right
                else:
                    root=root.left
                m=2
#print(root.val)
def preorder(root):
    if root:
        preorder(root.left)
        preorder(root.right)
preorder(temp)