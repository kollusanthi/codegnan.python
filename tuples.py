
'''tuple
-----
--> tuple is collection of different datatype that are represented in () and separated by ,
--> tuple is immutable
go=(1,'java',[3,4],('python',78))
print(type(go))

methods
-------
index()
------
go=(1,'java',[3,4],('python',78))
print(go.index('java'))
print(go[2][1])

count()
------
syntax -- variable_name.count(item)
go=(1,'java',[3,4],('python',78))
print(go.count('python')) --> 0/p-- 0 because it does't count 'python' , it is not a separate item in tuple 
print(go.count('java')) --> o/p--1 , it counts because it is separate item in tuple
print(go.count(('python',78))) -->o/p-- 1


dictionary
----------
--> dict is a key : value pair
--> keys and values separated by :
--> dict is represented by {}
--> keys must be immutable datatypes
man={1:9,
     'name':'santhi',
     (3,5):90,
     2:90}
print(man)

methods
-------
1.keys
------
syntax -- dict.keys()
details={'name':'santhi',
         'a/c':3000056423,
         'pan':87654345678,
         'adhaar':8765445678,
         'pin':1517}
print(details.keys())
2.values
--------
syntax -- dict.values()
details={'name':'santhi',
         'a/c':3000056423,
         'pan':87654345678,
         'adhaar':8765445678,
         'pin':1517}
print(details.values())

3.items
-------
syntax -- dict.items()
details={'name':'santhi',
         'a/c':3000056423,
         'pan':87654345678,
         'adhaar':8765445678,
         'pin':1517}
print(details.items())

4.update
--------
syntax -- dict.update({key:value})
details={'name':'santhi',
         'a/c':3000056423,
         'pan':87654345678,
         'adhaar':8765445678,
         'pin':1517}
details.update({'name':'sara'}) -- change the name 
details.update({'gender':'female'}) -- adds new column to the dict
print(details)
details['name']='kollu' -- other way to change the name
print(details)


5.clear()
--------
syntax -- dict.clear()
details.clear()
print(details)

'''
