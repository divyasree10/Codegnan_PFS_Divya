#Break--->this is used to exit from the loop when we found the required element value.
'''
for j in range(1,10):
    print(j)
    if j==5:
        break
'''
'''
list1=[1,2,3,4]
for n in list1:
    print(n)
    if n==3:
        break
'''
#continue--->used to skip that particular loop
'''
for j in range(1,10):
    if j==5:                  #this doesn't work for j==5 and j==8 like conditions
        continue
    print(j)
'''
'''
list1=[1,21,43,64]
for n in list1:
    if n==43:
        continue
    print(n)
'''
#pass--->this is called as spaceholder. it is used incase any statement like if, for loop, elif, else,...
#this should be complete, or it throws syntax error. to avoid this we use pass.
'''
for j in range(1,10):
    pass
'''
#else-for--->falls back to else block, when all loops are completed
'''
for m in range(1,10):
    print(m)
else:
    print("else block")
'''
#while loop--->combination of if and for
#if the loop is not ended properly, it will run upto memory space  becomes empty.
'''
num=1
while num<5:
    print(num)     #if the code stops here, output gives unlimited 1's
    num+=1
'''

req_num=int(input("enter the limit: "))                #fibonacci series
num1=0
num2=1
print(num1,num2,end=" ")
for v in range(req_num+1):
    num3=num1+num2
    num1=num2
    num2=num3
    print(num3,end=" ")
'''

n = int(input())
a, b = 0, 1
for _ in range(n):
    print(a, end=' ')
    a, b = b, a + b
'''

























