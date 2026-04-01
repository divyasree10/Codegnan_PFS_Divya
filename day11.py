'''
num=int(input("enter a number: "))                          #print a table
for j in range(1,11):
    print(f"{num} X {j}={num*j}")
'''
#refer notes for string methods
'''
str=("He is a VolleyBall player")         #no.of capital and small letters
count_1=0
count_2=0
for ch in str:
    if ch.isupper():
        count_1+=1
    elif ch.islower():
        count_2+=1
print(f"there are total {count_1} capital letters")
print(f"there are total {count_2} small letters")
'''
'''
str=("I am learning PYTHON Programming")        #using append method
cap_L=[]
small_L=[]
for ch in str:
    if ch.isupper():
        cap_L.append(ch)
    elif ch.islower():
        small_L.append(ch)
print(f"{cap_L} contains all capital letters")
print(f"{small_L} contains all small letters")
'''
'''
user_acc_details={"Name":"Divya","ATM pin":"2110"}         #ATM pin
print("welcome to Union Bank ATM")
print("please insert your card")
pin=input("enter your 4-digit pin: ")
if len(pin)==4:
    if pin in user_acc_details['ATM pin']:
        print("correct pin")
    else:
        print("you have entered invalid pin")
else:
    print("check and enter your 4-digit pin")
'''
#perfect number--->sum of the factors is equal to the number
num=int(input("enter a number: "))
fact=0
for i in range(1,num):
    if num%i==0:
        fact+=i
if fact==num:
    print(f"{num} is a perfect number")
else:
    print(f"{num} is not a perfect number")










































