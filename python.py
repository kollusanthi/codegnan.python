'''
to find datatype -- type(variable_name)
to find memory -- id(variable_name)

datatypes
---------

int
---
number=9
float
-----
num=15.17
print(type(num))

string
------
--> string scqunce of char that are inclosed in  ('', "")
--> string is immutable

method
------
replace()
--------
used to replace old str with new string
syntax-- variable_name.replace('old_str','new_str','how many')
eg--
so='python is a language'
print(so.replace('python', 'java'))
print(so)

join()
------
--> this method will add the new char after every sub-string 
syntax -- 'new_string'.join(variable_name)
eg--
so='python is a language'
print('-'.join(so))

split()
-------
eg--
so='python is a language'
print(so.split(' '))

index()
-------
--> tells character position, finds position
-->indexing means it tells the character in the given index position
eg--
so='python is a language'
print(so.index('a'))

count()
-------
so='python is a language'
print(so.count('a'))
print(so.count('n',10,16))
indexing:
so='python is a language'
print(so[10])

list
----
-->list is the collection of different datatypesthat are represented in [] and separated by ,
-->mutable datatype
eg--
any_=[1,'python',[2,4]]
print(any_[1][2])

methods
------
append() --> this method is used to add new item into the list and it will add at last index position
eg--
any_=[1,2,3,4,5]
any_.append(10)
print(any_)
any_.append("python")
print(any_)

extend() --> it is used to add new item into the end of the list
eg--
any_=[1,2,3,4,5]
any_.extend("python")
print(any_)
any_.append("python")
print(any_)

remove() --> the remove will delete the item based on the value given...
if the value is not in the list will the error
eg--
any_=[1,2,3,4,5]
any_.remove(2)
print(any_)

pop() -->the pop will delete the item based on the index position given...
if the indexx position is out of range in the list will the error
eg--
any_=[1,2,3,4,5]
any_.pop(2)
print(any_)
print(any_.pop())
'''
