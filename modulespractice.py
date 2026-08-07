
'''
asscii_letters --> this string mudule function that can give upper and lower letters
digits --> string module function that can give number(0-9)
punctuation --> this string module function can give us punctuation (!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~)

punctuation=string.punctuation

import random
import string

letters=string.ascii_letters
digits=string.digits

special_char='@#*$'

all_chars=letters+digits+special_char

password=''
for i in range(5):
    password += random.choice(all_chars)
print(password)

atm
---

bank_balance=10000
from datetime import datetime
import sys
now=datetime.now()

while True:
    print('---------Welcome to SBI ATM----------')
    user_opt=int(input('\n1.Withdraw \n2.Deposite \n3.Check Balance \n4.Exit'))
    if user_opt==1:
        with_m=int(input('Enter the money you want to withdraw: '))
        if with_m<bank_balance:
            bank_balance-=with_m
            print(f'remaining money {bank_balance} {now.strftime('%H:%M %y-%m-%d')}')
        else:
            print('insufficient money')
    elif user_opt==2:
        Deposite_m=int(input('Enter the money you want to deposite: '))
        bank_balance+=Deposite_m
        print(f'Money added successfully: {bank_balance} {now.strftime('%H:%M %y-%m-%d')}')
    elif user_opt==3:
        print(f'Available balance: {bank_balance} {now.strftime('%H:%M %y-%m-%d')}')
    elif user_opt==4:
        sys.exit()



guess the random number game
----------------------------
import random
num=random.randint(1,100)
user_opt=int(input('guess the number: '))
if user_opt==num:
    print('Congragulations! You win the game')
else:
    print('Incorrect, you loose the game')

    

import random, math, datetime, sys
print(random.randint(1,10))
data=['s','a','n','t','h','i']
print(random.choice(data))
print(random.uniform(1,10))
random.shuffle(data)
print(data)
print(math.factorial(5))
print(sys.version)
print(datetime.today())
'''




with open('demo.txt','w') as file:
    print(file.write('The time is 3:15 pm'))



































                
