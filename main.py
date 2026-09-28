from Employee1 import Employee1
from Person import Person
from Student import Student

def introduce(x):
    x.display()

e1 = Employee1("Abc","Pune",213212.12)
e2 = Employee1("Xyz","Pune",3243212.12)

p1 = Person("Aaa","Pune")

s1 = Student("ABC","Pune",211)
s2 = Student("XYZ","Pune",344)

introduce(e1)
introduce(e2)
introduce(p1)
introduce(s1)