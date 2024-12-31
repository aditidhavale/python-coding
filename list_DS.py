l=list(range(0,10,2))
print(l)

s="durga"
l=list(s)
print(l)

s="Learning python is very easy"
l=s.split()
print(l)

#accessing elements
#1.using index
list=[10,20,30,40]
print(list[0])
print(list[-1])
#2.using slice operator
n=[1,2,3,4,5,6,7,8,9,10]
print(n[2:7:2])
print(n[4::2])

#traversing element
#1.while loop
n=[1,2,3,4,5,6,7,8,9,10]
i=0
while i<len(n):
    print(n[i])
    i=i+1
#2.for loop
n=[1,2,3,4,5,]
for n1 in n:
    print(n1)
#3.display even numbers
n=[1,2,3,4,5]
for n1 in n:
    if n1%2==0:
        print(n1)
#4.display elements index wise
l=["a","b","c"]
x=len(l)
for i in range(x):
    print(l[i],"is at +ve index:",i,"and at -ve index:",i-x)


#IMP functions
#1.get info
n=[1,2,3,4,5]
print(len(n))

n=[1,2,2,2,2,3,3]
print(n.count(1))
print(n.count(2))
print(n.count(3))
print(n.count(4))

n=[1,2,2,2,2,3,3]
print(n.index(1))
print(n.index(2))
print(n.index(3))
#print(n.index(4))=>error

#manipulation of elements
#1.append()-end of list
list=[]
for i in range(101):
    if i%10==0:
        list.append(i)
print(list)
#2.insert()-at specific position
n=[1,2,3,4,5]
n.insert(1,888)
print(n)
#3.extend()-add elements of one list to other list
order1=["chicken","mutton","fish"]
order2=["RC","KF","FO"]
order1.extend(order2)
print(order1)
#4.remove()
n=[10,20,10,40]
n.remove(10)#if element repeat then only 1st occurence removed
#n.remove(40)-gives error ,as not in list
print(n)
#5.pop()
n=[10,20,30,40]
print(n.pop())
print(n.pop())
print(n)


#ordering elements
#1.reverse()
n=[1,2,3,4,5]
n.reverse()
print(n)
#2.sort()-to use this all elements in list should be homogeneous 
n=[5,9,2,10,1]#default ascending
n.sort()
print(n)
n=["rohini","aditi","ganesh"]#default alphabetical
n.sort()
print(n)

#aliasing & cloning
x=[10,20,30,40]
y=x
print(id(x))
print(id(y))

x=[10,20,30,40]
y=x
y[1]=77
print(x)
#cloning
#1.slice
x=[10,20,30,40]
y=x[:]
y[1]=77
print(x)
print(y)
#2.copy()
x=[10,20,30,40]
y=x.copy()
y[1]=77
print(x)
print(y)

#mathematical operators
#1.concatenation(both should be only list type , no other)
a=[1,2,3]
b=[4,5,6]
c=a+b
print(c)
#2.repetition
x=[1,2,3]
y=x*2
print(y)

#comparing
x=["Dog","Cat","Rat"]
y=["Dog","Cat","Rat"]
z=["DOG","CAT","RAT"]
print(x==y)
print(x==z)
print(x!=z)

x=[50,20,30]
y=[40,50,60,100,200]
print(x>y)
print(x>=y)
print(x<y)
print(x<=y)

x=["Dog","Cat","Rat"]
y=["Rat","Cat","Dog"]
print(x>y)
print(x>=y)
print(x<y)
print(x<=y)

#membership
n=[10,20,30,40]
print(10 in n )
print(10 not in n )
print(50 in n )
print(50 not in n )

#clear()
n=[10,20,30,40]
print(n)
n.clear()
print(n)

#nesting of list
n=[10,20,[30,40]]
print(n)
print(n[0])
print(n[2])
print(n[2][0])
print(n[2][1])

#list comprehension
s=[x*x for x in range(1,11)]
print(s)
v=[2*x for x in range(1,6)]
print(v)
m=[x for x in s if x%2==0]
print(m)

words=["Aditi","Ganesh","Dhavale"]
l=[w[0]for w in words]
print(l)

words="aditi ganesh dhavale".split()
print(words)
l=[[w.upper(),len(w)] for w in words]
print(l)