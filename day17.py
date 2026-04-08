#recursive functions()--->recursion is a programming technique where a function calls itself either directly or indirectly
#to solve a problem by breaking it into smaller,simpler subproblems.
#recursion is especially useful for problems that can be divided into identical smaller tasks such as mathematical
#calculations,tree traversals or divide and conquer algorithms.
'''
def validate_pin(self):
    while self.remaining_attempts>0:
        user_pin=input("enter a 4-digit pin: ")
        if len(user_pin)==4 and user_pin==self.user_information['pin']:
            print(" ✅welcome to ATM")
            return True
        else:
            self.remaining_attempts-=1
            if self.remaining_attempts>0:
                print(f"❌Invalid pin.attempts left:{self.remaining_attempts}")
            else:
                print("card blocked.please contact customer service")
                return False
'''
'''
str="i am leaning python"
vowel_list=[]
consonant_list=[]
def vowel_consonant(str,vowel_list,consonant_list):
    for j in str:
        if j in "AEIOUaeiou":
            vowel_list.append(j)
        elif j not in "AEIOUaeiou" and j not in " ":              #excludes spaces also
            consonant_list.append(j)
    print(f"{vowel_list} are all the vowels in the string")
    print(f"{consonant_list} are all the consonants in the string")
vowel_consonant(str,vowel_list,consonant_list)
'''
num=int(input("enter a number: "))
count=0
def prime_num(num,count):
    for j in range(1,num+1):
        if num%j==0:
            count+=1
    if count==2:
        print("prime")
    else:
        print("not")
prime_num(num,count)


























    
