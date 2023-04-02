'''
given two lists, both having integer elements, write a python program using python lists to create and
return a new list as per the rule given below: If the double of an element in list1 is present in list2, then add it to the new list.

Estimated Time: 20 minutes

Sample Input

list1 [11,8,23,7,25,15] - list2 [6,33,50,31,46,78,16,34] -

Expected Output

new_list [8,23,25]
'''

class Node:
    def __init__(self,dataval= None):
        self.dataval = dataval
        self.nextval = None

class SLinkdedList:
    def __init__(self):
        self.head = None

    def Traverse(self):
        a = self.head
        while a is not None:
            print(a.dataval)
            a = a.nextval

def listthree(s1,s2):
    l3=[]
    a1 = s1.head
    a2 = s2.head
    for i in a1:
        for j in a2:
            if a1.dataval*2 == j:
                l3.append(i)
    print(l3)




s1 = SLinkdedList()
s2 = SLinkdedList()
l1 = [8,23,7,25,15]
l2 = [33,50,31,46,78,16,34]

n1 = Node(11)
s1.head = n1
for i in l1:
    n1.nextval = Node(i)
    n1=n1.nextval

n2 = Node(6)
s2.head = n2
for i in l2:
    n2.nextval = Node(i)
    n2=n2.nextval
s1.Traverse()
print("Second Node")
s2.Traverse()
listthree(s1,s2)




