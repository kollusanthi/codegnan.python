'''

                                                                         Output Formatting
                                                                         -----------------
1. camma(,) separation
----------------------
eg--
name='santhi'
age=21
print('welcom', name,'your age is',age)

2. F-string (doc-string)
------------------------
eg--
name='santhi'
age=21
print(f'Welcome {name} your age is {age}')

3. %
-----
%s --> all
%d --> digit only
%f --> float
eg--
name='santhi'
age=21
height=5.23
print('Name :%s' %name)
print('age : %d' %age)
print('heaight : %f' %height)

4. (dot) .format()
------------------
eg--
name='santhi'
age=21
print('name :{}'.format(name)) -- print single variable
print('name :{} age : {}'.format(name,age)) -- print side by side
print('name :{} \nage : {}'.format(name,age)) -- print in new line


statements
----------
1.condition -- if, if_else, elsif, mestedif
2.control -- break, control, pass
3.loop -- for loop(we know how many iterations), while loop(we don't know how many iterations)

if condition
------------
--> the if condition is used to check it is true or false
eg--
age=int(input('Enter your age'))
if age>=18:
    print(f'your age is {age} and eligible to vote')

if - else
---------
--> else is the fall-back statement, incase condition is false then this else block will execute... 
eg1--
age=int(input('Enter your age: '))
if age>=18:
    print(f'your age is {age} and eligible to vote')
else:
    print(f'your age is {age}, you have to wait {18-age} years')

eg2--
num=int(input('Enter the number: '))
if num%2==0:
    print(f'{num} is an even number')
else:
    print(f'{num} is an odd number')

eg3--
vol_ =input('Enter single letter: ')
if vol_ in 'aeiouAEIOU':
    print(f'{vol_} is vol')
else:
    print(f'{vol_} is con')

eg4--
so=input("Enter: ")
if so[::-1]==so:
    print(f'{so} is a palindrom')
else:
    print(f'{so} is not a palindrom')

eg5--
year_=int(input('Enter year: '))
if year_%4==0 and year_%100!=0 or year_%400==0:
     print(f'{year_} is leap year')
else:
     print(f'{year_} is not a leap year')

eg6--
mobile_=input('Enter your mobile number: ')
length=len(mobile_)
print(length)
if length ==10:
    print(f'{mobile_}  is an india number')
else:
    print(f'{mobilr_} is not an india number')
    

'''

mobile_=input('Enter your mobile number: ')
length=len(mobile_)
print(length)
if length ==10:
    print(f'{mobile_}  is an india number')
else:
    print(f'{mobilr_} is not an india number')
    
