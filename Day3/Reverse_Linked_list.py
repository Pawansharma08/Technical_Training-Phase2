class Node:
    def __init__(self,dataval = None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

    def reverse(self):
        prev = None
        curr = self.headval
        while curr  is not None:
            next = curr.nextval
            curr.nextval = prev
            prev = curr
            curr = next
        self.headval = prev

    def push(self,newData):
        newNode = Node(newData)
        newNode.nextval = self.headval
        self.headval = newNode

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

s1 = SLinkedList()
l=[20,30,40]
heed = Node(10)
s1.headval = heed
current = heed
for i in l :
    current.nextval = Node(i)
    current = current.nextval
s1.reverse()
s1.listprint()