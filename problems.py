
'''
1.Generate even and odd numbers for a certain range

eg--
limit_=int(input('Enter the limit: '))
for j in range(1,limit_+1):
    if j%2==0:
        print(f'{j} is a even')
    else:
        print(f'{j} is an odd')

2. check whether the number is a prime or not

eg1-- logic1
num=int(input('Enter a number: '))
res=1
for i in range(2,num):
    if num%i==0:
        res=0
        break
if res==1:
    print(f'{num} is prime')
else:
    print(f'{num} is not a prime')

eg-- logic2
num=int(input('Enter a number: '))
count=0
for i in range(1,num+1):
    if num%i==0:
        count+=1
if count==2:
    print(f'{num} is prime')
else:
    print(f'{num} is not a prime')


3. Generate prime numbers for a certain limit

eg--logic1

limit_=int(input('Enter the limit: '))
for i in range(2,limit_):
    res=1
    for j in range(2,i):
        if i%j==0:
            res=0
            break
    if res==1:
        print(f'{i} is prime')

        
eg2-- logic2

limit_=int(input('Enter the limit: '))
for i in range(2,limit_):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count==2:
        print(f'{i} is prime')


4. Reverse a string and check if it is palindrom or not

eg--
s=input('Enter: ')
rev_=''
for i in s:
    rev_=i+rev_
if rev_==s:
    print(f'{s} is Palindrom')
else:
    print(f'{s} not a palindrom')

5. draw rightangle triangle using * for a limit
o/p--
*
**
***
****

eg-- logic1
n=int(input('Enter a num: '))
for i in range(1,n+1):
    for j in range(1,i+1):
        print('*',end='') --> end is used to print the starts side by side
    print()  --> print() is used to go to the next line

eg-- logic2
n=int(input('Enter a num: '))
for i in range(1,n+1):
    print('*' *i)

0/p--
1
12
123
1234
12345


eg--
n=int(input('Enter a num: '))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end='')
    print()

o/p--
1
23
456
78910

eg--
n=int(input('Enter a num: '))
count=0
for i in range(1,n+1):
    for j in range(1,i+1):
        count+=1
        print(count,end='')
    print()

6. reverse tringle
o/p--
*****
****
***
**
*

eg--
n=int(input('Enter a num: '))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print('*',end='')
    print()
    
0/p--
10
98
765
4321

eg--
n=int(input('Enter a num: '))
count=0
for i in range(n,0,-1):
    for j in range(1,i+1):
        count+=1
        print(count,end='')
    print()
    
o/p--
1234
123
12
1

eg--
n=int(input('Enter a num: '))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end='')
    print()

7.  to print piramid
o/p--
    *
   * *
  * * *
 * * * *
* * * * *

eg--
n=int(input('Enter a num: '))
for i in range(n):
    print(' '*(n-i-1),end='') --> to give spaces before  starts
    print('* '*(i+1)) --> to print starts

8. reverse piramid
o/p--
* * * *
 * * *
  * *
   *

eg--
n=int(input('Enter a num: '))
for i in range(n,0,-1):
    print(' '*(n-i),end='')
    print('* '*(i))

-- remove doublicates from the list
eg--

nums=[1,2,2,5,5]
emp_=[]
for j in nums:
    if j not in emp_:
        emp_.append(j)
print(emp_)

9. check whether the given number is a perfect number or not
eg--
num=int(input('Enter a num: '))
per_num=0
for j in range(1, num):
        if num%j==0:
            per_num+=j
if per_num==num:
    print(f'{num} is perfect number')
else:
    print(f'{num} is not a perfect number')


10. to print a table upto a certain limit
eg--
num=int(input('Enter the table: '))
for i in range(1,11):
        print(f'{num} X {i} = {num*i}')

11.Amstrong Number

eg--
num=int(input('Enter the num: '))
length=len(str(num))
am_=0
for i in str(num):
    am_=int(i)**length+am_
if am_==num:
        print(f'{num} is Amstrong')
else:
        print(f'{num} is not amstrong')

12. Generate Fibbonoce numbers for a certain limit
eg--
limit_=10
num1=0
num2=1
print(num1,num2,end=' ')
for i in range(1,limit_+1):
        all_add=num1+num2
        num1=num2
        num2=all_add
        print(all_add, end=' ')

13. Calculator
eg--
num1=int(input('Enter a num: '))
num2=int(input('Enter a num: '))
opt_=int(input('Enter  \n1.ADD \n2.SUB \n3.MUL \n4.DIV : \n'))
if opt_==1:
        print(num1+num2)
elif opt_==2:
        print(num1-num2)
elif opt_==3:
        print(num1*num2)
elif opt_==4:
        print(num1/num2)
else:
        print('Enter correctly')


14. ATM Working


'''

ICIC_Santhi={'name':'Santhi',
             'addhar':'454323456',
             'Pan':'3er345678g',
             'ATM_PIN':'2020',
             'Balance':5000,
             'Transaction History':[]}
remain_A=3
withdraw=0
deposite=0
while remain_A>0:
        pin_=input('Enter your atm pin: ')
        if len(pin_)==4:
                if pin_ in ICIC_Santhi['ATM_PIN']:
                        opt_=int(input('Enter \n1.Withdraw \n2.Deposite \n3.Check Balance \n4.Transaction History \n5.Pin change: \n'))
                        if opt_==1:
                                withdraw_m=int(input('Enter amount you want to withdraw: '))
                                if withdraw_m<=ICIC_Santhi['Balance'] and withdraw_m%100==0:
                                        ICIC_Santhi['Balance']-=withdraw_m
                                        withdraw=withdraw_m
                                        print(f'You have withdraw {withdraw_m} and the total balance {ICIC_Santhi['Balance']}')
                                        user_=int(input('Enter  \n1.Homepage \n2.Exit: \n'))
                                        if user_==1:
                                                print('Home page')
                                        else:
                                                print('Thank you for visiting')
                                                break
                                else:
                                        print('Can not provide change or no balance')
                                        break
                        elif opt_==2:
                                deposite_m=int(input('Enter the money you want to deposite: '))
                                if deposite_m%100==0:
                                        ICIC_Santhi['Balance']+=deposite_m
                                        print(f' You have deposite {deposite_m} and the total balance {ICIC_Santhi['Balance']}')
                                        deposite=deposite_m
                                        user_=int(input('Enter  \n1.Homepage \n2.Exit: \n'))
                                        if user_==1:
                                                print('Home page')
                                        else:
                                                print('Thank you for visiting')
                                                break
                                else:
                                        print('Change can not be deposite')
                                        break
                        elif opt_==3:
                                print(f'Balance is {ICIC_Santhi['Balance']}')
                                user_=int(input('Enter  \n1.Homepage \n2.Exit: \n'))
                                if user_==1:
                                        print('Home page')
                                else:
                                        print('Thank you for visiting')
                                        break
                                
                        elif opt_==4:
                                print(f'Transaction history withdraw amount:{withdraw} deposite amout:{deposite}')
                                
                                user_=int(input('Enter  \n1.Homepage \n2.Exit: \n'))
                                if user_==1:
                                        print('Home page')
                                else:
                                        print('Thank you for visiting')
                                        break
                                
                        elif opt_==5:
                                pass
                else:
                    remain_A-=1
                    if remain_A>0:
                        print(f'Incorrect pin and you have only {remain_A}')
                    else:
                        print('Your card is block')
                        break
        else:
                print('Please enter only 4 digit atm pin')
        
                














