'''

elif
----
eg1-- Grade
marks_=int(input())
if marks_>=90:
    print('A+')
elif marks_>=80:
    print('B+')
elif marks_>=70:
    print('C+')
elif marks_>=35:
    print('Pass')
else:
    print('Fail')

eg2-- Greater number
num1=int(input())
num2=int(input())
num3=int(input())
if num1>num2 and num1>num3:
    print(num1,'is greater value')
elif num2>num1 and num2>num3:
    print(num2,'is greater value')
else:
    print(num3,'is greater value')


nested if
---------
eg--
details={'ATMPIN' : '2002'}
atm=input('Enter your 4 digit atm pin: ')
if len(atm)==4:
    if atm==details['ATMPIN']:
        opt=int(input('1.Enter \n1.Withdraw\n2.Deposite \n3.pinchange\n'))
        if opt==1:
            money_w=int(input('Enter money to withdraw: '))
        elif opt==2:
            money_d=int(input('Enter money to deposite: '))
    else:
        print('Icorrect pin entered')
else:
    print('Please enter only 4 digit pin')

Control Statements
------------------
1.Break
-------
--> exit from the loop
eg--
s='python'
for i in s:
    print(i)
    if i=='t':
        break
else:
    print('End')

eg-- for break
s=[2,24,34,68,91]
for i in s:
    print(i)
    if i==34:
        break
else:
    print('End')

2.Continue
----------
--> skips the particular iteration
eg--
s=[2,24,34,68,91]
for i in s:
    if i==34:
        continue
    print(i)
else:
    print('End')

3.pass
------
--> space holder
eg--
s=[2,24,34,68,91]
for i in s:
    pass

    
loops
-----
1.for loop
----------
--> for loop is used to iterate over sequence such as str, list, tuple
--> integers are not iterate
eg --
num=int(input())
for i in num:
    print(i)
--> else in for loop, it will execute when whole iterations are completed...
--> incase if condition becomes true, then else will never execute...
range()
-------
--> range() function is used to generate number upto a limit...
syntax -- range(start,end,step)
eg--
for j in range(1,11,2):
    print(j)
    

eg--
s='python'
for i in s:
    print(i)
eg--
s='python'
for i in s:
    print(i)
else:
    print('End')


    
2.whileioop
-----------
eg-- continues loop, unlimited iterations
num=1
while num<10:
    print(num)

eg--
num=1
while num<10:
    print(num)
    num+=1

assert keyword
--------------
--> the keyword used to check the condition, it will raise the error if the condition is false
eg1--
age=int(input())
assert age>=18, 'Not Eligible'
print('eligible')

eg2--
marks=int(input())
assert marks>=35, 'fail'
print('pass')

'''

marks=int(input())
assert marks>=35, 'fail'
print('pass')
























