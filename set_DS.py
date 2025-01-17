#creating
s={10,20,30,40}
print(s)

l=[1,2,3,4,5]
s=set(l)
print(s)

#Imp functions
#1.add(x)
s={1,2,3}
s.add(4)
print(s)
#2.update(x,y,z)
s={10,20,30}
l=[40,50,60,70]
s.update(l,range(5))
print(s)
#3.copy()
s={1,2,3}
s1=s.copy()
print(s1)
#4.pop()-remove random element
s={1,2,3,4,5}
print(s.pop())
print(s)
#5.remove-remove specified element& if element is not present then gives error
s={1,2,3,4,5}
s.remove(4)
#s.remove(8)
print(s)
#6.discard-remove specified element &if element is not present then does not give error
s={1,2,3,4,5}
s.discard(2)
#s.discard(8)-does not give error
print(s)
#clear-removes all elements
s={1,2,3}
s.clear()
print(s)

#mathematical operations
#1.union()
x={1,2,3,4,5}
y={6,7,8,9}
print(x.union(y))
#print(x|y)-gives same ans
#2.intersection
x={1,2,3,4,5}
y={4,5,6,7}
print(x.intersection(y))
#print(x&y)-gives same ans
#3.difference
x={1,2,3,4}
y={3,4,5,6}
print(x.difference(y))
#print(x-y)-gives same ans
print(y-x)
#4.symmetric difference
x={1,2,3,4}
y={3,4,5,6}
print(x.symmetric_difference(y))
#print(x^y)-gives same ans

#membership operator
s=set("aditi")
print(s)
print("d" in s)
print("z" in s)

#set comprehension
s={x*x for x in range(5)}
print(s)

s={2**x for x in range(2,10,2)}
print(s)