#if the letter is vowel or consonant
'''
letter=input("enter a letter: ")
if letter=="a":
    print("vowel")
elif letter=="e":
        print("vowel")
elif letter=="i":
        print("vowel")
elif letter=="o":
        print("vowel")
elif letter=="u":
        print("vowel")
else:
    print("consonant")
'''
'''
letter=input("enter a letter: ")
if letter in "AEIOUaeiou":
    print("vowel")
else:
    print("consonant")
'''
#convert 24hr clock into 12hr clock
'''
time=input("enter time in 24hr clock: ")
part=time.split(":")        #using split method
print(part)
hours=int(part[0])
mins=int(part[1])
print(hours)
print(mins)
if hours>=13 and mins<60:
    print(f"the time in 12hr clock is {hours-12}:{mins} PM") 
else:
    print(f"the entered time is already in 12hr clock i.e;{time}")
'''
#list--->different datatypes inside the [], which are seperated by ",". Ex-[2,"divya",[4.8,"sree"]]
#list is mutable i.e; i can modify on that particular variable
#immutable-cannot modify directly on a variable. Ex-String
'''
list_1=[1,2,3,"python",[1,2,["python","java"],"language"]]      #check the notes
print(list_1[4][2][0][3])
print(list_1[4][2][1][2])
'''
#methods of list-append(),extend(),remove(),pop()
#append()--->used to add new item into the list at the last index of the list
#syntax--->variable_name.append(item)            #only one item
'''
list_2=[1,2,3,4,5]
print(list_2)
list_2.append(21)
print(list_2)
list_2.append(10)
print(list_2)
list_2.append([1,2])
print(list_2)
list_2.append("list")
print(list_2)
list_2.append(0.3)
print(list_2)
'''
#extend()--->used to add items at the last index where each item/substring is each index in the list
'''
list_3=[4,5,6,7]
list_3.extend("sree")            #seperates every item even if its a string, list
print(list_3)
list_3.extend([8,9])
print(list_3)
list_3.extend([1,0.8])          #float alone cannot be extended
print(list_3)
'''
#remove()--->will delete the item or a value directly from any position
#syntax--->variable_name.remove(item)
'''
list_4=[1,4,5,"python",6,4,8]
list_4.remove(4)
print(list_4)
'''
#pop()--->will delete the item or value based on index position
#syntax--->variable_name.pop(index number)
list_5=[1,4,5,"python",6]
list_5.pop(1)
print(list_5)





























