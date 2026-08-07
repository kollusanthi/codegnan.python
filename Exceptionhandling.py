
'''

Exception handling
------------------
--> an error can be handled by try and execept

1.try:
------
--> we can check the code here which may contain any error
syntax --> try:
               write code here...

eg--
try:
    print(n)
except:
    print('error')


2.except:
---------
--> exception can handle any error that come in the try block
eg1--
try:
    num1=6
    num2=0
    print(num1/num2)
except:
    print('ZeroDivisionError')

eg2--
try:
    num=int(input('Enter a number: '))
    print(num+9)
except:
    print('Error')

eg3--
try:
    print(9+'python')
except:
    print('Error')

3.else:
-------
--> if no error in the code were raised, then the else block will execute
eg--
try:
    print(9+6)
except:
    print('Error')
else:
    print('no error')

eg2--
try:
    print(9/0)
except ZeroDivisionError:
    print('This will raise ZeroDivisionError')
else:
    print('no error')

eg3-- this will check only one error which comes first
try:
    print(9/0)
    print(num)
except ZeroDivisionError:
    print('This will raise ZeroDivisionError')
except NameError:
    print('This will raise NameError')
else:
    print('no error')

eg4-- this will check only one error which comes first( uses for debugging )
try:
    print('python'+9)
    print(9/0)
    print(num)
except ZeroDivisionError:
    print('This will raise ZeroDivisionError')
except NameError:
    print('This will raise NameError')
except TypeError:
    print('TypeError')
else:
    print('no error')

4.finally:
----------
--> the finally block will execute if error present in the try block or not

eg1-- with error
try:
    print(9/0)
except ZeroDivisionError:
    print('This will raise ZeroDivisionError')
else:
    print('no error')
finally:
    print('End')

eg2-- without error
try:
    print(9/3)
except ZeroDivisionError:
    print('This will raise ZeroDivisionError')
else:
    print('no error')
finally:
    print('End')


file handling
-------------
--> an file handler is an object used to connect with that particular file

1.with(keyword)
---------------
--> By using with keyword no need close the file, it will close it by itself
syntax for file name
------
with open('file_name','mode') as alias_name:

syntax for file path
-------
with open(r'file_path','mode') as aslias_name:

eg--
with open(r'C:\Users\santhi\Desktop\codegnan\demo.text','r') as f1:
    print(f1.read())


eg--
with open('demo.txt','r') as f1:
    print(f1.read())

2.open()
-------
--> by using this open() we have to close the file by using close()
eg--
any_=open('demo.txt','r')
print(any_.read())
any_.close()

modes
-----
1.'r'
-----
--> the 'r' mode is used for functions read(), readline() and readlines()
eg--
with open('demo.txt','r') as file:
    print(file.read())

    
2.'w'
-----
--> the 'w' mode is used for write() function

eg--
with open('demo.txt','w') as file:
    file.write('The time is 3:15 pm')
    
3.'a'
-----
--> the 'a'  mode is used for write() function and it will add the text at last position
eg--
with open('demo.txt','a') as file:
    file.write('python module takes 2 hrs per day')


4.'x'
-----
--> it is used to create a new file
eg--
with open('demo1.txt','x') as file:
    file.write('this creates files')


function
--------
1.write()
2.read()
--------
--> the read() function will read the file chunk by chunk where we can specify the size
eg--
with open('demo.txt','r') as file:
    print(file.read(10))

3.readline()
------------
--> it will only read one line at a time
eg--
with open('demo.txt','r') as file:
    print(file.readline())

4.readlines()
-------------
--> the readlines() will read whole file and writen it in a list, where each line is one index in the list
eg--
with open('demo1.txt','r') as file:
    print(file.readlines())

'''











    

