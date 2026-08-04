'''
Modules
-------
--> Modules are the python code which is saved in (.py) that contains functions, variables, classes

types
-----
1.Build-in
----------
--> the build-in modules that are already designed which comes with python when we are installing

eg--
.math
.sys
.os
.random

2.user-defined
--------------
--> the user-defined modules are created by the programmer
syntax--> import(keyword) module_name
eg--
import first_module
print(first_module.add(10,5))
print(first_module.sub(10,5))
print(first_module.mul(3,2))

importing with alias name
-------------------------
--> we can also import a module with different name
--> after importing with the alias name, we have to use that alias name in the code
eg--
import first_module as fm
print(fm.add(10,5))
print(fm.sub(10,5))
print(fm.mul(3,2))

eg--
import first_module as fm
print(fm.add(10,5))
print(first_module.mul(3,2))
o/p--
15
Traceback (most recent call last):
  File "C:/Users/santhi/Desktop/codegnan/module.py", line 36, in <module>
    print(first_module.mul(3,2))
NameError: name 'first_module' is not defined

importing only need functoin
----------------------------
--> when we are importing the few functions from the module can only access that function
syntax--> from(keyword) module_name import(keyword) functions
eg--
from first_module import add,mul
print(add(5,15))
print(mul(3,4))

importing all functons
----------------------
--> use the all functions in that module we have to use (*) to get all of those...
syntax--> from(keyword) module_name import(keyword) *
eg--
from first_module import *
print(add(12,8))
print(sub(12,8))
print(mul(12,8))
print(div(10,2))

eg--
import first_module
print(first_module.display())
eg--
import first_module
first_module.display()
eg--
import first_module
first_module.display('Kollu')

random
------
eg--
import random
print(random.randint(1,10))
print(random.randint(1000,9999))

math
----
import math
print(math.sqrt(25))

sys
---
import sys
print(sys.version)

'''


details={
    'name':'santhi',
    'ATM PIN':'2020'
    }
import random

remain=3
while remain>0:
    pin_=input('Enter pin number: ')
    if pin_==details['ATM PIN']:
        otp=random.randint(1000,9999)
        print(otp)

        user_otp=int(input('Enter user otp: '))
        if user_otp==otp:
            opt=int(input('Enter option \n1.Withdraw \n2.Deposite \n3.Check balance \n4.History:\n'))
    else:
        remain-=1
        if remain>0:
            print(f'Incorrect pin entered and you have {remain} left')
        else:
            print(f'You have entered 3 times incorrect pin, card is blocked')





























