class Queue:
    def __init__(self,max_size):
        self.__max_size = max_size
        self.__front = 0
        self.__rare = -1
        self.__element = [None]*max_size

    def is_empty(self):
        if self.__rare < self.__front:
            return True
        return False

    def is_full(self):
        if (self.__rare == self.__max_size-1):
            return True
        return False

    def eneque(self,data):
        if (self.is_full()):
            print("Queue is full")
        else:
            self.__rare+=1
            self.__element[self.__rare]=data

    def deque(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            data= self.__element[self.__front]
            self.__front+=1
            return data

    def display(self):
        for i in range (self.__front,self.__rare+1):
            print(self.__element[i])

    def max_size(self):
        return self.__max_size


queue = Queue(4)
print("Is queue is empty",queue.is_empty())
queue.eneque(100)
print("is queue is empty",queue.is_empty())
queue.eneque(200)
queue.eneque(300)
queue.display()
queue.eneque(400)
queue.eneque(500)
queue.eneque(600)
queue.display()
queue.deque()
print("After deleting the first element")
queue.display()
