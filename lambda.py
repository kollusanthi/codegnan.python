'''

Anonymous function
------------------
--> Anonymous function is aa function that don't any name
--> This also called as lambda function
--> lambda function will take n number of arguments but only one expression

syntax --> lambda arguments : expression
eg-- single argument
so=lambda a : a+10
print(so(5))

eg-- multiple arguments
so=lambda a,b,c : a+b+c
print(so(5,8,2))

map()
-----
--> the map function will be applied on the given function of each and every element of an itterable
eg--
nums=[1,2,3,4,5]
so=list(map(lambda x:x*x, nums))
print(so)

filter()
--------
--> filter() function will only consider if the condition is true, then it will keep thet values...
eg--
nums=[1,2,3,4,5]
so=list(filter(lambda x:x%2==0, nums))
print(so)

reduce()
--------
--> the reduce() function consider all elements and reduce to one single element...
--> to use this reduce() we have to import it first from the functools
eg--
from functools import reduce
nums=[1,2,3,4,5]
so=reduce(lambda x,y:x+y, nums)
print(so)

difference between print() and return
-------------------------------------
print()
------
--> print() is an in-build function that is used for display the values stored by variable

return
------
--> only used inside the functions
--> when the return is executed then it will exit from that function and holds the returned values in  the calling

'''


from functools import reduce
nums=[1,2,3,4,5]
so=reduce(lambda x,y:x+y, nums)
print(so)
























