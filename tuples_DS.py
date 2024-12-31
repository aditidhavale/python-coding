#creation
t=()
t=(10,)#single valued
t=(10,20,30)
list=[1,2,3]
t=tuple(list)
print(t)

#accessing
#1using index
t=(1,2,3,4,5)
print(t[0])
print(t[-1])
#2.using slice operator
t=(1,2,3,4)
print(t[1:3])
print(t[2:100])
print(t[::2])

#mathematical operators
#concatenation
t1=(1,2,3,4)
t2=(5,6,7,8)
t3=t1+t2
print(t3)
#repetition
t=(1,2,3)
s=t*3
print(s)

#imp functions
#len
t=(1,2,3,4,5)
print(len(t))
#count
t=(1,1,2,2,2,2,3,3,3,3,3,)
print(t.count(1))
print(t.count(2))
print(t.count(3))
#index
t=(1,2,3,4,6)
print(t.index(3))
#print(t.index(8))-error
#sorted
t=(4,8,3,7,1)
t1=sorted(t)
print(t)
print(t1)
#min-max
t=(2,4,1,8)
print(min(t))
print(max(t))
#packing&unpacking
a=1
b=2
c=3
t=a,b,c
print(t)
#unpacking
t=(1,2,3,4)
a,b,c,d=t
print("a=",a,"b=",b,"c=",c,"d=",d)