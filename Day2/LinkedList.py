class Node:
    def __init__(self,dataval = None):
        self.dataval = dataval
        self.nextval = None


class SLinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval


    def AtStart(self,newdata):
        NewNode = Node(newdata)
        NewNode.nextval = self.headval
        self.headval = NewNode

    def AtEnd(self,newData):
        NewNode = Node(newData)
        if self.headval is None:
            self.headval = NewNode
            return
        laste = self.headval
        while(laste.nextval):
            laste = laste.nextval
        laste.nextval = NewNode

    def atMiddle(self,middleNode,Newdata):
        NewNode = Node(Newdata)
        a = self.headval
        for i in range (1,middleNode-1):
            a = a.nextval

        NewNode.nextval = a.nextval
        a.nextval = NewNode

    def del_starting(self):
        a = self.headval
        self.headval = a.nextval
        a.nextval = None


    def del_AtEnd(self):
        pre = self.headval
        a = self.headval.nextval
        while a.nextval is not None:
            a = a.nextval
            pre = pre.nextval

        pre.nextval = None

    def del_AtSpecific(self,pos):
        prv = self.headval
        a= self.headval.nextval
        for i in range (1,pos-1):
            a = a.nextval
            prv = prv.nextval

        prv.nextval = a.nextval
        a.nextval = None

list = SLinkedList()
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
list.headval.nextval = e2
e2.nextval = e3
list.AtStart("Days")
list.AtEnd("Fri")
list.atMiddle(5,"Thu")
list.del_starting()
list.del_AtEnd()
list.del_AtSpecific(2)
list.listprint()
