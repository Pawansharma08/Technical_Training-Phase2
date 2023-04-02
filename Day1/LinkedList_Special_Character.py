'''
Given a linked list of characters. Write a python function to return a new string that is created by appending all the
characters given in the linked list as per the rules given below.
Rules:
Replace '*' or '/' by a single space
In case of two consecutive occurrences of '*' or '/', replace
those two occurrences by a single space and convert
the next character to upper case
Assume that
There will not be more than two consecutive occurrences of '*' or "/".
The linked list will always end with an alphabet
Sample Input
A,n,*,/,a,p,p,l,e,*,a,/,day,*,*,k,e,e,p,s,/,*,a,/,/,d,o,c,t,o,
r,*,A,w,a,y

expected output:
An apple a day Keeps a Docter Away
'''

class Node:
    def __init__(self,dataval):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

    def travers(self):
        res=""
        if self.headval is None:
             print("Empty")
        else:
            pre = self.headval
            c=0
            while pre is not None:
                if pre.dataval in ['*','/']:
                    if c==0:
                        res+=" "
                        c=1
                    if (pre.nextval.dataval == "*" and pre.dataval == "*") or (pre.nextval.dataval == '/' and pre.dataval == '/'):
                        pre= pre.nextval
                        res+=pre.nextval.dataval.upper()
                        pre= pre.nextval

                    else:
                        pre = pre.nextval
                else:
                    c=0
                    res=res+pre.dataval
                pre= pre.nextval
        return res

s1 = SLinkedList()
l=['n','*','/','a','p','p','l','e','*','a','/','day','*','*','k','e','e','p','s','/','*','a','/','/','d','o','c','t','o','r','*','A','w','a','y']
heed = Node('A')
s1.headval = heed
current = heed
for i in l :
    current.nextval = Node(i)
    current = current.nextval
p=s1.travers()
print(p)