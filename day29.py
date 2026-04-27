#Regular Expression(RegEx)--->this regular expression or RegEx is a sequence of characters that forms a searching pattern.
#to use this we have to import re, which will unlock the package
#functions--
#1.findall-->by using this function,it will find all sequence in the string
#syntax-re.findall("metachar",variable_name)
#2.search-->by using this function,it will only find 1st sequence in the string
#syntax-re.search("metachar",variable_name)
#metacharacters-->are used to form searching patterns
#1.[]-in this metacharacter we search for [a-z],[A-Z],[0-9]
'''
import re
any="this method can read the entire file and return into the list"
so=re.findall("[a-z]",any)   #this line is called searching pattern   #[aeh] for a,e,h
an=re.search("[a]",any)
print(so)
print(an)
'''
#2.dot(.)-it will form a seaching pattern as it will take any single character for (.)
'''
import re
we="hello"
the=re.findall("h...o",we)
thing=re.search("he..o",we)
print(the)
print(thing)
'''
#3.cap(^)-this is used to find the string is starting with the sequence or not
#syntax-re.findall("metachar",variable_name)
'''
import re
how="This is used to find the string is starting"
who=re.findall("^This is",how)
then=re.search("^This",how)
print(who)
print(then)
'''
#4.$-used to find the string is ending with sequence or not
#syntax-re.findall("$",variable_name)
'''
import re
out="used to find the string is empty sequence "
one=re.findall("sequence $",out)
two=re.search("used$",out)
print(one)
print(two)
'''
#5.*-will form a searching pattern as it will take any zero or more character for (*)
#syntax-re.findall(".*",variable_name)
'''
import re
hey="will form a searching pattern as it will take any zero or more character"
hi=re.findall("c.*i",hey)
hello=re.search("w.*",hey)
print(hi)
print(hello)
'''
#6.+-will form a searching pattern as it will take any one or more character for (+)
#syntax-re.findall(".+",variable_name)
import re
hey="This will form a searching pattern as it will take any one or more cahracter"
hi=re.findall("an.+y",hey)
hello=re.search("T.+",hey)
print(hi)
print(hello)























