'''
varaibles-->variable is basically a named storage location that is used to hold the
data in the memory, to make it simple it is the label which points
out to a value-->storage placeholders

rules for defining variables
-->A-Z, a-z, 0-9
-->start with uppercase, lowercase letters, even with a underscore
-->but cannot start with symbols(@,#,$,....) and numbers

the better preferable way is to go with general purpose terms(ex-name, email_id, account_num)
'''

a=1
b=5
#a,b are called literals and 1,5 are called values
a=25
#pytyhon is dynamically typed, you need not define the datatype and also
#only the recent value to the variable with same name is pointed
print(a)
print(b)
#@sre=88  #syntax error
#$gsd=70  #invalid syntax

#store your personal details
name="codegnan"
location="visakhapatnam"
age=7
email_id="cmo@codegnan.com"
print(name,location,age,email_id)

#how to assign multiple values to a variable
akash, praneeth, ajay=21, 20, 23
print(akash)
print(praneeth)
print(ajay)
#assign same values to multiple variables
x=y=z=21
print(x, y, z)

#keywords are reserved words which will have specific usage
#there are 35 keywords in python
#never use keywords as identifiers (ex- if=42 gives invalid syntax)
#python is case sensistive (if cannot be used as an identifier but If can be used)
#identifiers are names given to variables,functions,classes,objects,...
#literals are fixed valures to a identifier
age=25
name='saketh'
#name is identifier and 25 is literal
#single line comments uses # and multi lines comments uses ''' ___ '''

#Built-in Datatypes-->numeric,boolean and collections
#numeric datatypes-->int,float,complex
#int-->count,values,quantities
#float-->temperature,percentage
#complex-->specific conversions(real and imaginary)
#implicit as python follows dynamic type

count=40
print(count)
print(type(count))

price=175.25
print(price)
print(type(price))

value=3+4j
print(value)
print(type(value))

j3=25
value=2+j3  #not a complex num because it can start with a variable
print(value)
print(type(value))

#Typecasting--->converting one datatype to another
#int-->float,complex

age=25
print(age)
print(type(age))

b=float(age)
print(b)
print(type(b))
c=complex(age)
print(c)
print(type(c))

#float-->int,complex
value=32.5
print(value)
print(type(value))
value2=complex(value)
print(value2)
print(type(value2))
value3=int(value)
print(value3)
print(type(value3))

'''#complex-->int         #not possible
val=3+5j
print(val)
val1=int(val)
print(val1)
val2=float(val)
print(val2)'''

#Boolean Datatype-->validation-->True/False
a=True
print(a)
print(type(a))

#Typeconveresion of bool
b=int(a)
print(b)
c=float(a)
print(c)
d=complex(float(int(False)))
print(d)
print(type(d))

num=25+True+3
print(num)
print(type(num))

#input-->input()/output-->print()
a=5
print(a)

a = input("enter a value") #any input but result as str
print(a)
print(type(a))

a = int(input("enter a value:")) #only integer input
print(a)
print(type(a))

b = float ( input ("enter another value"))
print(b)
print(type(b))

#now cse study
#details of the student
name=input("enter the student name:")
print("--------")
admission_fees=int(input("enter admission fees:"))
tuition_fees=float(input("enter tuition fees:"))
hostel_fees=float(input("enter hostel_fees:"))
#calc the total fee
total_fees=admission_fees+tuition_fees+hostel_fees
print("--------------")
print("student name: ",name)
print("admission fee: ",admission_fees)
print("tuition fee: ",tuition_fees)
print("hostel fee: ",hostel_fees)
print("total fee: ",total_fees)
print("---------------")























