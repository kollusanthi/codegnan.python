'''
Functions
---------
--> function is block that can be executes when we call it...
--> to avoid the repeated lines of code

def function_name(parameters):
    ------
    ------
    ------
function_name(arguments)

Types of functions
------------------
1.Build-in
----------
examples--
print()
len()
max()
min()
sum()

2.user-defined
--------------
--> user-define are the functions that are develop by the user
eg1--
num1=5
num2=10
def total_(num1,num2):
    print(num1+num2)
total_(num1,num2)
total_(1,2)

eg2--
num1=10
num2=5
def total_(num1,num2):
    print(num1+num2)
    print(num1*num2)
    print(num1-num2)
    print(num1//num2)
total_(num1,num2)

Required arguments
--------------------
--> We have to pass same number arguments that match in the paramenters
eg--
num1=10
num2=5
def total_(num1,num2):
    print(num1)
total_(num1,num2) -- this
total_(1,2,3) -- this one gets error 

Positional arguments
--------------------
--> It does not matter how we are passing the variable, if we assign the value to the variable in the calling...

eg1--
def name_(name='sony'):
    print(name)
name_('Santhi')

eg2--
def num(a,b):
    print(a)
    print(b)
num(b=5,a=3)
eg3--
def name(first, last):
    print(first)
    print(last)
name(last='kollu', first='Santhi')

eg4--
def pos_(m,d,a,c,b):
    print(a)
    print(b)
    print(c)
    print(d)
    print(m)
pos_(a=0,b=8,c=4,d=1,m=7)

default arguments
-----------------
eg--
def any_(age, edu, name):
    print(name)
    print(age)
any_('santhi',21,'B.Tech')

eg--
def any_(age, edu, name):
    print(name)
    print(age)
any_(name='santhi',age=21,edu='B.Tech')

Variable-length positional arguments
------------------------------------
*args
-----
--> we can pass tuple of arguments and stored in a single parameter by just adding * before the parameter...
--> and we can access the arguments using indexing 
eg--
def all_va(*nums):
    print(nums)
    print(nums[1])
    print(nums[0]+nums[3])
all_va(10,34,5,89)

Variable-length keyword arguments
---------------------------------
**kargs
----------
--> By pass keyword arguments in the arguments, will get it as dictionary just adding ** before the parameter
--> and can access by using dictionary methods...

eg1--
def dect(**all_in):
    for key, val in all_in.items():
        print(key,':',val)
dect(name='santhi', age='21', role='mentor')

eg2--
def dct_nums(*args,**key_args):
    print(args)
    print(key_args)
dct_nums(12,56,7,name='santhi',age=21,edu='B.Tech')

Scope of variables
------------------
1.Global
2.Local
eg--
num2=55 -- global varoable
def nums(num2):
    num1=90 -- local variable
    print(num1)
    print(num1+10)
nums(num2)
print(num2)

eg-- fibonacci
limit=int(input('Enter limit: '))
a,b=0,1
sum_=0
def fibonacci(a,b):
    print(a,b,end=' ')
    for i in range(limit):
        sum_=a+b
        a=b
        b=sum_
        print(sum_,end=' ')
fibonacci(a,b)


pass by values
--------------
--> passing direct values in the arguments
eg--
def any_(a,b):
    print(a)
    print(b)
any_(8,56)

--> taking user input
eg--
def any_(num1,num2):
    print(num1)
    print(num2)
any_(num1=int(input('Enter num1: ')), num2=int(input('Enter num2: ')))

--> reference input
eg--
def any_(num1,num2):
    print(num1)
    print(num2)
any_(num1=8,num2=6)

'''

def any_(num1,num2):
    print(num1)
    print(num2)
any_(num1=8,num2=6)














