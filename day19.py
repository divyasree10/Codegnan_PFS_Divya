#generators--->this is a special type of function that generates return an ITERATOR which one at a time(slight time delay)
#yield--->pauses and resumes the value.this is not a normal keyword and cannot be used in normal functions
#used to produce a value and pause execution
'''
def gen():
    yield 1                       #yield is similar to return in functions
    yield 2
    yield 3
gen1=gen()
print(next(gen1))
print(next(gen1))
print(next(gen1))
'''
'''
def square_gen(n):
    for i in range(n):
        yield i*i
for val in square_gen(11):
    print(val)
'''
'''
def add(n,m):
    yield n+m
add1=add(23,54)
print(next(add1))
'''
'''
def num(n):
    if n%2==0:
        yield 'even'
    else:
        yield 'odd'
num1=num(12)
print(next(num1))
'''
#Next()--->used to get next value from a generator
#when the value is finished,it will stop the iterator
def square_gen(n):
    for i in range(n):
        yield i
for val in square_gen(11):
    print(val)





















