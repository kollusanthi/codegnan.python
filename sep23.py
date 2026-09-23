'''
Polymorphism --> Method Overloading, Method overriding, operator overloading

Method overloading  --> Default arguments, variable length arguments, Types of arguments


#method overloading (Compile time polymorphism) --> Default arguments

class Hotstar:
    """default args usage"""
    def watch(self, movie=None):
        self.movie=movie
        if self.movie==None:
            print(f'Welcome to Hotstar')
        elif self.movie==movie:
            print(f'User watching {self.movie}')
u1=Hotstar()
u1.watch() #in this case we made movie as default
u1.watch("Hi Nanna")


#Method overloading with variable length arguments
#scenario of adding movies to watchlist
class Hotstar:
    """*args args usage"""
    def watch(self, movie=None):
        print(f'Welcome to Hotstar')
    def add_tolist(self, *movies):
        print(movies)
        for movie in movies:
            print(movie)
u1=Hotstar()
u1.add_tolist("Sita Ramam", "Happy", "Lenin", "SVSC", "Hi Nanna", "Bhahubali", "Save the Tigers")
u1.watch()


#Method overloading with type of arguments(isinstance())
#Hotstar --> one movie, multiple movies
#isinstance is a keyword used to check the datatype of the object

class Hotstar:
    """Usage of type of args"""
    def watch(self, movie=None):
        print(f'Welcome to Hotstar')
    def movies_list(self, content):
        if isinstance(content, str):
            self.content=content
            print(f'User watching {self.content}')
        elif isinstance(content, list):
            print(content)
            for movie in content:
                print(movie)
        #elif isinstance(content, tuple):
            #print(content)
            #for movie in content:
                #print(movie)
                
u1=Hotstar()
u1.watch()
u2=Hotstar()
u2.movies_list('Sita Ramam')
u2.movies_list(['Leo','Vikram','BlackPanther'])
#print(movies_list(("Sita Ramam", "Happy", "Lenin", "SVSC", "Hi Nanna", "Bhahubali", "Save the Tigers")))
print(u2.movies_list(("Sita Ramam", "Happy", "Lenin", "SVSC", "Hi Nanna", "Bhahubali", "Save the Tigers")))


#Method Overriding --> Inheritance usage
#when the same method name is used in base class and also in derived class
#super()
#Free user --> [Can watch free content with advertisements]
#Premium User --> [Can watch premium content without advertisements]
#VIP User --> [Can watch premium along with devices count, streaming]
class Hotstar:
    """Usage of Overring"""
    def watch(self):
        print('Welcome to Hotstar')
class free_user(Hotstar):
    """Free users class with advertisements"""
    def watch(self):
        super().watch()
        print('This is a free user method')
class premium_user(free_user):
    """Premium Content"""
    def watch(self):
        super().watch()
        print('This is a premium user method')
class VIP_user(premium_user):
    """Live Content"""
    def watch(self):
        super().watch()
        print('This is a vip user method')

u1=Hotstar()   
u1.watch()
u2=free_user()
u2.watch()
u3=premium_user()
u3.watch()
u4=VIP_user()
u4.watch()
        

#Operator Overloading --> (Magic methods/dunder methods) __init__(), __add__(),...

a=13;b=24
print(a<b)
print(a.__le__(b)) #lessthan or equal to
print(a+b)
print(a.__add__(b)) #self.value+other.value
print('codegnan'.__add__('Python')) #concatenation
print([1,3,4,].__add__([2,3,9,5])) #Merging

#in above case same __add__() is performing different cases(Addition, concatenation, merging)

a=[1,2,3,4,5]
print(a.__len__()) #len(a)


#now linking above operators scenario to Hotstar
class WatchHistory:
    """Duration of watching content"""
    def duration(self, hours):
        self.hours=hours
    #def __add__(self, other):
        #return self.hours+other.hours
u1=WatchHistory()
u1.duration(25)
u2=WatchHistory()
u2.duration(35)
print(u1.hours+u2.hours)
#get the complete duration
#print(u1+u2) #this is directly accessible when we have __add__()
'''

class WatchHistory:
    """Duration of watching content"""
    def duration(self, hours):
        self.hours=hours
    def __add__(self, other):
        return self.hours+other.hours
    def __str__(self):
        print(f'USer watching {self.hours} hours duration')
u1=WatchHistory()
u1.duration(25)
u2=WatchHistory()
u2.duration(35)
print(u1+u2)
u1.__str__()
u2.__str__()


















