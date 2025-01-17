def wish():
    print("Hello GM")
wish()
wish()

#parameters
def wish(name):
    print("Hello",name,"GM")
wish("Aditi")
wish("Appu")
def square(number):
    print("Square of",number,"is",number*number)
square(4)
square(5)

#return stat
def add(x,y):
    return x+y
result=add(10,20)
print("the sum is",result)
print("the sum is",add(100,200))
#multiple values
def calc(a,b):
    sum=a+b
    sub=a-b
    mul=a*b
    div=a/b
    return sum,sub,mul,div
t=calc(100,50)
print("results are")
for i in t:
    print(i)

#types of argumrnts
#1.positional
def sub(a,b):
    print(a-b)
sub(100,200)
#2.keyword
def wish(name,msg):
    print("hello",name,msg)
wish(name="aditi",msg="GM")
wish(msg="GM",name="appu")
#3.default
def wish(name="aditi"):
    print("hey",name,"GM")
wish("Adi")
wish()
#4.variable length
def sum(*n):
    total=0
    for n1 in n:
        total=total+n1
    print("the sum=",total)
sum()
sum(10)
sum(10,20)
sum(10,20,30,40)


#types of variables
#1.global variable
a=10#global
def f1():
    print(a)

def f2():
    print(a)

f1()
f2()
#2.local variable
def f1():
    a=10
    print(a)
#def f2():
    #print(a) - invalid
f1()
#global keyword
a=10
def f1():
    a=777
    print(a)
def f2():
    print(a)
f1()
f2()

a=10
def f1():
    global a
    a=777
    print(a)
def  f2():
    print(a)
f1()
f2()


#recursive functions
def factorial(n):
    if n==0:
        result=1
    else:
        result=n*factorial(n-1)
    return result
print("factorial of 4 is:",factorial(4))
print("factorial of 5 is:",factorial(5))

#lambda function
s=lambda n:n*n
print("square of 4 is:",s(4))
print("square of 5 is :",s(5))

#filter function
#without lambda
def isEven(x):
    if x%2==0:
        return True
    else:
        return False
l=[0,5,10,15,20,25,30]
l1=list(filter(isEven,l))
print(l1)
#with lambda
l=[0,5,10,15,20,25,30]
l1=list(filter(lambda x:x%2==0,l))
print(l1)
l2=list(filter(lambda x:x%2!=0,l))
print(l2)


#map function
#without lambda
l=[1,2,3,4,5]
def double(x):
    return 2*x
l1=list(map(double,l))
print(l1)
#with lambda
l=[1,2,3,4,5]
l1=list(map(lambda x:2*x,l))
print(l1)

l=[1,2,3,4,5]
l1=list(map(lambda x:x*x,l))
print(l1)

l1=[1,2,3,4]
l2=[2,3,4,5]
l3=list(map(lambda x,y:x*y,l1,l2))
print(l3)

#reduce function
from functools import*
l=[10,20,30,40,50]
result=reduce(lambda x,y:x+y,l)
print(result)
result=reduce(lambda x,y:x*y,l)
print(result)
from functools import*
result=reduce(lambda x,y:x+y,range(1,101))
print(result)

#function aliasing
def wish(name):
    print("GM:",name)
greeting=wish
print(id(wish))
print(id(greeting))
greeting("Aditi")
wish("Aditi")

def wish(name):
    print("GM:",name)
greeting=wish
del wish
greeting("aaru")


#nesting functions
def outer():
    print("outer function started")
    def inner():
        print("inner function execution")
    print("outer function calling inner function")
    inner()
outer()

def outer():
    print("outer function started")
    def inner():
        print("inner function execution")
    print("outer function returning inner function")
    return inner
f1=outer()
f1()
f1()