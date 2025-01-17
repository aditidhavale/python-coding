#instance variable
#declare
#1.inside constructor using self variable
class Employee:
    def __init__(self):
        self.eno=100
        self.ename="Aditi"
        self.esal=100000
e=Employee()
print(e.__dict__)

class Test:
    def __init__(self):
        self.a=10
        self.b=20
    def m1(self):
        self.c=30#2.inside instance method using self variable
t=Test()
t.m1()
t.d=40#3.outside class using object reference variable
print(t.__dict__)

#access
class Test:
    def __init__(self):
        self.a=10
        self.b=20
    def display(self):
        print(self.a)
        print(self.b)#1.inside class using self 
t=Test()
t.display()
t.d=40
print(t.a,t.b)#2.outside class using object reference

#delete
class Test:
    def __init__(self):
        self.a=10
        self.b=20
        self.c=30
        self.d=40
    def m1(self):
        del self.d#1.inside class 
t=Test()
print(t.__dict__)
t.m1()
print(t.__dict__)
del t.c
print(t.__dict__)#2.outside class

#instace varible deleted in first object will not be deleted in another object
class Test:
    def __init__(self):
        self.a=10
        self.b=20
        self.c=30
        self.d=40
t1=Test()
t2=Test()
del t1.a
print(t1.__dict__)
print(t2.__dict__)

#values changed of instance variable will not be reflected in another object
class Test:
    def __init__(self):
        self.a=10
        self.b=20
t1=Test()
t1.a=888
t1.b=999
t2=Test()
print("t1:",t1.a,t1.b)
print("t2:",t2.a,t2.b)


#static variable
#declare
class Test:
    a=10#within class & outside method
    def __init__(self):
        Test.b=20#in constructor using class name
    def m1(self):
        Test.c=30#3.in instace method using class name
    @classmethod
    def m2(cls):
        cls.d1=40
        Test.d2=400#4.in class method using cls variable or class name
    @staticmethod
    def m3():
        Test.e=50#5.in static method using class name
print(Test.__dict__)
t=Test()
print(Test.__dict__)
t.m1()
print(Test.__dict__)
t.m2()
print(Test.__dict__)
t.m3()
print(Test.__dict__)
Test.f=60
print(Test.__dict__)

#access
class Test:
    a=10
    def __init__(self):
        print(self.a)
        print(Test.a)#in constructor using self or class name
    def m1(self):
        print(self.a)
        print(Test.a)#in instace method using self or class name
    @classmethod
    def m2(cls):
        print(cls.a)
        print(Test.a)#in class method using cls variable or class name
    @staticmethod
    def m3():
        print(Test.a)#in static method using class name
t=Test()
print(Test.a)
print(t.a)#outside using object refereence or class name
t.m1()
t.m2()
t.m3()

#modify value of static variable
class Test:
    a=77
    @classmethod
    def m1(cls):
        cls.a=88
    @staticmethod
    def m2():
        Test.a=99
print(Test.a)
Test.m1()
print(Test.a)
Test.m2()
print(Test.a)

#delete
class Test:
    a=10
    @classmethod
    def m1(cls):
        del cls.a
Test.m1()
print(Test.__dict__)


#local variable
class Test:
    def m1(self):
        a=1000
        print(a)
    def m2(self):
        b=2000
        print(b)
t=Test()
t.m1()
t.m2()