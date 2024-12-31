#access string item
#1.using index
s="aditi"
print(s[2])#we can access all the letters using index ,if we give index<4 it is error
#2.slice
s="aditi"
print(s[1:4:1])

#mathematical operators
print("aditi"+"ganesh"+"dhavale")#concatenation(both arguments should be string)
print("aditi"*2)#repetition(one should be str & other should be int)
print(len("aditi"))

#check membership(in & not in operators)
print("d"in "aditi")
print("z" in "aditi")
print("z"not in "aditi")

#comparison
s1=input("enter s1 string=")
s2=input("enter s2 string=")
if s1==s2:
    print("both are equal")
elif s1<s2:
    print("s2 is greater")
else:
    print("s1 is greater")

#finding substring(1-find() 2-rfind() 3-index() 4-rindex())
s="aditi"
print(s.find("d"))
print(s.find("z"))#returns -1 if not find
print(s.rfind("i"))#from reverse
s="adiappuaaradhya"
print(s.find("a",11,15))
s="aditi"
print(s.index("a"))
#print(s.index("z"))#gives error if not found
print(s.rindex("i"))

#counting sub string in given string
s="abcabcabcabcadda"
print(s.count("a"))
print(s.count("ab"))
print(s.count("a",3,7))


#replacing string
s="learning python is difficult"
s1=s.replace("difficult","easy")
print(s1)
s="abcabcabcabcadda"
s1=s.replace("a","e")
print(s1)


#splitting
s="aditi ganesh dhavale"
l=s.split()
for x in l:
    print(x)
s="28-12-2024"
l=s.split("-")
for x in l:
    print(x)


#joining
t=("adi","appu","aara")
s="-".join(t)
print(s)

#changing case
s="learning Python is very Easy"
print(s.upper())
print(s.lower())
print(s.swapcase())
print(s.title())#1st letter of every word capital
print(s.capitalize())#only 1st letter capitaladi

#checking starting and ending
s="learning Python is very Easy"
print(s.startswith("learning"))
print(s.startswith("easy"))
print(s.endswith("Easy"))


#check type of characters
#isalnum()=true if (atoz,AtoZ,0-9)
#isalpha()=true if (atoz,AtoZ)
#isdigit()=true if(0-9)
#islower()=true if lowercase
#isupper()=true if uppercase
#istitle()=true if title
#isspace()=true if only spaces