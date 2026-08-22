'''

Regular Expression(RegEx)
-------------------------
--> This RegEx is used to form a search pattern to find out the string contain sequence char or not
--> To use this RegEx, we need to import re module

Functions
---------
Findall
-------
--> The searching pattern is found then, it will gives the output in the list[]
eg--
import re
some='Python is a programming language'
print(re.findall('[a]', some))


Search
------
--> This is also used to form a search pattern, but it will give only the first matched object or first occurance
--> Where it will gives with the index position, where the matched object is found by the pattern
eg--
import re
do='I have 1000 rupees with me'
print(re.search('e', do))


Meta characters
---------------
--> Meta characters are the symbols used in the search pattern

1. []
--> This [] symbol is used to find a group char that present in the string, where we can also specify the range
syntax --> re.findall('[range/ pattern]', variable_name)
--> By using this symbol we can search cap(A-Z), small(a-z) and digits(0-9)
eg--
import re
some='We are in the Class 5'
print(re.findall('[aeiou]', some))
print(re.findall('[a-z]', some))
print(re.findall('[A-Z]', some))
print(re.findall('[0-9]', some))
print(re.search('[a-z]', some))
print(re.search('[A-Z]', some))


2. .
--> This . symbol will refer only one character means can match only a single char in the pattern...
syntax --> re.search('char...', variable_name)
eg--
import re
some='Hello! World'
print(re.findall('H...o', some))
print(re.search('H..',some))


3. +
--> This + symbol will find max number of sequence from the string from atleast one character
syntax --> re.findall('.+', variable_name)
eg--
import re
some='Hello! world This is example'
print(re.findall('H.+i',some))

4. ^
--> The ^ symbol is used to find pattern where string starting match or not
syntax --> re.findall('^', variable_name)
eg--
import re
some='Hello! World'
print(re.findall('^Hello', some))
print(re.search('^Hello',some))

5. $
--> This $ symbol will find out if the string is ending with pattern or not
syntax --> re.findall('sequence$', variable_name)
eg--
import re
any_='I am planning for a trip'
print(re.findall('trip$', any_))
print(re.search('trip$',any_))

6. ?
--> This ? symbol will find max upto 1 match in the pattern/string
syntax --> re.findall('.?', variable-name)
eg--
import re
some='Hello! world Hello'
print(re.findall('Hel.?o',some))

7. *
--> This * symbol will find max numberof sequence from the string
syntax --> re.findall('.*', variable_name)
eg--
import re
some='Hello! world'
print(re.findall('H.*l',some))


8.{}
--> The {} symbol is used to find a group char that present in string
syntax --> re.findall('char.{size}', variable_name)
eg--
import re
all_='I have 1000 rupees with me'
print(re.findall('I.{12}', all_))

check name
----------
import re
user_name=input('Please enter your name: ')
pattern=re.findall('^[a-z, A-Z]{3,}$', user_name)
if pattern:
    print('Correct name')
else:
    print('Incorrect name')

check whether the number is india or not
----------------------------------------
import re
num=input('Please enter a number: ')
fnd=re.findall('^[6-9][0-9]{9}$', num)
if fnd:
    print('Indian')
else:
    print('Not Indian')
'''

import re
some='Hello! world This is example'
print(re.findall('H.+i',some))






























