'''
num=int(input("enter a number: "))            #number is prime or not
count=0
for j in range(1,num+1):
    if num%j==0:
        count+=1
if count==2:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")
'''
'''
for num in range(2,11):         #prints the number and if it is prime or not
    count=0
    for j in range(1,num+1):    #(1,3) (1,4) (1,5) . . . . (1,12)
        if num%j==0:
            count+=1
    if count==2:
        print(f"{num} is a prime")
    else:
        print(f"{num} is not a prime")
'''
'''
lst=[1057,197,9,86,17673]           #elements in a list are prime or not
for an in lst:
    print(an)
    count=0
    for j in range(1,an+1):    
        if an%j==0:
            count+=1
    if count==2:
        print(f"{an} is a prime")
    else:
        print(f"{an} is not a prime")
'''
'''
any=[2,356,8,6,3,2,8]      #remove the duplicates 
empty=[]                   #here we take an empty list and push the elements that are not already present in it 
for j in any:
    if j not in empty:
        empty.append(j)
        print(empty)
'''
num=153
length=len(str(num))
amstr=0
for j in str(num):
    amstr+=int(j)**length
    print(amstr)
if amstr==num:
    print(f"{num}is a amstrong num")
else:
    print(f"{num} is not a amstrong num")








