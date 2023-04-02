class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        max1=0
        a = self.head
        while a is not None:
            if max1 < a.data:
                max1 = a.data
            print(a.data,end=' ')
            a =a.next
        print()
        print("Max is :",max1)
        return max1

    def replace(self,data,max1):
        a = self.head
        while a is not None:
            if a.data == max1:
                a.data = data
            a = a.next



s1 = SLinkedList()
l1=[11,18,111,100]
heed = Node(1)
s1.head = heed
current1 = heed
for i in l1 :
    current1.next = Node(i)
    current1 = current1.next
max1=s1.traverse()
s1.replace(20,max1)
s1.traverse()