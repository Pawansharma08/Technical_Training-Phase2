'''
Given a stack of integers, write a python program that updates the input stack such that all occurrences of the smallest values are at the bottom of the stack, while the order of the other elements remains the same.

KEEP SII

For example:

Input stack (top-bottom): 5 66 5 8 7
 Output: 66 8 7 5 5
'''

class stack:
    def __init__(self,max_size):
        self.__max_size = max_size
        self.__top = -1
        self.__element = [None]*max_size

    def is_empty(self):
        if self.__top == -1:
            return True
        return False

    def is_full(self):
        if self.__top == self.__max_size-1:
            return True
        return False

    def push(self,data):
        if (self.is_full()):
            print("Stack is Full")
        else:
            self.__top += 1
            self.__element[self.__top] = data


    def display(self):
        l=[]
        if(self.is_empty()):
            print("List is empty")
        else:
            index = (self.__top)
            while(index>=0):
                print(self.__element[index])
                l.append(self.__element[index])
                index-=1
        return l


def put_in_last(l):
    a = min(l)
    c = l.count(a)
    for i in range(c):
        l.remove(a)
        l.append(a)
    return l

l=[]
s1 = stack(5)
s1.push(7)
s1.push(8)
s1.push(5)
s1.push(66)
s1.push(5)
l=s1.display()
print(put_in_last(l))


