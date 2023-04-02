'''
Write a python program to remove all duplicate elements from a sorted linked list containing integer data. Use the LinkedList class and methods in it to implement the above program.

Example:

Input LinkedList: 10 10 20 20 30 30 30 40 50

Output LinkedList: 10 20 30 40 50
'''


class Node:
    def __init__(self,data = None):
        self.data = data
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None

    def listprint(self):
        a = self.head
        while a is not None:
            print(a.data)
            a = a.next

    def remove_duplicates(self):

        ptr1 = None
        ptr2 = None
        dup = None
        ptr1 = self.head

        while (ptr1 != None and ptr1.next != None):

            ptr2 = ptr1
            while (ptr2.next != None):
                if (ptr1.data == ptr2.next.data):
                    dup = ptr2.next
                    ptr2.next = ptr2.next.next
                else:
                    ptr2 = ptr2.next

            ptr1 = ptr1.next



s1 = SLinkedList()
l = [10,10,20,20,20,30,30,30,40,50]
z=[]
heed = Node(10)
s1.head = heed
current = heed
for i in l :
    current.next = Node(i)
    current = current.next
s1.remove_duplicates()
s1.listprint()




