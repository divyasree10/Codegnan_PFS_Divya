#constructor(__init__)--->A constructor is a special method used to initialize the object data i.e; __init__
'''
class shopping:
    def __init__(self,store,garment):
        self.store=store
        self.garment=garment
    def display(self):
        print(self.store,self.garment)
shop_1=shopping("Ajio","jean")
shop_1.display()
'''
#Access specifiers--->public,protected,private
#1.public:syntax-name
#we can use it anywhere in the program
#2.protected:syntax-_name
#only for internal use
#3.private:syntax-__name
#this one is restricted

#self-->this keyword is instance variable and unique for each object
'''
class some:
    def __init__(self):
        self.public="public"
        self.protected="protected"
        self.private="private"
any=some()
print(any.public)
print(any._protected)
print(any.__private)
'''




























