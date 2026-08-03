'''
list comprehension
------------------
--> the comprehension is the short form of syntax used to generate a new list from the old list...
syntax --> [expression loop]
eg--
nums=[1,2,3,4,5]
new_list=[j for j in nums]
print(new_list)

eg--
nums=[1,2,3,4,5]
new_list=[j for j in nums if j%2==0]
print(new_list)

eg--
nums=[1,2,3,4,5]
new_list=[j if j%2==0 else 'odd' for j in nums]
print(new_list)

nel=[i for i in nums if i%2!=0]
print(nel)

Nested comprehension
--------------------
--> Nested comprehension means an comprehension inside the another comprehension is called the nested comprehension
syntax -- [expression loop_1 loop_2]
eg--
all_=[j for j in match]
all_n=[num for i in match for num in i]
print(all_)
print(all_n)

eg--
n=[i for i in range(1,6)]
new_=[[i*j for i in range(1,6)] for j in range(1,6)]
print(n)
print(new_)

generator
---------
--> this generator will genereate value one at a time and the pause it on the position when we are using yield keyword
--> here we will use yield to get the value
yield keyword
-------------
--> this yield() is used to get the value and will only gives one value and pauses there itself
next keyword
------------
--> the next() will retrieve the  value 

eg--
def gen(n):
    for i in range(1,n+1):
        yield i*i
a=gen(5)
print(next(a))
print(next(a))
print(next(a))


Difference between functions and generators
-------------------------------------------
Function        
--------    
--> return  
--> when the return is executed, it will exit for the function
--> in functions will get all values once
eg--
def any_(n):
    for i in range(1,n+1):
        print(i*n)
b=any_
print(b(5))

Generator
---------
--> yield
--> when the yield is executed, it will pause the function and the next yield is called then it will resume again
--> in generator will get one at a time
eg--
def gen(n):
    for i in range(1,n+1):
        yield i*i
a=gen(5)
print(next(a))
print(next(a))
print(next(a))

'''

def gen(n):
    for i in range(1,n+1):
        yield i*i
a=gen(5)
print(next(a))
print(next(a))
print(next(a))









                    





















