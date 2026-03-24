'''string--->sequence/collection of characters which represented by "" or ''
and we can access the string using indexing i.e;position '''
'''
str='python program'
print(str)
print(str[7])
'''
#finding the position
# print(str[7,8,9])  #gives error-at a time only one character position can be found
''''slicing--->dividing the string according to the requirements'''
'''
str='python program'
print(str[7:13])  #13-upto 12 positions i.e;(12+1)
print(str.replace("python","java"))
print(str)   #change does not happen in the string 
'''
'''
str='python program'
so=str.replace("python","java")
print(str)
print(so)  #change does not happen in the string 
print(so[-5])    #string allows negaive index but from the end
#print(so[1000])    #error--->string index out of range
'''
'''
data="i am divya , i am currently learning PFS at Codegnan,Visakhapatnam"
print(f"my name is {data[5:10]}")
print(f"location is {data[-13: ]}")
print(data[ : :-1])  #reversing the string
print(len(data))    #length of a string
'''
'''
data="123"
print(type(data))
print(len(data))
'''
#we can only convert string to integer if and only if it contains only integers
'''some="123p"
num=int(some)
print(type(some)) #error '''
'''methods of string:'''
#split()-remove space and the output is in the list[] and it will give seperated thing in each index
#syntax--->varaible_name.split("substring")
'''
str="python is a programming language"
print(str.split(" "))
print(str.split("programming"))     #splits at the word programming
'''
#lower()-convert all letters into lower case
#syntax--->variable_name.lower()
#upper()-convert all letters into upper case
#syntax--->variable_namme.upper()
'''
str="pYThon iS A proGramming LANGuage"
print(str.lower())
print(str.upper())
'''
#replace()-replace old string with a new string
#syntax--->varaible_name.replace("old string","new string")
'''
str="python is a programming language"
print(str.replace("python","java"))
'''
#check if the string contains "python"
str="python is a programming language"
if "python" in str:
    print("yes")
else:
    print("no")













































