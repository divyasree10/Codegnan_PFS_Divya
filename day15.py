#ways to pass arguements in calling function
#1.required arguements-
#it should match same number variables in calling with def
'''
num=8
numb=9
def add(num,numb):
    print(num+numb)
add(num,numb)
'''
#2.default arguements-
#it takes the default values from the arguements
'''
name="divya"
def add(name):
    print(name)
add(name="sree")        #here sree overwrites divya
add(name="priya")       #priya is also printed cause the function is called the 2nd time
'''
'''
num=7
count=0
def prime(num,count):
    print(num,count)
    for j in range(1,num+1):
        if num%j==0:
            count+=1
    if count==2:
        print("prime")
    else:
        print("not")
prime(num,count)        #prime
prime(num=12,count=0)   #not
'''
#4.variable length arguement-
#adding a star(*) before the parameter name in function,receive a tuple of arguements and can access items with indices
'''
def name(*student):       #*-->assigning values in the form of tuple
    print(student)
name("divya","sree","priya")
'''
def name(*student):       
    print(student[2])              #accessing using index
name("divya","sree","priya")
























