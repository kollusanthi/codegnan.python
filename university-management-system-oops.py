from abc import ABC, abstractmethod


class University:
    def __init__(self):
        self.students = []
        self.courses = []

    def add_student(self, student):
        self.students.append(student)

    def add_course(self, course):
        self.courses.append(course)


class Student(ABC):
    def __init__(self, name):
        self.name = name
        self.courses = []

    @abstractmethod
    def enroll(self, course):
        pass

    def grades(self, grade):
        print(self.name, "Grade:", grade)


class Undergraduate(Student):
    def enroll(self, course):
        self.courses.append(course)
        print(self.name, "enrolled in", course)

    def schedule(self):
        print("Undergraduate Schedule")


class Graduate(Student):
    def enroll(self, course):
        self.courses.append(course)
        print(self.name, "enrolled in", course)

    def schedule(self):
        print("Graduate Schedule")


class Faculty:
    def __init__(self, name):
        self.name = name

    def assign_course(self, course):
        print(self.name, "assigned to", course)


u = University()

s1 = Undergraduate("Santhi")
s2 = Graduate("Ramu")
f1 = Faculty("Kumar")

u.add_student(s1)
u.add_student(s2)
u.add_course("Python")

s1.enroll("Python")
s2.enroll("Python")

f1.assign_course("Python")

s1.schedule()
s2.schedule()
s1.grades("A")
