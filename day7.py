'''
list_p=[1,2,4,["Divya","Sree",["Python","Flowers"]],5,7,89]
print(list_p)
print(list_p[3])
print(list_p[3][2])
print(list_p[3][2][1])

concatenation---this is noting but a (+)
case1---intergers---this will act as addition for integers
print(9+8)
case2---for other datatypes(we have use same datatypes str or list)---this will act as cancatenations means joins the 2 string
print("Divya"+"Sree")
print([1,2]+[3,4])

print([1,2]+"Divya")  #can only concatenate list (not "str") to list
print("Divya"+[1,2])  #can only concatenate str (not "list") to str
note:concatenation can't access 2 different type of data types(str-str,list-list)


tuple()---it is collection of different dayatypes,this is represented by (), seperated by (,)
thing=(1,2,"Divya",[3,4],(5,6))
print(thing)

eg1=(12,89,"Python",(23,"Divya",[67,"Python is a language",(7,8)],[8,("python",[34,9])]))
print(eg1)
print(eg1[3])
print(eg1[3][2])
print(eg1[3][2][1][9])
'''

leap_year=int(input("Enter year:"))
if (leap_year%4==0 and leap_year%100!=0)or leap_year%400==0:
    print(f"{leap_year} is a leap year")
else:
    print(f"{leap_year} is not a leap year")
