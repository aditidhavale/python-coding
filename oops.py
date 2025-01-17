class Student:
    name="aditi"
s1=Student()
print(s1.name)
s2=Student()
print(s2.name)

class Car:
    color="black"
    brand="mercedes"
c=Car()
print(c.color)
print(c.brand)

class Student:
    college_name="JJMCOE"#class attribute
    def __init__(self,name,rollno,marks):
        self.name=name#object attribute
        self.rollno=rollno
        self.marks=marks
    def talk(self):
        print("Hello my name is:",self.name)
        print("My rollno:",self.rollno)
        print("My marks are :",self.marks)
s1=Student("Aditi",101,80)
s1.talk()

class Student:
    def __init__(self,x,y,z):
        self.name=x
        self.rollno=y
        self.marks=z
    def display(self):
        print("Student Name:{}\nRollNo:{}\nMarks:{}".format(self.name,self.rollno,self.marks))
s1=Student("Aditi",101,80)
s1.display()
s2=Student("Apurva",102,100)
s2.display()


#create class student that takes name marks of 3 subjects as arguments in constructor.then create method to print average
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def get_avg(self):
        sum=0
        for val in self.marks:
            sum += val
        print("hi",self.name,"your avg score is:",sum/3)
s1=Student("aditi dhavale",[99,98,97])
s1.get_avg