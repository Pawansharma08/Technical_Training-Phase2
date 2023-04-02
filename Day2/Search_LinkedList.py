class Node:
    def __init__(self,dataval):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None


    def listprint(self,data):
        printval = self.headval
        while printval is not None:
            if printval.dataval == data:
                return True
            return False
            printval = printval.nextval

s1 = SLinkedList()
l=[20,30,40]
heed = Node(10)
s1.headval = heed
current = heed
for i in l :
    current.nextval = Node(i)
    current = current.nextval
z = s1.listprint(100)
if (z):
    print("Data found")
else:
    print("Data not Found")