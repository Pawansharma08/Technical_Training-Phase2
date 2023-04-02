'''A train is identified by its name and list of compartments.
The compartments are identified by its name,total seating
capacity and the number of passengers.
Implement the class Train as given in the class diagram.
Train
- train_name
- compartment_list
init(train_name,compartment_list)
+ get_train_name()
+ get_compartment_list()
+ count_compartments ()
+ check_vacancy()
Write a python program to implement the following:
count_compartments()- returns the total number of compartments
 in the train
check_vacancy()-returns the count of the compartments in which
 more than 50% of the seats are vacant
Note : Compartment list is maintained as a linked list where
data in each node refers to a compartment.

compartment1=Compartment("SL",250,400)
compartment2=Compartment("2AC",125,280)
compartment3=Compartment("3AC",120,300)
compartment4=Compartment("FC",160,300)
compartment5=Compartment("1AC",100,210)
'''

class Node:
    def __init__(self, Compartment_name, no_of_setting, total_person):
        self.Compartment_name = Compartment_name
        self.no_of_setting = no_of_setting
        self.total_person = total_person
        self.next= None


    def get_next(self):
        return self.next

    def get_Compartment_name(self):
        return self.Compartment_name

    def get_no_of_setting(self):
        return self.no_of_setting

    def get_total_person(self):
        return self.total_person




class Train:
    def __init__(self,train_name,Compartment_list):
        self.train_name = train_name
        self.Compartment_list = Compartment_list

    def get_Train_name(self,train_name):
        return self.train_name

    def get_Compartment_list(self,Compartment_list):
        return Compartment_list

    def count_compartment(self):
        a =0
        p = self.Compartment_list.get_head()
        while p is not None:
            a+=1
            p = p.get_next()
        return a

    def check_vacancy(self):
        c=0
        p = self.Compartment_list.get_head()
        while p is not None:
            if(p.no_of_setting < p.total_person//2):
                c+=1
            p = p.next
        return c




class Compartment:
    def __init__(self):
        self.head = None

    def get_head(self):
        return self.head

    def print_comptartent(self):
        a = self.head
        while a is not None:
            print(a.Compartment_name,a.no_of_setting,a.total_person)
            l.append(a.Compartment_name)
            a = a.next

    def remove_compartment(self,pos):
        prv = self.head
        a = self.head.next
        for i in range(0,pos-1):
            a = a.__next
            prv = prv.__next

        prv.__next = a.__next
        a.__next = None


l=[]
n1 = Node("SL",250,400)
n2 = Node("2AC",125,280)
n3 = Node("3AC",120,300)
n4 = Node("FC",160,300)
s1 = Compartment()
s1.head = n1
n1.next = n2
n2.next = n3
n3.next = n4
s1.print_comptartent()
print(l)
t1 = Train("Raj",s1)
print("No of Compartment")
print(t1.count_compartment())
vac_count=t1.check_vacancy()
print("Vacancy :",vac_count)
















