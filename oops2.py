class Person:
    __name="anonymous"
    def __hello(self):
        print("hello person!")
    def welcome(self):
        self.__hello()
p1=Person()
print(p1.welcome())

#inheritance
#single
class Car:
   # @staticmethod
    def start(self):
        print("Car started....")
   # @staticmethod
    def stop():
        print("Car stopped...")
class Toyota(Car):
    def __init__(self,name):
        self.name=name
car1=Toyota("fortuner")
print(car1.name)
print(car1.start())
#multi level
class Car:
    @staticmethod
    def start():
        print("Car started....")
    @staticmethod
    def stop():
        print("Car stopped...")
class Toyota(Car):
    def __init__(self,brand):
        self.brand=brand
class Fortuner(Toyota):
    def __init__(self, type):
        self.type=type
car1=Fortuner("disel")
print(car1.type)
car1.start()
#multiple level
class A:
    varA="welcome to class A"
class B:
    varB="welcome to class B"
class C(A,B):
    varC="welcome to class C"
c1=C()
print(c1.varC)
print(c1.varA)
print(c1.varB)

#super method-used to accces methods of parent class
class Car:
    def __init__(self,type):
        self.type=type
    @staticmethod
    def start():
        print("Car started....")
    @staticmethod
    def stop():
        print("Car stopped...")
class Toyota(Car):
    def __init__(self,name,type):
        self.brand=name
        #self.type=type-it will be of toyota but we want of car so use below statement
        super().__init__(type)
        super().start()
car1=Toyota("fortuner","disel")
print(car1.type)


#polymorphism
#implicit overloading
print(1+2)#arithemetic
print("aditi"+"dhavale")#concatenate
print([1,2,3]+[4,5,6])#merge

#operator overloading
class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def showNumber(self):
        print(self.real,"i +",self.img,"j")
    #def add(self,num2):
     #   newReal =self.real+num2.real
      #  newImg=self.img+num2.img
       # return Complex(newReal,newImg)
#num1=Complex(1,3)
#num1.showNumber()
#num2=Complex(4,6)
#num2.showNumber()
#num3=num1.add(num2)
#num3.showNumber()
    def __sub__(self,num2): #dunder function
         newReal=self.real-num2.real
         newImg=self.img-num2.img
         return Complex(newReal,newImg)
num1=Complex(1,3)
num1.showNumber()
num2=Complex(4,6)
num2.showNumber()
num3=num1 - num2
num3.showNumber()

#define a circle class to create with radius r using constructor.define area()method of class which calculates area of circle.define perimeter
#() method of class which allows you to calculate perimeter of circle
class Circle:
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius **2
    def perimeter(self):
        return 2 * 3.14 * self.radius
c1=Circle(21)
print(c1.area())
print(c1.perimeter())
#define Employee class with attributes role,dept&salary.define showDetails()method.create an Engineer class that inherits prpperties
#from Employee & has additional atrributes:name&age
class Employee:
    def __init__(self,role,dept,salary):
        self.role = role
        self.dept = dept
        self.salary=salary
    def showDetails(self):
        print("role=", self.role)
        print("dept=",self.dept)
        print("salary=",self.salary)
class Engineer(Employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("Engineer","CSE","75,000")
eng1=Engineer("Aditi Dhavale",20)
eng1.showDetails()   
#create class Order which stores item&its price.use __gt__()to convey that
#order1>order2 if price of order1>price of order2
class Order:
    def __init__(self,item,price):
        self.item=item
        self.price=price
    def __gt__(self,odr2):
        return self.price>odr2.price
odr1=Order("chips",20)
odr2=Order("tea",10)
print(odr1>odr2)
