#encapsulation-->the principal of binding data(attributes) and methods that
#operate on that data into a single unit,which is a class
'''
class Bank:
    def __init__(self,balance):
        self.__balance=balance
    def deposite(self,amount):
        self.__balance+=amount
    def get_balance(self):
        return self.__balance
acc=Bank(15000)
acc.deposite(17000)
print(acc.get_balance())
'''
#inheritance-->allows a child class(Subclass) to aquire the attributes and methods of a parent class(base class)
#1.single inheritance-using single method of the class from base class
#super()-->used to call methods of the parent class from the child class
'''
class parent:
    def display(self):
        print("this is parent method")
class child(parent):
    def display(self):
        super().display()
        print("this is child method")
obj=child()
obj.display()
'''
#2.multiple inheritance-a child class inherits from more than one parent class
'''
class father:
    def skill_1(self):
        print("father:hard working")
class mother:
    def skill_2(self):
        print("mother :cooking")
class child(father,mother):
    def skills(self):
        print("child:coding")
some=child()
some.skill_1()
some.skill_2()
some.skills()
'''























