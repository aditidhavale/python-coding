#instance methods
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print("hi",self.name)
        print("Your marks are:",self.marks)
    def grade(self):
        if self.marks>=60:
            print("First grade")
        elif self.marks>=50:
            print("Second grade")
        elif self.marks>=35:
            print("Third grade")
        else:
            print("Failed")
n=int(input("Enter number of students:"))
for i in range(n):
    name=input("Enter name:")
    marks=int(input("Enter marks:"))
    s=Student(name,marks)
    s.display()
    s.grade()
    print()

#setter & getter method
class Student:
    def setName(self,name):
        self.Name=name
    def getName(self):
        return self.Name
    def setMarks(self,marks):
        self.marks=marks
    def getMarks(self):
        return self.marks
n=int(input("Enter number of students:"))
for i in range(n):
    s=Student()
    name=input("Enter name:")
    s.setName(name)
    marks=int(input("Enter marks:"))
    s.setMarks(marks)
    print()

#class methods
class Animal:
    legs=4
    @classmethod
    def walk(cls,name):
        print("{} walks with legs...".format(name,cls.legs))
Animal.walk("dog")
Animal.walk("cat")

#static method
class Math:
    @staticmethod
    def add(x,y):
        print("the sum:",x+y)
    @staticmethod
    def sub(x,y):
        print("the difference:",x-y)
    @staticmethod
    def avg(x,y):
        print("the average is:",(x+y)/2)
Math.add(10,20)
Math.sub(30,40)
Math.avg(50,60)

#passing members of one class to another class
#we can access members of one class inside another class
class Employee:
    def __init__(self,eno,ename,esal):
        self.eno=eno
        self.ename=ename
        self.esal=esal
    def display(self):
        print("Employee number:",self.eno)
        print("Employee name:",self.ename)
        print("Employee Salary",self.esal)
class Test:
    def modify(emp):
        emp.esal=emp.esal+10000
        emp.display()
e=Employee(100,"Aditi",10000)
Test.modify(e)

#inner classes
class Outer:
    def __init__(self):
        print("outer class object creation")
    class inner:
        def __init__(self):
            print("inner class object creation")
        def m1(self):
            print("inner class method")
o=Outer()
i=o.inner()
i.m1()