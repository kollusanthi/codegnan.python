'''
a.math
-----
--> math module used to do work on mathematical functionality

floor
-----
-->it will round-down to the near value
eg--
import math
print(math.floor(3.78))

ceil
----
-->it will round-up to the near value
eg--
import math
print(math.ceil(3.78))

gcd
----
-->it will find the gcd(greater common division) or HCF value
eg--
import math
print(math.gcd(24,36))

lcm
----
-->it will find the lcm value
eg--
import math
print(math.lcm(24,36))

sqrt
----
-->it will get square root value
eg--
import math
print(math.sqrt(25))

factorial
---------
--> it will give factorial value
eg--
import math
print(math.factorial(5))

eg--
import math
print(math.log(2,3))
print(math.cos(math.pi))
print(math.pi)
print(math.cos(90))

b.sys
-----
--> sys module is used to get details of python interpreter

version
-------
--> the version of python interpreter
eg--
import sys
print(sys.version)

path
----
--> .py path we will get by this function
eg--
import sys
print(sys.path)

exit
----
--> this function will exit from the program
eg--
import sys
print(sys.exit())

platform
--------
--> it will gives the python run platform
eg--
import sys
print(sys.platform)

argv
----
--> it will give the current file run path
eg--
import sys
print(sys.argv)



c.os
d.random
--------
--> the random module used to get random number

randint
-------
--> used to generate random numbers based on the range
eg--
import random
print(random.randint(1,100))

choice
------
--> it will the random value from the given data
eg--
import random
color=['red','green','blue','yellow']
print(random.choice(color))

shuffle
-------
--> it can shuffle the data randomly
eg--
import random
color=['red','green','blue','yellow']
random.shuffle(color)
print(color)

uniform
-------
-->it will give the decimal values in a range given
eg--
import random
print(random.uniform(1,100))


.datetime
---------
-->used to work with date and time

now
---
--> it will give the today time + date
eg--
from datetime import datetime
print(datetime.now())

eg2--
from datetime import datetime, date, time
print(datetime.now())
print(datetime.today())

eg3--
from datetime import datetime
now=datetime.now()
print(now.strftime('%y-%m-%d'))  --> it gives year, month and day
print(now.strftime('%y-%m')) --> it will give year and month only
print(now.strftime('%y'))
print(now.strftime('%A'))
print(now.strftime('%B'))
print(now.strftime('%H:%M:%S'))

%y --> will get the year
%m --> will get the month
%d --> will get the day
%H --> will get the hours
%M --> will get the minutes
%S --> will get the seconds
%A --> will get the current day
%B --> will get the current month name

.collections
-----------
--> the collections module will provide container type data which is more powerful than built-in data types(dict,list,tuple)
eg--
import collections
data=['apple','banana','orange','mango','banana']
print(collections.Counter(data))

deque
-----
--> deque(double ended queue) is used work with list
append
------
eg--
from collections import deque
how=deque([1,2,3])
how.append(7)
print(how)  o/p-- [1,2,3,7]

eg2--
from collections import deque
how=deque([1,2,3])
how.appendleft(7)
print(how)  0/p-- [7,1,2,3]

extend
------
eg--
from collections import deque
how=deque([1,2,3])
how.extend([4,5,6])
print(how)

eg2--
from collections import deque
how=deque([1,2,3])
how.extendleft([4,5,6])
print(how)   o/p-- [

pop()
-----
eg1--
from collections import deque
how=deque([1,2,3])
how.pop()
print(how)  o/p-- [1,2]

eg--2
from collections import deque
how=deque([1,2,3])
how.popleft()
print(how)  o/p-- [2,3]

namedtuple
----------
eg--
from collections import namedtuple
data=namedtuple('stu',('name','age'))
print(data('santhi','21'))


.itertools
----------

count
-----
eg--
from itertools import count
c=count(100)
for i in range(5):
    print(next(c))

repeat
------
eg--
import itertools
for i in itertools.repeat('python',10):
    print(i)

permutations
------------
eg--
from itertools import permutations
data=permutations([1,2,3],2)
print(list(data))

combinations
------------
eg--
from itertools import combinations
data=combinations([1,2,3],2)
print(list(data))


eg--
from itertools import permutations,combinations
data=permutations([1,2,3],2)
print(list(data))

any_=combinations([1,2,3],2)
print(list(any_))

platform
--------
eg--
import platform
print(platform.python_version())
print(platform.python_compiler())
print(platform.machine())
print(platform.processor())

'''

import platform
print(platform.python_version())
print(platform.python_compiler())
print(platform.machine())
print(platform.processor())

















