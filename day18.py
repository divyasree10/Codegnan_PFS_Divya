#lambda function()--->also called anonymous function
#this can take n no.of arguments but they have one expression
#syntax-lambda(keyword) arguments:expression
'''
num=lambda num_2:num_2+10
print(num(6))

num_1=lambda a,b,c:(b-a)*c
print(num_1(4,9,2))                  #(9-4)*2

num_3=lambda d,e: d-e
print(num_3(16,9))

num_4=lambda f,g:f*g
print(num_4(3,4))

num_5=lambda h,i:h/i
print(num_5(6,3))
'''
#list comprehension--->offers the shorter syntax when you want to create a new list from the existing list
#syntax-variable_name=[[expression loop and condition]
'''
old_list=[11,42,35,44,50]
new_list=[j for j in old_list]
print(new_list)
'''
old_list=[11,42,35,44,50]
new_list=[j for j in old_list if j%2==0]  #prints even numbers
print(new_list)


