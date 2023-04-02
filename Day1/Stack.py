class stack:
    def __init__(self,max_size):
        self.__max_size = max_size
        self.__top = -1
        self.__element = [None]*max_size

    def is_empty(self):
        if(self.__top == -1):
            return True
        return False

    def stack_full(self):
        if(self.__top == self.__max_size-1):
            return True
        return False

    def push(self,data):
        if(self.stack_full()):
            print("Stack is full")
        else:
            self.__top += 1
            self.__element[self.__top] = data

    def pop(self):
        if(self.is_empty()):
            print("Stack is empty")
        else:
            data = self.__element[self.__top]
            self.__top-=1
            return data

    def display(self):
        if(self.is_empty()):
            print("List is empty")
        else:
            index = (self.__top)
            while(index>=0):
                print(self.__element[index])
                index-=1

    def get_max_size(self):
        return self.__max_size



ball_stack = stack(4)
print("is it is empty",ball_stack.is_empty())
ball_stack.push(5)
print("after adding 1 element")
print("is it is empty",ball_stack.is_empty())
ball_stack.push(6)
ball_stack.push(7)
ball_stack.push(8)
ball_stack.display()
print("Size of the stack",ball_stack.get_max_size())
print("the element is deleted",ball_stack.pop())
ball_stack.display()
