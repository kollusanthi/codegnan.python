'''

Inheritance
-----------
--> Inheritance is the process of inherite one class into another class
--> will general inherite from a class is called parent class and using it in another that class is called child class
eg--
class company:
    def salary(self):
        print('Comapny salary')
class employee(company):
    def mon_sal(self):
        print('Employee salary')
per_sal=employee()
per_sal.mon_sal()
per_sal.salary()

Types
-----
1.single inheritance
--------------------
--> If one child class inherite from one parent class this is called single inheritance
eg--
class father:
    def land(self):
        print('5 acers of land')
class me(father):
    def flat(self):
        print('6 flats')
all_=me()
all_.flat()
all_.land()

2.multiple inheritance
----------------------
--> If one child inherite from more then one parent class this is called multiple inheritance
eg--
class father:
    def home(self):
        print('Home at village')
class mother:
    def gold(self):
        print('50kg gold')
class son(father, mother):
    def flat(self):
        print('sons flat')
all_to=son()
all_to.home()
all_to.gold()
all_to.flat()

3.multi-level inheritance
-------------------------
--> one child class become parent class to the another class is called multi-level inheritance

eg--
class grandfather:
    def land(self):
        print('Grandfather land')
class father(grandfather):
    def flat(self):
        print('Father flat')
class son(father):
    def car(self):
        print('sons car')
fam=son()
fam.land()
fam.land()
fam.car()

4.Hierarchical inheritance
--------------------------
--> If two child class inherite from one parent class is called as Hierarchical inheritance
eg--
class father:
    def land(self):
        print('50 acer land')
class son_1(father):
    def flat(self):
        print('First Son flat')
class son_2(father):
    def car(self):
        print('Second son car')

s1=son_1()
s1.land()
s1.flat()

s2=son_2()
s2.land()
s2.car()


5.Hybrid inheritance
---------------------
--> inherite from more than two types into one class is called as hybrid inheritance
eg--
class person:
    def name(self):
        print('Santhi is her name')
class student(person):
    def study(self):
        print('B.Tech final year')

class py_teacher:
    def teach(self):
        print('Python')
class java_teacher:
    def teac(self):
        print('Java')
class learner(py_teacher, java_teacher):
    def learn(self):
        print('Learner')

class all_get(student, learner):
    def get_it(self):
        print('This person getting all data')

an=all_get()
an.name()
an.study()
an.teach()
an.teac()
an.learn()
an.get_it()
        



practice
--------
eg-- single inheritance
class reporter:
    def question(self):
        print('what is your age')
class person(reporter):
    def answer(self):
        print(22)
r1=person()
r1.question()
r1.answer()

eg-- mutiple inheritance
class reporter1:
    def question1(self):
        print('what is your age')
class reporter2:
    def question2(self):
        print('What is your Qualification')
class person(reporter1, reporter2):
    def answer1(self):
        print(22)
    def answer2(self):
        print('B.Tech')
r1=person()
r1.question1()
r1.answer1()
r1.question2()
r1.answer2()

'''


        


















        
