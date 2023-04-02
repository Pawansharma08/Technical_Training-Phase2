class Queue:
    def __init__(self,max_size):
        self.max_size = max_size
        self.rare = -1
        self.front = 0
        self.element = [None]*max_size

    def details(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def is_empty(self):
        if self.rare < self.front:
            return True
        return False

    def is_full(self):
        if self.rare == self.max_size-1:
            return True
        return False

    def enque(self,data):
        if (self.is_full()):
            print("Queue is full")
        else:
            self.rare += 1
            self.element[self.rare] = data


    def display(self):
        for i in range(self.front,self.rare):
            print(self.element[i])

    def specific_gender(self,gender):
        for i in range(self.front,self.rare):
            if self.element[i][2] == gender:
                print(self.element[i])



q1 = Queue(6)
q1.enque(["pawan",20,"Male"])
q1.enque(["Rupesh",20,"Male"])
q1.enque(["Pinaki",20,"Female"])
q1.enque(["Arshad",20,"Male"])
q1.enque(["Sonu",20,"Female"])
q1.specific_gender("Male")