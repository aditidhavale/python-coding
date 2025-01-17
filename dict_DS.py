#creating
#1.empty
d={}
#d=dict()
#we can add items
d[1]="aditi"
d[2]="appu"
d[3]="aaru"
print(d)
#2.know elements
d={1:"adi",2:"appu",3:"aaru"}
print(d)

#accessing
d={1:"adi",2:"appu",3:"aaru"}
print(d[1])
print(d[3])
#if key is not present yhen we get error
#to check use->if 4 in d:
                  #print(d[4])



#update 
d={1:"adi",2:"appu",3:"aaru"}
d[4]="rohini"#if key is not present new pair will br addes to dict
print(d)
d[3]="ganesh"#if key is present old value is replaced
print(d)


#delete elements
#1.del d[key]
d={1:"adi",2:"appu",3:"aaru"}
del d[1]
print(d)
#del d[4]-error
#2.d.clear()
d={1:"adi",2:"appu",3:"aaru"}
d.clear()
print(d)
#del d
d={1:"adi",2:"appu",3:"aaru"}
#total dict is deleted


#imp func
#dict()-create dict
#len()
d={1:"adi",2:"appu",3:"aaru"}
print(len(d))
#clear()
#get()
d={1:"adi",2:"appu",3:"aaru"}
print(d[1])
#print(d[4])-error
print(d.get(1))
print(d.get(4))
print(d.get(1,"guest"))
print(d.get(4,"guest"))
#pop
d={1:"adi",2:"appu",3:"aaru"}
d.pop(1)#d.pop(4)-error
print(d)
#popitem()
d={1:"adi",2:"appu",3:"aaru"}
print(d.popitem())
print(d)
#keys
d={1:"adi",2:"appu",3:"aaru"}
print(d.keys())
for k in d.keys():
    print(k)
#values
d={1:"adi",2:"appu",3:"aaru"}
print(d.values())
for v in d.values():
    print(v)
#items
d={1:"adi",2:"appu",3:"aaru"}
for k,v in d.items():
    print(k,"--",v)
#copy()
#setdefault()
d={1:"adi",2:"appu",3:"aaru"}
print(d.setdefault(4,"ganesh"))#as not present it will be added
print(d)
print(d.setdefault(1,"rohini"))#as it is present corresponding value will be returned
print(d)
#update()

#dict comprehension
squares={x:x*x for x in range(1,6)}
print(squares)
doubles={x:2*x for x in range(1,6)}
print(doubles) 