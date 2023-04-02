'''Write a python function which accepts two linked lists containing integer data and an integer ,n merges the two linked
lists, such that list2 is merged with list1 after n number of nodes.
Assume that value of n will always be less than or equal to the number of nodes in list 1

Sample Input                       Expected Output
list1                              1->2->4->3->5
list2                              9->8->11
n - 2                              1->2->9->8->11->4->3->5
'''


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        c=0
        a = self.head
        while a is not None:
            if a.data == 9999:
                a = a.next
                pass
            else:
                print(a.data, "->", end='')
                c += 1
                a = a.next
        return c

def merge(s1,s2,n):
    s3 = SLinkedList()
    n3 = Node(9999)
    s3.head = n3
    c=n3
    a =s1.head
    n1=0
    f=0
    b=s2.head
    while a is not None:
        if n1 < n:
            c.next = Node(a.data)
            c = c.next
            a = a.next
        n1+=1
        if f==0 and n==n1:
            while b is not None:
                c.next = Node(b.data)
                c = c.next
                b = b.next
                f=1
                n1=n1-2*n
    print()
    s3.traverse()



s1 = SLinkedList()
l1=[2,4,3,5]
heed = Node(1)
s1.head = heed
current1 = heed
for i in l1 :
    current1.next = Node(i)
    current1 = current1.next
n1=s1.traverse()
print()
s2 = SLinkedList()
l2=[8,11]
heed = Node(9)
s2.head = heed
current2 = heed
for i in l2 :
    current2.next = Node(i)
    current2 = current2.next
n2=s2.traverse()
merge(s1,s2,2)




