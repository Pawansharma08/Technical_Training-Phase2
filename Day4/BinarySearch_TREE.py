class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.rigth = None

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(str(root.key)+"->",end='')
        inorder(root.rigth)

def insert(node,key):
    if node is None:
        return Node(key)

    if key < node.key:
        node.left = insert(node.left,key)
    else:
        node.rigth = insert(node.rigth,key)
    return node

def preorder(root):
    if root is not None:
        print(str(root.key) + "->",end = '')
        preorder(root.left)
        preorder(root.rigth)


def minValueMethod(node):
    curr = node
    while curr.left is not None:
        curr = curr.left
    return curr


root = None
root= insert(root,8)
root= insert(root,3)
root = insert(root,1)
root = insert(root,6)
root = insert(root,4)
root = insert(root,7)
root = insert(root,10)
inorder(root)


