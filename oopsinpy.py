'''
OOPs
----
--> object oriented programming system
--> OOPs is used to maintain the code structure in object and classes

1. class
--------
--> Class is an blueprint or template to an object

syntax
------
class(keyword) Name:
    #attribute
    #methods
    
2. object
---------
--> Object is insstance of the class

syntax
------
class(keyword) Name:
    #attribute
    #methods
variable=class_name

eg--
class person:
    name='santhi'
    edu='B.Tech'
p1=person()
print(p1.name)
print(p1.edu)

eg--
class codegnan:
    city='Hyd'
    Tech='Python'
    data_='MySQL'
code_=codegnan()
print(code_.city)


3. attribute
------------
--> Attribute is the data present in the class or pass to the class

eg--
Take car
--------
color
brand
seat

eg--
class std:
    name='Santhi'
    age=21
    edu='B.Tech'
an=std()
print(an.name)
--> in this example name, age, edu are attributes


class car:
    def __init__(self):
        self.color='Red'
        self.seat=6
        self.brand='BMW'
    
c1=car()
print(c1.color)
print(c1.brand)
print(c1.seat)

class details:
    def __init__(self):
        self.name='santhi'
        self.age=21
        self.edu='B.Tech'
        self.role='Menter'
person=details()
print(person.name)
print(person.age)
print(person.edu)
print(person.role)

class Bank:
    def __init__(self):
        self.name='santhi'
        self.acc=12345432
        self.branch='vizag'
        self.adr='34376565432'
        self.numb=5432234123
        
per_d=Bank()
print(per_d.name)
print(per_d.acc)
print(per_d.branch)
print(per_d.adr)
print(per_d.numb)


4. methods
----------
--> Methods is a function that is created inside the class
syntax
------
class(keyword) name:
    #attributes
    def fun_name(self):
        #code
obj=class_name()
print(obj.fun_name())

eg--
class student:
    def __init__(self):
        self.name='santhi'
        self.age=21
        self.course='PFS'
    def all_data(self): 
        print(self.name)
        print(self.age)
        print(self.course)
    def st_name(self):
        print(self.name)
stu=student()
stu.st_name()
stu.all_data()

class car:
    def __init__(self):
        self.color='Blue'
        self.seat=6
        self.brand='BMW'
    def brake_(self):
        print(f'{self.brand} brake will apply at speed 250KM')
    def accelator(self):
        print(f'{self.brand} will take 2 sec to reach 180 speed')
    def clucth(self):
        print(f'{self.brand} with {self.seat} No automatic')

    
c1=car()
c1.brake_()
c1.accelator()
c1.clucth()

class student:
    def __init__(self, name, age, batch):
        self.name=name
        self.age=age
        self.batch=batch
    def all_data(self): 
        print(self.name)
        print(self.age)
        print(self.batch)
        
stu1=student('santhi', 21, 5)
stu1.all_data()

stu2=student('harshi' , 22, 15)
stu2.all_data()


class registration:
    def __init__(self, name, age, pan, adhr, email):
        self.name=name
        self.age=age
        self.pan=pan
        self.adhr=adhr
        self.email=email
    def all_data(self): 
        print(self.name)
        print(self.age)
        print(self.pan)
        print(self.adhr)
        print(self.email)

        
form1=registration('santhi', 21, 234543212345, 23454321345, 'kollusanthi95@gmail.com')
form1.all_data()

form2=registration('siri', 22, 345431234, 3456787654, 'siri12@gmail.com')
form2.all_data()



class calculator:
    def __init__(self, num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        print(self.num1+self.num2)
    def sub(self):
        print(self.num1-self.num2)
    def mul(self):
        print(self.num1*self.num2)
    def div(self):
        print(self.num1/self.num2)
cal=calculator(10,5)
cal.add()
cal.sub()
cal.mul()
cal.div()


class Book:
    def __init__(self,title,author,year):
        self.title=title
        self.author=author
        self.year=year
    def book1(self):
        print(self.title)
        print(self.author)
        print(self.year)
b=Book('pride and prejudice', 'jane austen', 1984)
b.book1()
b1=Book('Gitanjali','Rabindranath Tagore', 1910)
b1.book1()

'''

class Book:
    def __init__(self,title,author,year):
        self.title=title
        self.author=author
        self.year=year
    def book1(self):
        print(self.title)
        print(self.author)
        print(self.year)
b=Book('pride and prejudice', 'jane austen', 1984)
b.book1()
b1=Book('Gitanjali','Rabindranath Tagore', 1910)
b1.book1()
















