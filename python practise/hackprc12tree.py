class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key
root=Node(5)
root.left=Node(6)
root.right=Node(7)
def preorder(root):
    if root:
        preorder(root.left)
        print(root.val)
        preorder(root.right)
preorder(root)