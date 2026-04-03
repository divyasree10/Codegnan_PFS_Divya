#print a pattern
'''
num=int(input("enter the limit: "))
for j in range(num):
    for i in range(1,j):
        print(i,end="")
    print() 
'''
'''
num=4   #print a square pattern
for j in range(num):
    for i in range(num):
        print("*",end="")
    print()
'''
'''
num=int(input("enter the limit: "))#reverse triangle pattern
for j in range(num):
    for i in range(num-j):
        print("*",end="")
    print()
'''
'''
num=int(input("enter the limit: "))     #print a triangle
for j in range(num):
    print(" "*(num-j),end="")
    for i in range(j+1):
        print("*",end=" ")
    print()
'''
user_acc_details={"Name":"Divya","ATM pin":"2110","Balance":70000}         #ATM pin
print("welcome to Union Bank ATM")
print("please insert your card")
pin=input("enter your 4-digit pin: ")
if len(pin)==4:
    if pin in user_acc_details['ATM pin']:
        user_choice=int(input("enter \n 1.Withdraw: "))
        if user_choice==1:
            money_w=int(input("enter the amount you want to withdraw: "))
            if money_w<=user_acc_details['Balance']:
                user_acc_details['Balance']-=money_w
                print(user_acc_details['Balance'])
            else:
                print("insuficient balance")
    else:
        print("you have entered invalid pin")
else:
    print("check and enter your 4-digit pin")






