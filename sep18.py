'''
OOP --> Object Oriented Programming --> objects
POP --> Procedure Oriented Programming --> Functions

#chair(object) --> Wood (Material), Design (Dimension), Person

A class is a blueprint of a object

A object is a real world entity which contains --> Attributes(variables) --> Methods(Functions)

class keyword

flipkart --> products --> laptop, mobiles, gadgets...

Features --> Encapsulation, Inheritance, Polymorphism
#function --> house
#class --. power house

class ClassName:
    """docstring"""
    #attributes (define the data)
    .....
    .....
    def fname(self): #behaviour
    def __init__(self):
        statement(s)...
        ...........

obj=ClassName()


#Students -->name, age
class Students:
    """Students details"""
    name='Santhi'
    age=20
    place='vizag'

    def details(self):
        print(f'{self.name} is in {self.place} and age os {self.age} years')

#Creatioln of objects
st1=Students()
print(st1)
print(dir(st1))
print(st1.name,st1.age,st1.place)
#print(st1.details()) --> TypeError
#print(st1.details()) ---> NameError as we have thrown self but no reference
#now we pass the reference
st1.details()
st2=Students()
st2.details()

#In above case how many objects you create the result will be same


class Students:
    """Student details for multiple students"""
    def details(self, name, age, place):
        self.name=name
        self.age=age
        self.place=place
    #now to access those details
    def display(self):
        print(f'Student name is {self.name}')
        print(f'Student age is {self.age} and lives in {self.place}')
        
st1=Students()
st1.details('Santhi', 21, 'vizag')
print(st1.name, st1.place)
st1.display()
print(st1.__class__)
print(st1.__doc__)
print(st1.__dict__)

st2=Students()
st2.details('Sara', 23, 'Kakinada')
st2.display()


#In this case we want object to be initialized --> __init__()
class Students:
    """Student details for multiple students"""
    def __init__(self, name, age, place): #constructor
        #instance variables or public variables
        self.name=name
        self.age=age
        self.place=place
    #now to access those details
    def display(self): #instance method
        print(f'Student name is {self.name}')
        print(f'Student age is {self.age} and lives in {self.place}')
st1=Students('Santhi', 21, 'vizag')
st1.display()
print(st1.__dict__)
st2=Students('Sara',23,'kakinada')
st2.display()
print(st2.__dict__)



#Create a Cars class with attributes as brand, name, price
#create multiple objects
class Cars:
    """Car details"""
    def __init__(self, brand, name, price):
        self.brand=brand
        self.name=name
        self.price=price
    def display(self):
        print(f'{self.name} is {self.brand} brand and price is {self.price}')
c1=Cars('TATA', 'benz',800000)
c1.display()
print(c1.__dict__)

#Encapsulation --> How the methods and attributes are binded to single
#class, in similar way how we can access the data --> Public, Protected, Private
                                                                                                                                                                            
#Public Attributes --> can be created and modified even outside the class

class Users:
    """Usage of Public attributes"""
    def __init__(self, username):
        self.user=username #Public attribute
    def display(self):
        print(f'Username is {self.user}')
u1=Users('Santhi')
print(u1.user)
u1.user='sara' #we can modify the public attribute
print(u1.user)
u1.display()


#Protected Attribute --> These can also be modified outside the class, its mainly useful as a hint/coding convention for other users/developers
#to create a protected attribute we use underscore --> _otp

class Users:
    """Usage of Protected attributes"""
    def __init__(self, username,_otp):
        self.user=username #Public attribute
        self._otp=_otp #Protected Attribute
    def display(self):
        print(f'Username is {self.user}')
        print(f'OTP is {self._otp}')
u1=Users('Santhi',5318)
u1.display()
u1._otp=1234 #we can modify the protected attribute
u1.display()


#Private Atribute --> restrict the usage and cannnot be directly accessed
#we have the usage or notation as double leading underscore --> __password

class Users:
    """Usage of Private attributes"""
    def __init__(self, username,_otp,__password):
        self.user=username #Public attribute
        self._otp=_otp #Protected Attribute
        self.__password=__password #Private attribute
    def display(self):
        print(f'Username is {self.user}')
        print(f'OTP is {self._otp}')
        print(f'Password {self.__password}')
u1=Users('Santhi',5318,'santhi@17')
print(u1.user,u1._otp)
u1.display()
print(u1.__dict__)
#print(u1.__password) password can't be accessed directly --> NameMangling
print(u1._Users__password)

'''
#Usage of getter(), setter() methods

class Users:
    """Usage of attributes"""
    def __init__(self, username,_otp,__password):
        self.user=username #Public attribute
        self._otp=_otp #Protected Attribute
        self.__password=__password #Private attribute
    #Usage of getter() or get() method for password
    def get_password(self):
        """Getter method for password"""
        #return "******"
        return self.__password
    #Usage of setter() to modify the data
    def set_password(self, new_password):
        if len(new_password)<6:
            return 'Password lenght is not matching'
        else:
            self.__password=new_password
            return 'Updated password'
    
u1=Users("Admin",5423,"santhi17")
print(u1.get_password())
print(u1.set_password("admin")) #you are not satisfied password requirements
print(u1.set_password('admin123')) #in this case satisfied
print(u1.get_password())
print(u1.__dict__)






























