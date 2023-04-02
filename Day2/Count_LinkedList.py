class Node:
    def __init__(self,dataval):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None


    def listprint(self):
        c=0
        printval = self.headval
        while printval is not None:
            c+=1
            printval = printval.nextval
        return c
s1 = SLinkedList()
l=[20,30,40]
heed = Node(10)
s1.headval = heed
current = heed
for i in l :
    current.nextval = Node(i)
    current = current.nextval
z = s1.listprint()
print(z)