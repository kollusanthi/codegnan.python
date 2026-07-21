'''

                                                                            Input Formatting
                                                                            ----------------


int -- int(input())
---
eg--
num=int(input('enter a num: '))
print(num+9)
print(type(num))

string -- input()
------
eg--
we=input('enter: ')
print(type(we))

list
----
eg--
nums=list(map(int,input('Enter nums: ').split()))
print(nums)

nums=input('Enter nums: ').split()
print(nums)

tuple
-----
eg--
nums=tuple(map(int,input('Enter nums: ').split()))
print(nums)

--give any value it will takes

num=eval(input('Enter: '))
print(type(num))

-- reverse the string
eg--
s='python'
print(s[::-1])

rev=''
for i in s:
    rev=i+rev
print(rev)


-- 24 hours clock into 12 hrs clock

time_=input('Enter 24H clock time: ')
parts_=time_.split(':')
hours_=int(parts_[0])-12
print(hours_,':',parts_[1],'pm')


'''
time_=input('Enter 24H clock time: ')
parts_=time_.split(':')
hours_=int(parts_[0])-12
print(hours_,':',parts_[1],'pm')







