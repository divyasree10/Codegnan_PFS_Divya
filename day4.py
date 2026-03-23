#conditions
#statements are of 3 types-control,conditional(decision-making),loop
'''
if statement
if-else statement
if-elif-else statement

if statement--->this(if stetment)is used to check any condition,if the condition
becomes true then it will enter inside the if statement'''
'''
age=int(input("enter your age: "))
if age>=18:
    print("your age is 18 or above")
'''
'''student_att=int(input("enter student attendance: "))
if student_att>75:
    print("you can sit in the exam")
'''
'''
total_bill=int(input("enter total bill amount: "))
if total_bill<5000:
               print("not eligible for discount")
'''
#if-else statement---> else part is called as fall-back statement.it only executes when if statement is false
'''
age=int(input("enter your age: "))
if age>=18:
    print("you can vote")
else:
    print(f"you cannot vote and have to wait {18-age} years")
'''
'''
total_amount=int(input("enter total amount: "))
if total_amount>=149:
    print("you get free delivery")
else:
    print(f"you get free delivery if you add {149-total_amount} to your cart")
'''
'''
marks=int(input("enter your marks: "))
if marks>=50:
    print("pass")
else:
    print(f"you would have passed if you got {50-marks} more")
'''
#if-elif-else statement--->in the elif part, i can check one more condition
'''
marks=int(input("enter your marks: "))
if marks>80:
    print("A grade")
elif marks<=80 and marks>=50:
    print("B grade")
elif marks<50 and marks>=30:
    print("C grade")
else:
    print("fail")
'''
#build your own calculator
'''
operator=input("enter the operator: ")
op1=int(input("enter the first operand: "))
op2=int(input("enter the second operand: "))
if operator=="+":
    print("the sum is: ",op1+op2)
elif operator=="-":
    print("the difference is: ",op1-op2)
elif operator=="*":
    print("the product is: ",op1*op2)
else:
    print("the quotient is: ",op1/op2)
'''
#traditional way
'''operator=int(input("enter the operator: \n1.Add \n2.Sub \n3.Mul \n"))
op1=int(input("enter the first operand: "))
op2=int(input("enter the second operand: "))
if operator == 1:
    print(op1+op2)
elif operator == 2:
    print(op1-op2)
elif operator == 3:
    print(op1*op2)
else:
    print(op1/op2)'''
num=int(input("enter a number: "))
if num>0:
    print("positive")
elif num<0:
    print("negative")
else:
    print("zero")



















