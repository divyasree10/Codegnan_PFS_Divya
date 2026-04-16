#OOPs--->classes,objects,attributes,methods
#Object Oriented Programming is a style of programming where we model real-world things
#as objects that contain both data and functions()
#why oops? reusability of code,scalability,easy maintenance 
#class--->template or blueprint that defines what kind of data and behavior a certain type of object will have
#object--->instance of class or an object is a real instance created from a class.It is the actual thing that exists in
#memory while the program runs
#attributes--->variables that store data related to class or object
'''
class car:  #class
    pass
car1=car()  #object
car2=car()  #object
'''
'''
class dog:                              #dog=class
    def __init__(self,breed,colour):    #breed,colour=attributes
        self.breed=breed                
        self.colour=colour
dog_1=dog("saint bernard","brown")       #dog_1,dog_2=objects
dog_2=dog("german shepard","cream")
print(dog_1.breed)
'''
'''
class school:
    def __init__(self,student,teacher,subject):
        self.student=student
        self.teacher=teacher
        self.subject=subject
school_1=school("divya","priya","math")
school_2=school("sree","vardhan","science")
print(school_1.student)
print(school_2.teacher)
'''
'''
class fruits:
    def __init__(self,name,colour):
        self.name=name
        self.colour=colour
fruits_1=fruits("watermelon","red")
fruits_2=fruits("pineapple","yellow")
print(fruits_2.colour)
'''
'''
class games:
    def __init__(self,name,players):
        self.name=name
        self.players=players
games_1=games("badminton","2")
games_2=games("cricket","11")
print(games_1.name)
'''
'''
class mobile:
    def __init__(self,company,model):
        self.company=company
        self.model=model
mobile_1=mobile("samsung","z fold")
mobile_2=mobile("google","pixel")
print(mobile_1.company)
'''
class shopping:
    def __init__(self,store,garment):
        self.store=store
        self.garment=garment
shopping_1=shopping("myntra","jean")
shopping_2=shopping("ajio","kurti")
print(shopping_2.store)

























































































































































