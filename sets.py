'''
set
---
--> set is an unordered collection
--> set do not allows duplicate values inside it..
--> set is mutable
--> set is represented in {}

do={1,2,3,2}
print(do)

#creating a empty set
so=set()
print(type(set))

methods
-------
1.update
--------
--> use to add new value into set
syntax -- variable_name.update(itterable)
eg--
do={1,2,3,2}
do.update([6,8])
print(do)
do.update('python')
print(do)

2.add()
-------
--> use to add new value into set
syntax -- variable_name.add(value)
eg--
do={1,2,3,2}
do.add('python')
print(do)

3.remove()
----------
--> use to delete the value from the set, incase if the value is not present in the set it will get the KeyError
syntax -- variable_name.remove(value)
eg--
do={1,2,3,4,5}
do.remove(4)
print(do)

4.discard()
----------
--> use to delete the value from the set, but never give any error incase value is not present inside the set...
syntax -- variable_name.discard(value)
eg--
do={1,2,3,4,5}
do.discard(9)
print(do)

5.pop()
-------
--> use to delete the value but this pop() will take 0 arguments inside it
syntax -- variable_name.pop()
eg--
do={1,2,3,4,5}
do.pop()
print(do)

operations
----------
1.union
-----
--> gives all sets values together but no duplicates
eg--
do={1,2,3,4,5}
so={4,5,6,7,8}
print(do|so)
print(do.union(so))

2.intersection
------------
--> gives common values in both sets
eg--
do={1,2,3,4,5}
so={4,5,6,7,8}
print(do&so)
print(do.intersection(so))

3.difference
------------
--> gives values of set1 but the values is not in set2
eg--
do={1,2,3,4,5}
so={4,5,6,7,8}
print(do-so)
print(do.difference(so))


                                                                     Type Convertion
                                                                     ---------------

Int :
-----

string -- str()
eg--
num=9
print(type(num))
so=str(num)
print(type(so))
                                                                    
Float -- float()
eg--
num=9
print(type(num))
so=float(num)
print(type(so))


Float :
-------

String -- str()
eg--
num=8.67
print(type(num))
so=str(num)
print(type(so))

Integer -- int()
eg--
num=8.67
print(type(num))
so=int(num)
print(so)
print(type(so))

String :
--------

Integer -- int()
how="67"
print(type(how))
who=int(how)
print(type(who))

Float -- float()
how="6.58"
print(type(how))
who=float(how)
print(type(who))

List -- list()
how='12345'
print(type(how))
who=list(how)
print(who)
print(type(who))

Tuple -- tuple()
how='12345'
print(type(how))
who=tuple(how)
print(who)
print(type(who))

List
----

string -- str()
num=[1,2,3,4]
print(type(num))
all_n=str(num)
print(type(all_n))

tuple -- tuple()
num=[1,2,3,4]
print(type(num))
all_n=tuple(num)
print(all_n)
print(type(all_n))

Tuple
-----
list -- list()
num=(1,2,3,4)
print(type(num))
all_n=list(num)
print(all_n)
print(type(all_n))


string -- str()
num=(1,2,3,4)
print(type(num))
all_n=str(num)
print(type(all_n))

(+) -- Concatination
--------------------
eg--
Integers--
num1=3
num2=6
print(num1+num2)

strings--
s1='python is a'
s2=' language'
print(s1+s2)

list--
num=[1,2]
all_=[3,4]
print(num+all_)

'''



