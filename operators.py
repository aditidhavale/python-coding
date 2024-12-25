#arithmetic operators
a=10
b=2
print("a+b=",a+b)#add
print("a-b=",a-b)#subtract
print("a*b=",a*b)#mult
print("a/b=",a/b)#div -always return float
print("a%b=",a%b)#modulo give remainder ans
print("a//b=",a//b)#floor div-if numbers are int then return int , float then float
print("a**b=",a**b)#exponent

#to use + for string both arguments should be string
x="durga"
y="10"
print("x+y=",x+y)#string concantenate
#to use * for string compulsory one argument should be int & other string
x=2
y="aditi"
print("x*y=",x*y)#string multiply

#relational operators
a=10
b=20
print("a>b is",a>b)
print("a>=b is",a>=b)
print("a<b is",a<b)
print("a<=b is",a<=b)

a="aditi"
b="aditi"
print("a>b is",a>b)
print("a>=b is",a>=b)
print("a<b is",a<b)
print("a<=b is",a<=b)

#logical,bitwise,shift,assignment operators

#ternary operators
#syntax=>x=firstValue if condition else second value
a=int(input("Enter first value="))
b=int(input("Enter second value="))
min=a if a<b else b
print("Min value is",min)

a=int(input("Enter first value="))
b=int(input("Enter second value="))
c=int(input("Enter  third value="))
min=a if a<b and a<c else b if b<c else c
print("Min value is",min)

#identityoperators,membership operators,operator precedance
