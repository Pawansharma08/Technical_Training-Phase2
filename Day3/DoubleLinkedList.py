class Node:
    def __init__(self,data):
        self.prev = None
        self.data = data
        self.next = None

class DLinkedList:
    def __init__(self):
        self.head = None

    def is_Empty(self):
        if self.head is None:
            return True
        return False

    def insertAt_Start(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode

    def insertAt_End(self,data):
        newNode = Node(data)
        if self.is_Empty():
            self.insertAt_Start(data)
        else:
            a = self.head
            while a.next is not None:
                a = a.next
            a.next = newNode
            newNode.prev = a


    def insertAt_Middle(self,pos,data):
        newNode = Node(data)
        if self.is_Empty():
            self.insertAt_Start(data)
        elif self.head.next is None:
            self.insertAt_End(data)
        else:
            a = self.head
            for i in range(0,pos-1):
                a = a.next
            newNode.prev = a
            newNode.next = a.next
            a.next.prev = newNode
            a.next = newNode


    def del_AtStart(self):
        a = self.head
        self.head = a.next
        a.next.prev = None

    def del_AtEnd(self):
        a = self.head
        while a.next is not None:
            a = a.next
        a.prev.next = None


    def del_AtAny(self,pos):
        a = self.head
        if pos == 0:
            self.del_AtStart()
        elif(a.next is not None):
            self.del_AtEnd()
        else:
            for i in range(0, pos - 1):
                a = a.next
            a.next = a.next.next
            a.next.prev = a.next

    def printLinkedList(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next

x = DLinkedList()
print(x.is_Empty())
n1 = Node(10)
x.head = n1
n2 = Node(20)
n1.next = n2
n2.prev = n1
n3 = Node(30)
n2.next = n3
n4 = Node(40)
n3.prev = n2
n3.next= n4
n4.prev = n3
x.insertAt_Start(50)
x.insertAt_End(60)
x.insertAt_Middle(2,15)
x.del_AtStart()
x.del_AtEnd()
x.del_AtAny(4)
x.printLinkedList()