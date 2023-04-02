'''
A teacher has given a project assignment to a class of KEEP SILENCE Students.
She wants to store the marks (out of 100) scored by each student. The marks scored are as mentioned below: 89,78,99,76,77,67,99,98,90
Write a python program to store the marks in a list and perform the following:

1. The teacher forgot to include the marks of one student. Insert 78 at index position, 8 and display the marks of all 10 students.
2. The teacher also wants to know the marks scored by students represented by index positions, 5 and 7.

Identify and display the two marks.
'''

class Node:
    def __init__(self,dataval):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

    def traverse(self):
        a = self.headval
        while a is not  None:
            print(a.dataval)
            a = a.nextval

    def insert_At_mid(self,pos,newdata):
        newNode = Node(newdata)
        a = self.headval
        for i in range(0,pos-1):
            a = a.nextval
        newNode.nextval = a.nextval
        a.nextval = newNode

    def show_between(self,start,end):
        c=0
        a= self.headval
        for i in range(0,start):
            a = a.nextval
            c+=1
        for i in range(c-1,end):
            print(a.dataval)
            a=a.nextval

l = [78,99,76,77,67,99,98,90]
s1 = SLinkedList()
heed = Node(89)
s1.headval = heed
current = heed
for i in l :
    current.nextval = Node(i)
    current = current.nextval
print("Student Between 5 to 7")
s1.show_between(4,6)
s1.traverse()
print("Insert At Position 8")
s1.insert_At_mid(7,78)
s1.traverse()
