#conditional statements
#if
name=input("Enter name=")
if name=="Aditi":
    print("Hello Aditi , gm")
print("How are you")

#if-else
name=input("Enter name=")
if name=="Aditi":
    print("Hello Aditi , gm")
else:
    print("Hello guest , gm")
print("How are you")

#if-elif-else
brand=input("enter your fav band=")
if brand=="RC":
    print("children brand")
elif brand=="KF":
    print("not so good")
elif brand=="FO":
    print("Buy one get one free")
else:
    print("no brand are recommended")


#iterative statement
#for loop
s=input("enter the string =")
i=0
for x in s:
    print("character present at",i,"index is =",x)
    i=i+1

#while loop
x=1
while x<=10:
    print(x)
    x=x+1


#transfer statement
#break
for i in range(10):
    if i==7:
        print("processing is enough...plz break")
        break
    print(i)

#continue(print odd no from range 0 to 9)
for i in range(10):
    if i%2==0:
        continue
    print(i)