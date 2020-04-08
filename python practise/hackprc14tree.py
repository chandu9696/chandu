class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key
def insert(temp,key1):
    q=[]
    q.append(temp)
    while(len(q)):
        temp=q[0]
        q.pop(0)
        if not temp.left:
            temp.left=Node(key1)
            break
        else:
            q.append(temp.left)
        if not temp.right:
            temp.right=Node(key1)
            break
        else:
            q.append(temp.right)
def search(root,key):
    if root.val==key:
        return True
    res1=search(root.left,key)
    if res1:
        return True
    res2=search(root.right,key)
    return res2
            
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
key=19
insert(root,key)
def preorder(root):
    if root:
        preorder(root.left)
        print(root.val)
        preorder(root.right)
preorder(root)
t=search(root,4)
print(t)