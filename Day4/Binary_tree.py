class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.rigth = None

def in_order(root):
    if root:
        in_order(root.left)
        print(str(root.data) + "->",end = '')
        in_order(root.rigth)

def preorder(root):
    if root:
        print(str(root.data) + "->",end = '')
        preorder(root.left)
        preorder(root.rigth)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.rigth)
        print(str(root.data) + "->", end='')



root = Node(1)
root.left = Node(2)
root.rigth = Node(3)
root.left.left = Node(4)
root.left.rigth = Node(5)

preorder(root)
print("in_order")
in_order(root)
print("Post_order")
postorder(root)