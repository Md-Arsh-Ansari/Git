--------------------------------------------------------------------------------------------------------------
Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello 
--------------------------------------------------------------------------------------------------------------





print("Hello Python world!")

or 

show = "Hello Python world!"
print(show)


name = "mohammad arsh ansari"
print(name.title())

print(name.upper())

print(name.lower())



















first = "mohammad"
middle = "arsh"
last = "ansari"
name = f"{first} {middle} {last}" #YE f" wala cheez bina bracket ke bhi kaam karta hai.
                            #Aur ye { } middle bracket bina small bracket ke bhi dena hai
                            #small bracket ( ) yaha par kaam nahi karega.
print(name.title())


first = "mohammad"
middle = "arsh"
last = "ansari"
name = f"{first} {middle} {last}"
print(f"\nAre you {middle.upper()}! \n\nAnd your full name is {name.title()}!")


first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!"
print(message)


print("\tPython")

print('\n\t\tLists-\n\tFood\n\tGrossery\n\tMedicines')



#STRIP THE STRING USING .strip() method


name='    arsh    '
name
name.rstrip()
name.lstrip()
name.strip()


##Using .strip() method, strip the string so that, only "Babylon" remains.
str="#$^&#@%$& Babylon #@$&@#"
#Type your code here.

str= str.strip("#$^&#@%$& ")

print(str)
>>>>>>>>>>>>>>>>>>>>>>>.
Babylon


###Rstrip method to remove from the right side only

str="@Bloomberg@@@@@###"
#Type your code here.

str= str.rstrip("@#")
print(str)
>>>>>>>>>>>>>>>>>>>>>>>>>>>
@Bloomberg



###Using a combination of .split() and .lstrip() methods, get the word "Derivatives".
str="......Macroeconomics,...........Derivatives"
#Type your code here.

lst = str.split(",")
ans_1 = lst[1].lstrip(".")

print(ans_1)
>>>>>>>>>>>>>>>>>>>>>>>
Derivatives



#########DIR FUNCTION USING Python’s dir() function
#Type your answer here.
str="Hello World!"

print(dir(str))
>>>>>>>>>>>>>>>>>>>>>>>>>>>...
['__add__', '__contains__', '__eq__', '__ge__', '__getattr__', '__getitem__', '__gt__', '__hash__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__repr__', '__rmul__', '__setattr__', '__str__', 'capitalize', 'center', 'count', 'endswith', 'expandtabs', 'find', 'format', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isnumeric', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'upper', 'zfill']




#Now print the attributes and methods of a list.
lst=list()
print(dir(lst))
>>>>>>>>>>>>>>>>>>>>>.
['__add__', '__contains__', '__eq__', '__ge__', '__getattr__', '__getitem__', '__gt__', '__hash__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__repr__', '__rmul__', '__setattr__', '__str__', 'append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']




# print the attributes and methods of a dictionary?
dicty = {"name" : "John", "age" : 36}
print(dir(dicty))
>>>>>>>>>>>>>>>>>>>>>>>>>>.
['__cmp__', '__contains__', '__delitem__', '__eq__', '__ge__', '__getattr__', '__getitem__', '__gt__', '__hash__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__repr__', '__setattr__', '__setitem__', '__str__', 'clear', 'copy', 'dict_merge', 'fromkeys', 'get', 'has_key', 'items', 'iteritems', 'iterkeys', 'itervalues', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values', 'viewitems', 'viewkeys', 'viewvalues']




sentence='My father's name is Masqurul Haque.'
print(sentence)

sentence="My father's name is Masqurul Haque."
print(sentence)
#to isse ye pata chalta hai ki hamesha double quotes ka istemal karna hai errors ko avoid karne ke liye.





#This is a comment
#written in
#more than just one line
print("Hello, World!")


i               s equal to :

"""
This is a comment
written in
more than just one line
"""
print("Hello, World!")


----------------------------------------------------------------------------------------------------------

Variables Variables Variables Variables Variables Variables Variables Variables Variables 

-----------------------------------------------------------------------------------------------------------





x, y, z = "Orange", "Banana", "Cherry"  
print(x)                               # Many Values to Multiple Variables
print(y)
print(z)



x = y = z = "Orange"
print(x)                      #One Value to Multiple Variables
print(y)
print(z)




x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

OR

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

OR

x = "Python is awesome"
print(x)


These all were global variables.
    
    Global variables: Variables that are created outside of a function (as in all of the examples above) are known as global variables.


    #Create a variable outside of a function, and use it inside the function
x = "awesome"
def myfunc():
  print("Python is " + x)
myfunc()
>>>>>>>>>>>>>>>>>>>
Python is awesome


    #Create a variable inside a function, with the same name as the global variable
x = "awesome"
def myfunc():
  x = "fantastic"
  print("Python is " + x)
myfunc()
print("Python is " + x)

>>>>>>>>>>>>>>>>>>
Python is fantastic
Python is awesome



#If you use the "global" keyword, the variable belongs to the global scope:
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)


#To change the value of a global variable (which is "awesome" in this example) inside a function, refer to the variable by using the "global" keyword:

x = "awesome"
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)
>>>>>>
Python is fantastic



----------------------------------------------------------------------------------------------------------

Data Type    Data Type    Data Type    Data Type    Data Type    Data Type    
Data Type    Data Type    Data Type    Data Type    Data Type    Data Type     

------------------------------------------------------------------------------------------------------------




x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0


How to get the data type:

x = 5
y = "John"
z = 20.5
print(type(x))
print(type(y))
print(type(z))

>>>>>
<class 'int'>
<class 'str'>
<class 'float'>




x = "Hello World"	                                  str	
x = 20	                                              int	
x = 20.5	                                              float	
x = 1j	                                            complex	
x = ["apple", "banana", "cherry"]	                           list	
x = ("apple", "banana", "cherry")                       	tuple	
x = range(6)	                                        range	
x = {"name" : "John", "age" : 36}	                      dict	
x = {"apple", "banana", "cherry"}	                         set	
x = frozenset({"apple", "banana", "cherry"})	           frozenset	
x = True                                            	bool	
x = b"Hello"            	                            bytes	
x = bytearray(5)	                                    bytearray	
x = memoryview(bytes(5))	                            memoryview	


--------------------------------------------------------------------------------------------------------------
Python Numbers   Python Numbers   Python Numbers   Python Numbers   Python Numbers   
--------------------------------------------------------------------------------------------------------------



x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

>>>>>>>>>>>>>>>>>>>>>>>>>>>

<class 'int'>
<class 'int'>
<class 'int'>



x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))
>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<class 'float'>
<class 'float'>
<class 'float'>




#Float can also be scientific numbers with an "e" to indicate the power of 10.

x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))
>>>>>>>>>>>>>>>>>>>>>>>>>>>>
<class 'float'>
<class 'float'>
<class 'float'>


Complex numbers are written with a "j" as the imaginary part:
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
<class 'complex'>
<class 'complex'>
<class 'complex'>


# Number Convert from one type to another:
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

>>>>>>>>>>>>>>>>>>>>>
1.0
2
(1+0j)
<class 'float'>
<class 'int'>
<class 'complex'>








-------------------------------------------------------------------------------------------------------------- 

Strings Strings Strings Strings Strings Strings Strings Strings Strings Strings Strings Strings 

-------------------------------------------------------------------------------------------------------------- 

#You can assign a multiline string to a variable by using """three""" quotes:

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

OR

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)


#Get the character at position 0 and 1

a = "Hello, World!"
print(a[0])                    #Square brackets can be used to access elements of the string.
print(a[1])



#we can loop through the characters in a string, with a for loop.
for x in "banana":
  print(x)



#To get the length of a string, use the len() function.
a = "Hello, World!"
print(len(a))


#To check if a certain phrase or character is present in a string, we can use the keyword "in".
txt = "The best things in life are free!"
print("free" in txt)
>>>>>>>>>>>>>>>>>True

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")


#Using the keyword "not in".
txt = "The best things in life are free!"
print("expensive" not in txt)


txt = "The best things in life are free!"
if "tree" not in txt:
	print("No, 'tree' not in txt")




#Getting range by using the slice syntax.
b = "Hello, World!"
print(b[2:5])  #Get the characters from position 2 to position 5 but not include 5:




b = "Hello, World!"
print(b[:5])        ##Get the characters from the start to position 4



b = "Hello, World!"
print(b[-5:-2])                    ##It goes from right to left

###SLICE IN REVERSE ORDER:

lst=[0,1,2,3,4]
# Type your answer here.

ans_1 = lst[::-1]

print(ans_1)
>>>>>>>>>>>>>>>>>>
[4, 3, 2, 1, 0]





#The replace() method replaces a string with another string:
a = "Hello, World!"
print(a.replace("H", "J"))



##The split() method splits the string into substrings if it finds instances of the separator:

a = "Hello World , bnb cnbc abc!"
b = a.split(",")
print(b)
>>>>>>>>>>>
['Hello World ', ' bnb cnbc abc!']



a = "Hello World bnb cnbc abc!"
b = a.split(" ")
print(b)
>>>>>>>>>>>>>
['Hello', 'World', 'bnb', 'cnbc', 'abc!']


###Using the split method, split the string with semi colon (;) first. Then, print only the last element.
str="Arsenal:0-Chelsea:1;Barcelona:2-Bayern Munich:2"
#Type your code here.

lst= str.split(";")
ans_1= lst[-1]

print(ans_1)
>>>>>>>>>>>>>>>>>>>>>>>>.
Barcelona:2-Bayern Munich:2




###format() method to insert numbers into strings:
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
>>>>>>>>>>>>>>>>
My name is John, and I am 36




quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
>>>>>>>>>>>>>>>>>>>>>
I want 3 pieces of item 567 for 49.95 dollars.




quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price)) 
>>>>>>>>>>>>>>>>>>>>>>>>>
I want to pay 49.95 dollars for 3 pieces of item 567



###To insert double quote character " " inside double quote " " print statement. use \" character.

txt = "We are the so-called \"Vikings\" from the north."
print(txt) 



#####INDEX METHOD

str="The best revenge is massive success."

#  Type your code here.

ans_1= str.index("v")


print(ans_1)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
11



######FIND METHOD

str="The best revenge is massive success."

#  Type your code here.

ans_1= str.find("m")


print(ans_1)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>
20

FIND METHOD when value is not present in the variable

str="The best revenge is massive success."

#  Type your code here.

ans_1 = str.find("X")

print(ans_1)
>>>>>>>>>>>>>>>>>>>
-1



str="The best revenge is massive success."

#  Type your code here.

ans_1 = str.index("X")

print(ans_1)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>
ValueError: substring not found on line 5



###########COUNT METHOD TO COUNT A CHARACTER

str="People often say that motivation doesn't last. Well, neither does bathing.  That's why we recommend it daily."
#  Type your code here.

ans_1= str.count("a")

ans_2= str.count("o")


print("count of a is: ", ans_1, " count of o is: ", ans_2)
>>>>>>>>>>>>>>>>>>
count of a is:  7  count of o is:  7


###DATA TYPE

v_1="1"
v_2=1

#  Type your code on line 4:

ans_1= type(v_2)

ans_2=type(v_1)


print(ans_1)
print(ans_2)
.>>>>>>>>>>>>>
<type 'int'>
<type 'str'>


str="1.975.000"

#  Type your code here:

ans_1= len(str)


print(ans_1)
>>>>>>>>>>>>>>>>>>>>>>>>>>
9



---------------------------------------------------------------------------------------------------------------

Boolean Boolean Boolean Boolean Boolean Boolean Boolean Boolean Boolean Boolean Boolean 

---------------------------------------------------------------------------------------------------------------


Booleans represent one of two values: True or False.

example:

print(10 > 9)
print(10 == 9)
print(10 < 9)
>>>>>>>>>>>>>>>>>>
True
False
False



print(bool("Hello"))
print(bool(15))
>>>>>>>>>>>>>>>>>>>>>
True
True

IN PYTHON BOOLEANS:
Any string is True, except empty strings.

Any number is True, except 0.

Any list, tuple, set, and dictionary are True, except empty ones



FALSE VALUE WHEN YOU RUN ON PYTHON

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))
>>>>>>>>>>>>>>>>>>>>>>>>>
False
False
False
False
False
False
False











--------------------------------------------------------------------------------------------------------------

LIST LIST LIST LIST LIST LIST LIST LIST LIST LIST LIST LIST LIST LIST LIST LIST

Array Array Array Array Array Array Array Array Array Array Array Array Array Array Array  

-------------------------------------------------------------------------------------------------------------- 

There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.





names = ['Alice', 'Bob', 'Charley']
for name in names:
    print(f"Hello, {name.upper()}")

x = [1023, 454, 56,]                             #It is a list.
print(x)

y = ["bb", "aa", "zz", "mm"]            #It is a list of strings.
print(y)

print(["N"] * 4)                        #This will multiply list element 4 times
>>>>>>>>>>>>>>
['N', 'N', 'N', 'N']


x.append(599)           #append will add 599 to the x list.
print(x)

x.sort()            #It will sort in items on the increasing order.
print(x)

y.sort()            #It will also sort y list into incerasing order.
print(y)




D = [x ** 2 for x in [2, 3, 4, 5, 6, 8, 9]]    #It will give you squire of list elements.
print(D)


y = [1, 2, 3, 4, 5, 6] 
for x in y:
    print(x)

y = []
for x in [1, 2, 3, 4, 5, 6]:            #It will give you same result as up.
    y.append(x ** 2)



members=['Abbu', 'Ammi', 'Arsh', 'Falah', 'Sadaf', 'Zihan']
print(members[2])



print(members[5].upper())

print(members[-1])

message= f'The first member of our Family is- {members[0].upper()}!'
print(message)



###Lists allow duplicate values:

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)


thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
>>>>>>>>>>>>>>>>>>
cherry



motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati' #to replace an element
print(motorcycles)

motorcycles.append('RTR')  #to add at the end of the list
print(motorcycles)


motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.insert(2, 'ducati') #To insert an object into the list at place 2
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[0]
print(motorcycles)




thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
#This will return the items from position 2 to 5.

#Remember that the first item is position 0,
#and note that the item in position 5 is NOT included
>>>>>>>>>>>>>>>>>>>>>>>
['cherry', 'orange', 'kiwi']


#slicing third limit and slicing objects

S = 'abcdefghijklmnop'
S[1:10:2]                   ## Skipping items
>>>>>>>>>
'bdfhj'

S[::2]
>>>>>>>>>>>>>
'acegikmo'



#NESTED DATA

##Print 5 by accessing the nested data.
nested_lst=[[1,2,3], [4,5,6], [7,8,9]]
#Type your answer here.
ans_1= nested_lst[1][1]

print(ans_1)
>>>>>>>>>>>>>>>>>>>>>>.
5

###Print "Z" from the nested data.

nested_lst = [["Hat", "Glove", "Goggle"], ["Button", "Zipper", "Hook"]]
#Type your code here.

ans_1= nested_lst[1][1][0]

print(ans_1)
>>>>>>>>>>>>>>>>>>>>>>>>>
Z


##What color is the violet?
nested_lst = [{"orange": "orange"}, {"rose": "red"}, {"violet": "blue"}]
#Type your code here.

ans_1= nested_lst[2]["violet"]


print(ans_1)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>..
blue



#Print the values of the "roads" key from the nested dictionary.
nested_dict = {"Dakar":{"weather":"sunny", "roads":"dry"}}
#Type your answer here.

ans_1= nested_dict["Dakar"]["roads"]


print(ans_1)
>>>>>>>>>>>>>>>>>>>>>>>
dry


##Print the first element of the weather for Tokyo.
nested_dict = {"Tokyo": {"weather":["sunny", "cloudy"], "roads":"dry"}, "Dakar": {"weather":["foggy","windy"], "roads": "sandy"}}
#Type your answer here.

ans_1= nested_dict["Tokyo"]["weather"][0]


print(ans_1)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
sunny





S = '#$#$#$#$'
S = S.replace("$", "Arsh")           #replace all elements from a string.
print(S)
>>>>>>>>>>>>>
#Arsh#Arsh#Arsh#Arsh



S = '#$#$#$#$'
where = S.find("$")           #This will search for position of element on a string.
print(where)
>>>>>>>>>>>>>
1










#COUNTING HOW MANY TIME A VALUE PRESENT or OCCUR IN A LIST

lst=[55, 6, 777, 54, 6, 76, 101, 1, 6, 2, 6]
#  Type your code inside print() function.

answer_1= lst.count(6)

print(answer_1)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
4



wansh=['dadi', 'nani', 'nana', 'dada']
print(wansh)



###Using the list() constructor to make a List:
thislist = list(("apple", "banana", "cherry"))
print(thislist)




#To change an item in a list

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]                #To change a range of item.
print(thislist)



###To insert a new list item, without replacing any of the existing values, we can use the insert() method.

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)




####To add an item to the end of the list, use the append() method:
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)



####To append elements from another list to the current list, use the extend() method.
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>
['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']



###########Using a for loop and .append() method append each item with a Dr. prefix to the lst.

lst1=["Phil", "Oz", "Seuss", "Dre"]
lst2=[]
#Type your answer here.
for i in lst1:
    lst2.append("Dr."+ i)



print(lst2)
>>>>>>>>>>>>>>>>>>>>>>>>>
['Dr.Phil', 'Dr.Oz', 'Dr.Seuss', 'Dr.Dre']




###The extend() method you can add any iterable object (tuples, sets, dictionaries etc.).

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
>>>>>>>>>>>>>>>>>>>>>>>
['apple', 'banana', 'cherry', 'kiwi', 'orange']


###Using for loop and if statement, append the value minus 1000 for each key to the new list if the value is above 1000
dict={"z1":900, "t1": 1100, "p1": 2300, "r1": 1050, "k1": 3200, "g1": 400}
lst=[]
#Type your answer here.
for i in dict:
    if dict[i] > 1000:
        lst.append(dict[i]-1000)

print(lst)
>>>>>>>>>>>>>>>>>>>>>>>.
[100, 1300, 50, 2200]




##########The remove() method removes the specified item.

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)


thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
>>>>>>>>>>>>>>>>>>>>>>>
Yes, 'apple' is in the fruits list



Change the second item:

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
>>>>>>>>>>>>>>>>>
['apple', 'blackcurrant', 'cherry']




thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]

thislist[1:3] = ["blackcurrant", "watermelon"]

print(thislist)

.>>>>>>>>>>>>>>>>>>>
['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']


##Change the second value by replacing it with two new values:

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)
>>>>>>>>>>>>>>>>>>>
['apple', 'blackcurrant', 'watermelon', 'cherry']



##Change the second and third value by replacing it with one value:

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)
>>>>>>>>>>>>>>>>
['apple', 'watermelon']


#####Insert "watermelon" as the third item:
thislist = ["apple", "banana", "cherry"]

thislist.insert(2, "watermelon")

print(thislist)

['apple', 'banana', 'watermelon', 'cherry']





#####Add the elements of tropical to thislist:

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
>>>>>>>>>>>>>>>>>>
['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']




######The pop() method removes the specified index.

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)


gone=wansh.pop()
print(wansh)

print(gone)



motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")


wansh=['dadi', 'nani', 'nana', 'dada']
inteqal=wansh.pop()
print(f'\n\t{inteqal.upper()} Inteqal farma chuke hai!')




######The pop() method removes the specified index.

wansh=['dadi', 'nani', 'nana', 'dada']
nana_inteqal=wansh.pop(2)
print(f'\n\t{nana_inteqal.upper()} bhi Inteqal farma chuke hai aur wo bhi 18 saal pahle!')
print(wansh)


wansh=['dadi', 'nani', 'nana', 'dada']
jinda=wansh.pop(0)
print(f'\n\t In charo me se sirf meri {jinda.upper()} Jinda hai!')




wansh=['dadi', 'nani', 'nana', 'dada']
print(wansh)

wansh.remove('dada')
print(wansh)




marhoom=['dadi', 'nani', 'nana', 'dada']
print(marhoom)

hayat='dadi'
marhoom.remove(hayat)
print(marhoom)
print(f'\n\t{hayat.upper()} hayat se hai. Meri dadi abhi bhi zinda hai!')



cars = ['bmw', 'audi', 'toyota', 'jaguar', 'ford', 'bugatti', 'lemborghini']
cars.sort()
print(cars)


##sort in descending order that is reverse

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)



cars = ['bmw', 'audi', 'toyota', 'jaguar', 'ford', 'bugatti', 'lemborghini']

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))


#Using sorted() function, sort the list in ascending order.
lst1=[500, 1000, 400, 40000, 999, 2, 0.5, 17]

#Type your answer here.

lst2= sorted(lst1)
print(lst2)
>>>>>>>>>>>>>>>>.
[0.5, 2, 17, 400, 500, 999, 1000, 40000]



#Using sorted() function, sort the list from a to z.
lst1=["zebra", "bird", "ant", "porcupine", "giraffe"]

#Type your answer here.
lst2= sorted(lst1)
print(lst2)
>>>>>>>>>>>>>>>>>
['ant', 'bird', 'giraffe', 'porcupine', 'zebra']




#Using sorted() function sort the list from z to a.
lst1=["zebra", "bird", "ant", "porcupine", "giraffe"]
#Type your answer here.
lst2= sorted(lst1, reverse = True)
print(lst2)
>>>>>>>>>>>>>>>>
['zebra', 'porcupine', 'giraffe', 'bird', 'ant']


#Using sorted() function sort the list in descending order.
lst1=[500, 1000, 400, 40000, 999, 2, 0.5, 17]
#Type your answer here.
lst2= sorted(lst1, reverse = True)
print(lst2)
>>>>>>>>>>>>>>>>>>>>>
[40000, 1000, 999, 500, 400, 17, 2, 0.5]



#Using len function and sorted() function, sort the list based on the length of the strings (In ascending order).



lakes1=["Malawi", "Medicine", "Tahoe", "Moraine", "Upper Arrow", "Plitvice", "Edith", "Emerald"]

#Type your answer here.

lakes2= sorted(lakes1, key = len)

print(lakes2)
>>>>>>>>>>>>>>>>>>>>>
['Tahoe', 'Edith', 'Malawi', 'Moraine', 'Emerald', 'Medicine', 'Plitvice', 'Upper Arrow']


##Using len function and sorted() function, sort the list based on the length of the strings this time in descending order.
lakes1=["Malawi", "Medicine", "Tahoe", "Moraine", "Upper Arrow", "Plitvice", "Edith", "Emerald"]

#Type your answer here.

lakes2= sorted(lakes1, key = len, reverse = True)

print(lakes2)
>>>>>>>>>>>>>>>>>>>>>>>>>>>
['Upper Arrow', 'Plitvice', 'Medicine', 'Emerald', 'Moraine', 'Malawi', 'Edith', 'Tahoe']






print("\nHere is the original list again:")
print(cars)




cars = ['bmw', 'audi', 'toyota', 'jaguar', 'ford', 'bugatti', 'lemborghini']
print(cars)

cars.reverse()
print(cars)




cars = ['bmw', 'audi', 'toyota', 'subaru']       # works only in terminal
len(cars)



####The del keyword can also delete the list completely.

thislist = ["apple", "banana", "cherry"]
del thislist
print(thislist) #this will cause an error because you have succsesfully deleted "thislist".



####The clear() method empties the list.
The list still remains, but it has no content.

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
>>>>>>>>>>>>>>>>>>>>>>>>>
[]



fruits = ["apple", "banana", "cherry"]   
x, y, z = fruits                    #Unpack a list
print(x)
print(y)
print(z)



####Make a list with copy method

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)


#######Make a copy of a list with the list() method:

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)


#Joining a list
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)
>>>>>>>>>>>>>>>>>>>>>>
['a', 'b', 'c', 1, 2, 3]


#JOINING A LIST THROUGH .join() method

addresses=("Mr.Hathaway", "amymail.com")
#Type your code here.
email= "@".join(addresses)

print(email)
>>>>>>>>>>>>>>>>>>>>>>>>>>>
Mr.Hathaway@amymail.com



lst=["Hawaii", "Phuket", "Aruba", "Keys"]
#Type your answer here.
joined = "+++".join(lst)
                         
print(joined) 
>>>>>>>>>>>>>>>>>>>>>>>>>
Hawaii+++Phuket+++Aruba+++Keys

#Join a dictionary through a comma and space:

economic_growth={"India": 7.0, "Cambodia": 7, "Tanzania": 6.9, "Bangladesh": 6.6, "Senegal": 6.6}
#Type your code here.
str= ", ".join(economic_growth)

print(str)
>>>>>>>>>>>>>>>>>>>>>>>>>
India, Cambodia, Tanzania, Bangladesh, Senegal





#Use the extend() method to add list2 at the end of list1:

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)
>>>>>>>>>>>>>>>>>>>>>>
['a', 'b', 'c', 1, 2, 3]



------------------------------------------------------------------------------------------------------------


LIST LIST LIST LIST LIST LIST LIST LIST LIST LIST LIST LIST LIST LIST LIST LIST  LOOPING LOOPING LOOPING LOOPING LOOPING LOOPING LOOPING LOOPING 


--------------------------------------------------------------------------------------------------------------





cars = ['bmw', 'audi', 'toyota', 'jaguar', 'ford', 'bugatti', 'lemborghini']
for car in cars:
    
    print(car)





cars = ['bmw', 'audi', 'toyota', 'jaguar', 'ford', 'bugatti', 'lemborghini']
for brand in cars:

    print(f'\t{brand.upper()} is a very good brand of car and it is amongs my known list of car!.\n')

    print(f"\t I am waiting to see you in jannah and at that point you my sawari will be live and at that time i could also talk to you  , {brand.upper()}.\n\n\n")





cars = ['bmw', 'audi', 'toyota', 'jaguar', 'ford', 'bugatti', 'lemborghini']
for brand in cars:

print(f'{brand.upper()} is a very good brand of car and it is amongs my known list of car!.')

print(f" I am waiting to see you in jannah and at that point you my sawari will be live and at that time i could also talk to you  , {brand.upper()}.\n")


print("I am egearly waiting for You!")



####A short hand for loop that will print all items in a list:

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]


####Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
>>>>>>>>>>>>>>>>>
['apple', 'banana', 'mango']



###With list comprehension you can do all that with only one line of code:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)
>>>>>>>>>>>>>>>>>>>>>>
['apple', 'banana', 'mango']


#### Only accept items that are not "apple":
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if x != "apple"]

print(newlist)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
['banana', 'cherry', 'kiwi', 'mango']



##########Without if and true or false

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits]

print(newlist)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>
['apple', 'banana', 'cherry', 'kiwi', 'mango']


#UPPER CASE

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x.upper() for x in fruits]

print(newlist)
>>>>>>>>>>>>>>>>>>>>>>>>>>
['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']




####Return "orange" instead of "banana":
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x if x != "banana" else "orange" for x in fruits]

print(newlist)

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
['apple', 'orange', 'cherry', 'kiwi', 'mango']



###RANGE FUNCTION
'
#Type your answer here.

rng= range(0, 50)

print(rng)
>>>>>>>>>>>>>>>>>>>>>>>.
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]


for number in range(2, 8):
print(number)


for number in range(7):
print(number)


number = list(range(2, 8))
print(number)
>>>[2, 3, 4, 5, 6, 7]



even=list(range(2,19,2))    # 2 ka pahada table 
print(even)
>>>>>>>>>[2, 4, 6, 8, 10, 12, 14, 16, 18]



three=list(range(3,31,3)) # 3 ka pahada table
print(three)

five=list(range(5,100,5)) # 5 ka pahada table
print(five)




squares = []
for value in range(1, 11):
    squares.append(value**2)
    print(squares)



digi=[1, 5, 6, 17 , 33, 44, 68, 99, 34, 22, 11]
min(digi)
max(digi)
sum(digi)


squares = [value**2 for value in range(1, 11)]
print(squares)


###RANGE IN DESCENDING ORDER
# Type your answer here.

rng= range(1300, 700, -100)


print(list(rng))
>>>>>>>>>>>>>>>>>>>>
[1300, 1200, 1100, 1000, 900, 800]



players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:4])
print(players[0:3])
print(players[:4])
print(players[2:])
print(players[-3:])





books = ['rich dad poor dad', 'think and grow rich', 'man are from mars and women are from venus', 'the five love languages', 'zero to one']
print("Here are the first three books on my book list:")
for book in books[:3]:
print(book.upper())




mybook=['rich dad poor dad', 'think and grow rich', 'man are from mars and women are from venus', 'the five love languages', 'zero to one']
attaurbook=mybook[:]  # YE EQUAL NAHI HO GAYA YE BAS COPY KIYE HAI.
print("my favourite books are:")
print(mybook)

print("\nNow my friend Attaur's favourite books is")
print(attaurbook)

mybook.append('the one thing')
attaurbook.append("can't hurt me")

print(mybook)
print(attaurbook)


----------------------------------------------------------------------------------------------------------------

Tuple Tuple Tuple Tuple Tuple Tuple Tuple Tuple Tuple Tuple Tuple Tuple Tuple Tuple Tuple

----------------------------------------------------------------------------------------------------------------


Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

A tuple is a collection which is ordered and unchangeable.and allow duplicate values.

Tuples are written with round brackets.

Ordered
When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

Unchangeable
Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

Allow Duplicates
Since tuples are indexed, they can have items with the same value:





##########Tuples allow duplicate values:

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#########Create Tuple With One Item
To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))
>>>>>>>>>>>>>>>>>>>>>
<class 'tuple'>
<class 'str'>


T = (1, 2, 3, 4)            #Tuple
len(T)
print(T)



###Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.
But
$$$$$$Can Convert the tuple into a list to be able to change it:
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)
>>>>>>>>>>>>>>>>>>.
("apple", "kiwi", "cherry")



#####Since tuples are immutable, they do not have a build-in append() method
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
>>>>>>>>>>>>>>>>>>>
('apple', 'banana', 'cherry', 'orange')


#######2. Add tuple to a tuple. You are allowed to add tuples to tuples, so if you want to add one item, (or many), create a new tuple with the item(s), and add it to the existing tuple:


Create a new tuple with the value "orange", and add that tuple:
#####Note: When creating a tuple with only one item, remember to include a comma after the item, otherwise it will not be identified as a tuple.

thistuple = ("apple", "banana", "cherry")
y = ("orange",) 

thistuple += y

print(thistuple)
>>>>>>>>>>>>>>>>>>>
('apple', 'banana', 'cherry', 'orange')


####Tuples are unchangeable, so you cannot remove items from it,
Convert the tuple into a list, remove "apple", and convert it back into a tuple:

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)



####The del keyword can delete the tuple completely:

thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists
>>>>>>>>>>>>>>>
Error



###########When we create a tuple, we normally assign values to it. This is called "packing" a tuple:

Example
Packing a tuple:

fruits = ("apple", "banana", "cherry")


##################But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":

Example
Unpacking a tuple:

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
>>>>>>>>>>>>>>
apple
banana
cherry


#####Using Asterisk*
If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:

Example
Assign the rest of the values as a list called "red":

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)
>>>>>>>>>>>>>>>>>
apple
banana
['cherry', 'strawberry', 'raspberry']


#########FOR LOOP IN TUPLE
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)


percentage=(76, 65, 80)
for percent in percentage:
print(percent)



######Print all items, using a "while" loop to go through all the index numbers:

thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1
>>>>>>>>>>>>>>>>
apple
banana
cherry



########Multiply the fruits tuple by 2:

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)
>>>>>>>>>>>>>>>>>>
('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')







dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])










#you can’t modify a tuple, you can assign a new value to a variable
that represents a tuple.

dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
print(dimension)
#Python doesn’t raise any errors this time, because reassigning a variable is valid.







----------------------------------------------------------------------------------------------------------------

Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set 

----------------------------------------------------------------------------------------------------------------



###A set is a collection which is unordered, unchangeable*, and unindexed.

###Create a Set:

thisset = {"apple", "banana", "cherry"}
print(thisset)
###### Note: the set list is unordered, meaning: the items will appear in a random order.

# Refresh this page to see the change in the result.
>>>>>>>>>>>>>>>>>
{'banana', 'cherry', 'apple'}


$$$$$$$$Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

Unchangeable
Set items are unchangeable, meaning that we cannot change the items after the set has been created.

Duplicates Not Allowed
Sets cannot have two items with the same value.

Remove and add items
Once a set is created, you cannot change its items, but you can remove items and add new items.



######Duplicate values will be ignored:

thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)
>>>>>>>>>>>>
{'banana', 'cherry', 'apple'}




####Using the set() constructor to make a set:

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
>>>>>>>>>>>>>
{'apple', 'banana', 'cherry'}




#####Check if "banana" is present in the set:

thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)
>>>>>>>>>>>>>>>>>>>>.
True




####Add an item to a set, using the add() method:

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)



#####Add Sets
To add items from another set into the current set, use the update() method.

Example
Add elements from tropical into thisset:

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)
>>>>>>>>>>>>>>>>
{'apple', 'mango', 'cherry', 'pineapple', 'banana', 'papaya'}


$$$$$$$$$The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).


thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)
>>>>>>>>>>>>>>>>>>>
{'banana', 'cherry', 'apple', 'orange', 'kiwi'}


$#########Remove Item
To remove an item in a set, use the remove(), or the discard() method.

Example
Remove "banana" by using the remove() method:

thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)




######Note: If the item to remove does not exist, discard() will NOT raise an error.

thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)




thisset = {"apple", "cherry"}

thisset.discard("banana")

print(thisset)
>>>>>>>>>>>>>>>>>>.
{'cherry', 'apple'}



##########You can also use the pop() method to remove an item

thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)

Note: Sets are unordered, so when using the pop() method, you do not know which item that gets removed.


########Loop through the set, and print the values:

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)


##############Join Two Sets
There are several ways to join two or more sets in Python.

You can use the union() method that returns a new set containing all items from both sets, or the update() method that inserts all the items from one set into another:

Example
The union() method returns a new set with all items from both sets:

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
$$$$$$$$$$$$$$$$Note: Both union() and update() will exclude any duplicate items.


>>>>>>>>>>>>>
The update() method inserts the items in set2 into set1:

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)





##############Keep ONLY the Duplicates
The intersection_update() method will keep only the items that are present in both sets.

Example
Keep the items that exist in both set x, and set y:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)

############The intersection() method will return a new set, that only contains the items that are present in both sets.

Example
Return a set that contains the items that exist in both set x, and set y:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)


########Keep All, But NOT the Duplicates
The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.

Example
Keep the items that are not present in both sets:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)



#########The symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets.

Example
Return a set that contains all items from both sets, except items that are present in both:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)
















------------------------------------------------------------------------------------------------------
Dictionary Dictionary Dictionary Dictionary Dictionary Dictionary Dictionary Dictionary Dictionary

-------------------------------------------------------------------------------------------------------


###Dictionary
Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

Dictionaries are written with curly brackets, and have keys and values:



thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)



########Duplicates Not Allowed
Dictionaries cannot have two items with the same key:

Example
Duplicate values will overwrite existing values:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)
>>>>>>>>>>>>>>
{'brand': 'Ford', 'model': 'Mustang', 'year': 2020}



########can access the items of a dictionary by referring to its key name, inside square brackets:
Get the value of the "model" key:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
>>>>>>>>>>>>>
Mustang



#####get() that will give you the same result:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.get("model")
print(x)
>>>>>>>>>
Mustang

###"Get" Method of Dictionaries for Sophisticated Value Calling
#.get() method takes two parameters, 1) value being looked up, 2) value to return if nothing comes up.

dict={"son's name": "Lucas", "son's eye color": "green", "son's height": 32, "son's weight": 25}

#Type your answer here.
ans_1= dict.get("son's age", "Sorry Sir Nothing Found")

print(ans_1)
>>>>>>>>>>>>>>>>>
Sorry Sir Nothing Found





#######Get Keys
The keys() method will return a list of all the keys in the dictionary.

Example
Get a list of the keys:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.keys()

print(x)
>>>>>>>>>>>>>>>>
dict_keys(['brand', 'model', 'year'])


#########Adding new item or a key in the dictionary :

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

#before the change
print(x) 

car["color"] = "white"

#after the change
print(x) 
>>>>>>>>>>>>>>>>>>>
dict_keys(['brand', 'model', 'year'])
dict_keys(['brand', 'model', 'year', 'color'])


###To Get Only Values
The values() method will return a list of all the values in the dictionary.

Example
Get a list of the values:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.values()

print(x)
>>>>>>>>>>>.
dict_values(['Ford', 'Mustang', 1964])


###########Changing the value of a key

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["year"] = 2020

print(x) #after the change

>>>>>>>>>>>>>>>>>>>>
dict_values(['Ford', 'Mustang', 1964])
dict_values(['Ford', 'Mustang', 2020])


########Get Items
The items() method will return each item in a dictionary, as tuples in a list.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.items()

print(x)
>>>>>>>>>>>>>
dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])




thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict["year"] = 2018

print(thisdict)
>>>>>>>>>>>
{'brand': 'Ford', 'model': 'Mustang', 'year': 2018}



##########Update the "year" of the car by using the update() method:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
>>>>>>>>>>>>
{'brand': 'Ford', 'model': 'Mustang', 'year': 2020}



####Add a color item to the dictionary by using the update() method:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})


#########Removing Items
There are several methods to remove items from a dictionary:

Example
The pop() method removes the item with the specified key name:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)
>>>>>>>>>>>>>>>>
{'brand': 'Ford', 'year': 1964}


#####The del keyword removes the item with the specified key name:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)
>>>>>>>>>>>>>>>>>>
{'brand': 'Ford', 'year': 1964}


####Loop Through a Dictionary
You can loop through a dictionary by using a for loop.

When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.

Example
Print all key names in the dictionary, one by one:

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x)
>>>>>>>>>>>>>>>>
brand
model
year


########Print all values in the dictionary, one by one:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(thisdict[x])
>>>>>>>>>>>>>>>
Ford
Mustang
1964


#######You can also use the values() method to return values of a dictionary:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.values():
  print(x)
>>>>>>>>>>>>>>>>>
Ford
Mustang
1964

####You can use the keys() method to return the keys of a dictionary:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.keys():
  print(x)

>>>>>>>>>>>>>>>
brand
model
year

######Loop through both keys and values, by using the items() method:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x, y in thisdict.items():
  print(x, y)
>>>>>>>>>>>>>>>>
brand Ford
model Mustang
year 1964


#######To make a copy of A Dictionary 
Make a copy of a dictionary with the copy() method:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)
>>>>>>>>>>>>>>>>>>
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}



####Make a copy of a dictionary with the dict() function:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)
>>>>>>>>>>>>>>>
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}



###SORT KEYS IN A DICTIONARY


dict={"tiramisu":5, "chocolate":2, "pudding":3, "cheesecake":4}
#  Type your code below.

key_list= dict.keys()

key_list.sort()

print(key_list)

>>>>>>>>>>>>>>>>>>>>>>>>>>>>
['cheesecake', 'chocolate', 'pudding', 'tiramisu']



##########Nested Dictionaries
A dictionary can contain dictionaries, this is called nested dictionaries.

Example
Create a dictionary that contain three dictionaries:

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
{'child1': {'name': 'Emil', 'year': 2004}, 'child2': {'name': 'Tobias', 'year': 2007}, 'child3': {'name': 'Linus', 'year': 2011}}




#####Or, if you want to add three dictionaries into a new dictionary:

Example
Create three dictionaries, then create one dictionary that will contain the other three dictionaries:

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

{'child1': {'name': 'Emil', 'year': 2004}, 'child2': {'name': 'Tobias', 'year': 2007}, 'child3': {'name': 'Linus', 'year': 2011}}





alien = {'color': 'green', 'points': 5}
print(alien['color'])
print(alien['points'])


alien_0 = {'color': 'green', 'points': 5}
new_points = alien_0['points']
print(f"You just earned {new_points} points!")

#Adding New Key-Value Pairs

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)



#STARTING WITH an EMPTY Dictionary

alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)


#Modifying Values in a Dictionary

alien = {}
alien['color']= 'green'
alien['points']= '5'
print(alien)
print(f"\n alien is {alien['color']}.")

alien['color']= 'yellow'
print(f"\n Now the color of Alien is {alien['color']}.\n")



# Removing Key-Value Pairs

alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

del alien_0['points'] #DELETING or REMOVING AN ITEM FROM THE Dictionary
print(alien_0)





favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

favorite_languages['sarah']




#USING .get()

alien_0 = {'color': 'green', 'speed': 'slow'}
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)





user_0 = {
'username': 'efermi',
'first': 'enrico',
'last': 'fermi',
}

for name, half in user_0.items():

    print(f'{name}')

    print(f'{half}')





favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

for key, value in favorite_languages.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")





    favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

    for name, language in favorite_languages.items():
        print(f"\n{name.title()}'s favourite language is {language.upper()}!\n")






        alien_0 = {'color': 'green', 'points': 5}
        alien_1 = {'color': 'yellow', 'points': 10}
        alien_2 = {'color': 'red', 'points': 15}

        aliens = [alien_0, alien_1, alien_2]
        for alien in aliens:
            print(alien)







            # Make an empty list for storing aliens.
            aliens = []
            # Make 30 green aliens.
            for alien_number in range(30):
              new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
              aliens.append(new_alien)

            # Show the first 5 aliens.
            for alien in aliens[:5]:
              print(alien)
            print("...")

            # Show how many aliens have been created.
            print(f"Total number of aliens: {len(aliens)}")







            #to change the first three aliens



            # Make an empty list for storing aliens.
            aliens = []
            # Make 30 green aliens.
            for alien_number in range (30):
                new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
                aliens.append(new_alien)
            for alien in aliens[:3]:
                if alien['color'] == 'green':
                    alien['color'] = 'yellow'
                    alien['speed'] = 'medium'
                    alien['points'] = 10
            # Show the first 5 aliens.
            for alien in aliens[:5]:
                print(alien)
            print("...")

            print(f"\nTotal number of aliens: {len(aliens)}")






            favorite_languages = {
            'jen': ['python', 'ruby'],
            'sarah': ['c'],
            'edward': ['ruby', 'go'],
            'phil': ['python', 'haskell'],
            }

            for name, languages in favorite_languages.items():
                print(f"\n{name.title()}'s favourite languages are:")
                for language in languages:
                    print(f"\t{language.title()}")



# Multiple Dictionary Multiple Dictionary Multiple Dictionary

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
    }
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")





 
-----------------------------------------------------------------------------------------------------------------

if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if

-----------------------------------------------------------------------------------------------------------------




a = 33
b = 200
if b > a:
  print("b is greater than a")
>>>>>>>>>>>>
b is greater than a


#####Indentation
Python relies on indentation (whitespace at the beginning of a line) to define scope in the code. Other programming languages often use curly-brackets for this purpose.

Example
If statement, without indentation (will raise an error):

a = 33
b = 200
if b > a:
print("b is greater than a") # you will get an error
>>>>>>>>>>>
Error




######Elif
The elif keyword is pythons way of saying "if the previous conditions were not true, then try this condition".

Example
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
>>>>>>>>>>>>>>>>>>>>>>>>>.....
a and b are equal



######Else
The else keyword catches anything which isn't caught by the preceding conditions.
a = 33
b = 33
if a > b:
  print("a is greater than b")
elif a < b:
  print("b is greater than a")
else:
  print("a is equal to b")

>>>>>>>>>>>>>>>>
a is equal to b



###########Short Hand If
If you have only one statement to execute, you can put it on the same line as the if statement.

Example
One line if statement:

if a > b: print("a is greater than b")
>>>>>>>>>>>>>>>>>>>>>>>>.
"a is greater than b"



#############Short Hand If ... Else
If you have only one statement to execute, one for if, and one for else, you can put it all on the same line:

Example
One line if else statement:

a = 2
b = 330
print("A") if a > b else print("B")
>>>>>>>>>>>>>>>>>>>>>
B



##########You can also have multiple else statements on the same line:

Example
One line if else statement, with 3 conditions:

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")
>>>>>>>>>>>>>>>>>>..
=

#####And
The and keyword is a logical operator, and is used to combine conditional statements:

Example
Test if a is greater than b, AND if c is greater than a:

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
>>>>>>>>>>>>>>>>>.
Both conditions are True


###########Or
The or keyword is a logical operator, and is used to combine conditional statements:

Example
Test if a is greater than b, OR if a is greater than c:

a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")
>>>>>>>>>>
At least one of the conditions is True





#########Nested If
You can have if statements inside if statements, this is called nested if statements.

Example
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
>>>>>>>>>>>>>
and also above 20!





##########The pass Statement
if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.

Example
a = 33
b = 200

if b > a:
  pass








members = ['masqurul', 'rukhsana', 'arsh', 'falah', 'sadaf', 'zihan']
for member in members:
if member=='masqurul':
print(member.upper())
else:
print(member.title())




car = 'bmw'
car == 'bmw'

 #A single equal sign(=) is really a statement:   “Set the value of car equal to 'bmw' .”
 #A double equal sign(==) asks a question:      “Is the value of car equal to 'bmw' ?”

car = 'audi'
car == 'bmw'



#two values with different capitalization are not considered equal:
>>> car = 'Audi'
>>> car == 'audi'
False


#you can convert the variable’s value to lowercase before doing the comparison:

>>> car = 'Audi'
>>> car.lower() == 'audi'
True

#can do this kind of comparison without affecting the original variable:

>>> car = 'Audi'
 >>> car.lower() == 'audi'
True
 >>> car
'Audi'




!= != != != != != != != != != != != != != != != != != != != != != != !=



order = 'burger'
if order != 'cold drink':
print("Hold a cold drink also!")


answer= 15
if answer!= 10:
print("That is not the correct answer. Please try again!")


>>> age_0 = 22
>>> age_1 = 18
>>> age_0 >= 21 and age_1 >= 21 #AND EXPRESSION
False




age1=15
age2=20
age1>=12 and age2>=12

age1>=20 and age2>=20





age1=15
age2=20
age1>=20 or age2>=20  # OR EXPRESSION

age2=18
age1>=20 or age2>=20



icecream=['cup', 'chocobar', 'vanilla']
'cup' in icecream                    #in EXPRESSION
'strawberry' in icecream


banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
print(f'\n Hey! {user.title()} You can post a response if you wish.')
else:
print(f"\n Hey! {banned_users.title()} You can't post a response even if you wish. Because you are added to Blocked user")





age = 17
if age >= 18:
print("You are old enough to vote!")
print("Have you registered to vote yet?")
else:
print("Sorry, you are too young to vote.")
print("Please register to vote as soon as you turn 18!")


elif elif elif elif elif elif elif elif elif elif elif elif elif elif


age= 19
if age<=4:
  print("Your admission cost is $0.")
elif age<=18:
  print("Your admission cost is $25.")
else :
  print("Your admission cost is $40.")


  age= 12
  if age<=4:
    price=0
  elif age<=18:
    price=25
  else :
    price=40
  print(f"\n\tYour admission cost is ${price}.\n")






  message = input("Tell me something, and I will repeat it back to you: ")
  print(message)

  name = input("Please enter your name: ")
print(f"\nHello, {name}!")



requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")





age= input("Please enter your age: ")
age=int(age)
if age<=4:
    price=0
elif age<=18:
    price=25
elif age<=50:
    price=40
elif age<=65:
    price=30
elif age<=75:
    price=20
else :                #USING else
    price=5
print(f"\n\tYour admission cost is ${price}.\n")




age= input("Please enter your age: ")
age=int(age)
if age<=4:
    price=0
elif age<=18:
    price=25
elif age<=50:
    price=40
elif age<=65:
    price=30
elif age<=75:
    price=20
elif age>=75:                # USING ONLY elif
    price=5
print(f"\n\tYour admission cost is ${price}.\n")




requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print('adding mushrooms')
if 'pepperoni' in requested_toppings:
    print('adding pepperoni')
if 'extra cheese' in requested_toppings:
    print('adding extra cheese')
print("\nFinished making your pizza!")



requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for bnb in requested_toppings:
    print(f"Adding {bnb}.")
print("\nFinished making your pizza!")



requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("\nSorry, we are out of green peppers right now.")
    else:
        print(f"\nAdding {requested_topping}.")
print("\n\tFinished making your pizza!\n")



available_toppings = ['mushrooms', 'olives', 'green peppers',
'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")
print("\nFinished making your pizza!")


-----------------------------------------------------------------------------------------------------

While While While While While While While While While While While While While While 

-----------------------------------------------------------------------------------------------------

$$$$$$Python Loops
Python has two primitive loop commands:

while loops
for loops


The while Loop
With the while loop we can execute a set of statements as long as a condition is true.

Example
Print i as long as i is less than 6:

i = 1
while i < 6:
  print(i)
  i += 1
>>>>>>>>>>>>>>>>>>>
1
2
3
4
5





##########The break Statement
With the break statement we can stop the loop even if the while condition is true:

Example
Exit the loop when i is 3:

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

>>>>>>>>>>>>>>>>>>
​1
2
3

#Place a break statement in the for loop so that it prints from 0 to 7 only (including 7).
for i in range(100):
    print(i)
    if i == 7:
        break
>>>>>>>>>>>
0
1
2
3
4
5
6
7


######The continue Statement
With the continue statement we can stop the current iteration, and continue with the next:

Example
Continue to the next iteration if i is 3:

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
>>>>>>>>>>>>>>>>>>>>>>>>>>>
1
2
4
5
6




####Add an if statement and a continue statement to the loop so that it skips when iterator equals "sun".
weather=["snow", "rain", "sun", "clouds"]

#Type your answer here.
for i in weather:
    if i == "sun":
        continue

    print(i)
>>>>>>>>>>>>>>>>>>>>>>>>>
snow
rain
clouds





#############
while True:
    line = input("> ")
    if line[0] == "#":
        continue
    if line == "done":
        break
    print(line)
print("Done")




############3The else Statement
With the else statement we can run a block of code once when the condition no longer is true:

Example
Print a message once the condition is false:

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

.>>>>>>>>>>>>>
1
2
3
4
5
i is no longer less than 6



##FINDING INDEX NUMBER OF A NUMBER IN A LIST
##Using while loop, if statement and str() function; iterate through the list and if there is a 100, print it with its index number. i.e.: "There is a 100 at index no: 5"

lst=[10, 99, 98, 85, 45, 59, 65, 66, 76, 12, 35, 13, 100, 80, 95]
#Type your code here.
i = 0
while i < len(lst):
    if lst[i] == 100:
        print("There is a 100 at index no: " , i) 
#OR print("There is a 100 at index no: " + str(i))  #this str will convert i(which is index number) into string. So, that it can be printed along with another string message on print. Because string and integer can't be print simultaniously in one line

    i = i+1
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>..
There is a 100 at index no: 12



### Using while loop and an if statement write a function named name_adder, and inside that function write a while loop that stops appending items to the new list as soon as it encounters an empty string: "". And prints "There is an empty string and returns the new list."


lst1=["Sam", "Ben", "Olivia", "", "Alicia"]

#Type your answer here.    
def name_adder(list):
    i=0
    new_list = []
    while i < len(list):
        if list[i] != "":
            new_list.append(list[i])
        else:
            break
        i += 1
    return new_list
        
print(name_adder(lst1))
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.
['Sam', 'Ben', 'Olivia']




Functions Functions Functions Functions Functions Functions Functions Functions








def hello():
    print('Hello there.')

hello()
hello()
hello()
hello()


#COMBINING A FUNCTION

def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')

def repeat_lyrics():
    print_lyrics()
    print_lyrics()

repeat_lyrics()
>>>>>>>>>>>>>>>>>>>>>>>>>>>.
I'm a lumberjack, and I'm okay.
I sleep all night and I work all day.
I'm a lumberjack, and I'm okay.
I sleep all night and I work all day.








def greet(user):
    print(f"Hello, {user.upper()}!")

greet('arsh')
greet('zihan')


#maximum of three number in python without built in function "max".

def maximum(x, y, z):
    max = 0
    if x>max:
       max = x
    if y>max:
        max = y
    if z>max:
        max = z
    return max
        
print(maximum(75, 5550, 69))

#Find out the length of given string without using buil in function "len".
def length(given_string):
    c = 0
    for element in given_string:
        c += 1
    return c
        
print(length("Arsh"))


#Positional Arguments #Positional Arguments #Positional Arguments


def pet_detail(animal, pet_name):
    print(f"\n I have a {animal}. and my {animal} name is {pet_name.title()}!\n" )

pet_detail('dog', 'hero')
pet_detail('hen', 'sundri')
pet_detail('black hen', 'kadaknaath')



def full(first, last):
    print(f'{first} {last}')

full('Mohammad', 'Arsh')
full('Amjad', 'khan')
full('Mohammad', 'Zihan')




#Write a function named "evens" which returns True if a number is even and otherwise returns False.

def evens(i):
    if i%2 == 0:
        return True
    else:
        return False


print(evens(99))
print(evens(98))
>>>>>>>>>>>>>>>>>>>>.
False
True



#Write a function named "thedecimal" which returns the decimal part of a number. If decimal part is zero function should return this string: "INTEGER".


def thedecimal(x):
    if x - int(x) != 0:
        return x - int(x)
    else:
        return "INTEGER"



print(thedecimal(99.09))
print(thedecimal(99.00))
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
0.09
INTEGER




##treepersqkm is a dictionary showing the tree number of countries per square kilometer for random countries with sizeable population numbers. Write a function named "moretrees" that returns a list of country names with more than 20.000 trees per square kilometer.

treepersqkm = {"Finland": 90652, "Taiwan": 69593, "Japan": 49894, "Russia": 41396, "Brazil": 39542, "Canada": 36388, "Bulgaria": 24987, "France": 24436, "Greece": 24323, "United States": 23513, "Turkey": 11126, "India": 11109, "Denmark": 6129, "Syria": 534, "Saudi Arabia": 1}
#Type your answer here.

def moretrees(x):
    lst = []
    for i in x:
        if x[i]>20000:
            lst.append(i)
        else:
            pass
    return lst

print(moretrees(treepersqkm))
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
['Finland', 'Taiwan', 'Japan', 'Russia', 'Brazil', 'Canada', 'Bulgaria', 'France', 'Greece', 'United States']




###COUNT HOW MANY WORD THAT CONTAIN "x" letter:
#Write a function named "count_l" that counts the number of words that contain the letter: "l" in a given string.

str = "Oranges and lemollllllllnls, Say the bllllllells of St. Clemlenllllllllt's. You owe me three farthings, Say the bllllells of St. Martin's"


#Type your answer here.

def count_l(a):
    c = 0
    for i in a.split(" "):
        if "l" in i:
            c = c+1
        else:
            pass

    return c
    
    

print(count_l(str))
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.
4



###COUNT HOW MANY WORD THAT STARTSWITH "x"

Write a similar function to 7-e which returns the number of words that start with letter "A" in a string. (Make sure it counts lower case a's as well.).


str = ""Oranges aaaaaand Alaaaaaemons, Say the bells of St. Clement's. You Aowaaaaaaaaae me three afaaaaaarthings, Say the bells of St. aMartinaaaaa's"

#Type your answer here.
    
def count_l(a):
    c = 0
    for i in a.split():
        if i[0].lower() == "a":
            c = c+1
        else:
            pass

    return c  

print(count_l(str))
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
5





#Keyword Arguments #Keyword Arguments #Keyword Arguments #Keyword Arguments


def pet_detail(animal, pet_name):
    print(f"\n I have a {animal}. and my {animal} name is {pet_name.title()}!\n" )

pet_detail(animal='dog',           pet_name= 'hero')
pet_detail(pet_name='sundri',      animal='hen')     # pet name AUR animal
                                                    IDHAR UDHAR HAI PHIR BHI
                                                    KOI FARK NAHI PADTA HAI
pet_detail(animal='black hen',     pet_name='kadaknaath')
pet_detail(pet_name='guturgu',     animal='pegion')



# DEFAULT ANIMAL # DEFAULT ANIMAL # DEFAULT ANIMAL # DEFAULT ANIMAL


def pet_detail(pet_name, animal='chicken'):
    print(f"\n I have a {animal}. and my {animal} name is {pet_name.title()}!\n" )

pet_detail(pet_name= 'sundri')
pet_detail(pet_name='charki')
pet_detail(pet_name='kadaknaath')
pet_detail(pet_name='farm murgi')

             OR
#just name of the pet #just name of the pet #just name of the pet
             pet_detail('sundri')
             pet_detail('charki')
             pet_detail('kadaknaath')
             pet_detail('farm murgi')



#Unlimited #Unlimited #Unlimited #Unlimited #Unlimited #Unlimited #Unlimited


def make_pizza(*toppings):
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')




#UNLIMITED WITH MEANINGFULL

def make_pizza(*toppings):
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')















 

--------------------------------------------------------------------------------------------------------------
for for for for for for for for for for for for for for for for for for for for for for for for for   
--------------------------------------------------------------------------------------------------------------






The break Statement
With the break statement we can stop the loop before it has looped through all the items:

Example
Exit the loop when x is "banana":

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
>>>>>>>>>>>>>>>>>>>>>>>
apple
banana




##############The continue Statement
With the continue statement we can stop the current iteration of the loop, and continue with the next:

Example
Do not print banana:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

>>>>>>>>>>>>>>>>>>>>>
apple
cherry






###########The range() Function
To loop through a set of code a specified number of times, we can use the range() function,
The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

Example
Using the range() function:

for x in range(6):
  print(x)
>>>>>>>>>>>>>>>>>>>>>>>>>>>
0
1
2
3
4
5



for x in range(2, 6):
  print(x)
>>>>>>>>>>>>>>>>>>.
2
3
4
5


############The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):

Example
Increment the sequence with 3 (default is 1):

for x in range(2, 30, 3):
  print(x)
>>>>>>>>>>>>>>>>>>>>>>>>>>>
2
5
8
11
14
17
20
23
26
29



#################Else in For Loop
The else keyword in a for loop specifies a block of code to be executed when the loop is finished:

Example
Print all numbers from 0 to 5, and print a message when the loop has ended:

for x in range(6):
  print(x)
else:
  print("Finally finished!")
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
0
1
2
3
4
5
Finally finished!





########Note: The else block will NOT be executed if the loop is stopped by a break statement.
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

#If the loop breaks, the else block is not executed.
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
0
1
2



###########Nested Loops
A nested loop is a loop inside a loop.

The "inner loop" will be executed one time for each iteration of the "outer loop":

Example
Print each adjective for every fruit:

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
 >>>>>>>>>>>>>>>>>>>>>>>>>>>>
red apple
red banana
red cherry
big apple
big banana
big cherry
tasty apple
tasty banana
tasty cherry


###########The pass Statement
for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.

Example
for x in [0, 1, 2]:
  pass
# having an empty for loop like this, would raise an error without the pass statement





#for loop but result not in column. Instead Result is in a Row and space in between!!!

for x in [1, 2, 3]:
    print(x, end=' ')






--------------------------------------------------------------------------------------------------------------
function function function function function function function function function function function 
--------------------------------------------------------------------------------------------------------------







 Python Functions
A function is a block of code which only runs when it is called.

You can pass data, known as parameters, into a function.

A function can return data as a result.

Creating a Function
In Python a function is defined using the def keyword:

Example
def my_function():
  print("Hello from a function")



##############Calling a Function
To call a function, use the function name followed by parenthesis:

Example
def my_function():
  print("Hello from a function")

my_function()  
>>>>>>>>>>>>>>>>>>> 
Hello from a function





##############Arguments
Information can be passed into functions as arguments.

Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.

The following example has a function with one argument (fname). When the function is called, we pass along a first name, which is used inside the function to print the full name:


def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Emil Refsnes
Tobias Refsnes
Linus Refsnes

 
Number of Arguments
By default, a function must be called with the correct number of arguments. Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.

Example
This function expects 2 arguments, and gets 2 arguments:

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")
>>>>>>>>>>>>>>>>>>>>>>>>>>>
Emil Refsnes




#####If you try to call the function with 1 or 3 arguments, you will get an error:
Example
This function expects 2 arguments, but gets only 1:

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil")
>>>>>>>>>>>>>>>>
Error



Arbitrary Arguments, *args
If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

This way the function will receive a tuple of arguments, and can access the items accordingly:

Example
If the number of arguments is unknown, add a * before the parameter name:

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")
>>>>>>>>>>>>>>>>
The youngest child is Linus




Keyword Arguments
You can also send arguments with the key = value syntax.

This way the order of the arguments does not matter.

Example
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
>>>>>>>>>>>>>>>>
The youngest child is Linus



Arbitrary Keyword Arguments, **kwargs
If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.

This way the function will receive a dictionary of arguments, and can access the items accordingly:

Example
If the number of keyword arguments is unknown, add a double ** before the parameter name:

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")
>>>>>>>>>>>>>>>>>>>>>>
His last name is Refsnes



Default Parameter Value
The following example shows how to use a default parameter value.

If we call the function without argument, it uses the default value:

Example
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
I am from Sweden
I am from India
I am from Norway
I am from Brazil



Passing a List as an Argument
You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.

E.g. if you send a List as an argument, it will still be a List when it reaches the function:

Example
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)
>>>>>>>>>>>>>>>>>>>>>>>>
apple
banana
cherry




Return Values
To let a function return a value, use the return statement:

Example
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))
>>>>>>>>>>>>>>>>>>>>>>>>>>>..
15
25
45

############
def num(a, b):
    x = a + b
    return x

any_variable = num(2, 5)
print(any_variable)


any_variable = num(4, 5)
print(any_variable)

any_variable = num(7, 9)
print(any_variable)






The pass Statement
function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.

Example
def myfunction():
  pass
# having an empty function definition like this, would raise an error without the pass statement











-----------------------------------------------------------------------------------------------------------------

input input input input input input input input input input input input input input input input 

-----------------------------------------------------------------------------------------------------------------



message = input("Tell me something, and I will repeat it back to you: ")
print(message)


message = input("Tell me something, and I will repeat it back to you: ")
print(f"\nDo you mean - {message}!")



text= "\nIf you could tell me that you will become my wife. Then i could talk to you in a zoom call but publicly. for now in text you could just tell me your first name."
text+= "\n\nCould you tell me your first name please:"
name = input(text)
print(f"\nHello, {name}!")


age = input(f"\n How old are you: ")
age = int(age)   # int FOR INTEGER
dob= age-2
print(f"\n Your date of birth according to 'ADHAAR CARD' is: {dob}\n")



height = input("\nHow tall are you, in feet? \n")
height = int(height)
if height >= 5:
    print("\nYou're tall enough to ride!\n")
else:
    print("\nYou'll be able to ride when you're a little older.\n")



    number = input("Enter a number, and I'll tell you if it's even or odd: ")
    number = int(number)
    if number % 2 == 0:
        print(f"\nThe number {number} is even.")
    else:
        print(f"\nThe number {number} is odd.")




#While LOOP #While LOOP #While LOOP #While LOOP

x = 1
while x <= 5:
    print(x)
    x += 1



current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1




    prompt = "\nTell me something, and I will repeat it back to you:"
    prompt += "\nYOu could end the program by typing 'quit'.\n "
    message = ""
    while message != 'quit':
        message = input(prompt)
        print(message)




        prompt = "\nTell me something, and I will repeat it back to you:"
        prompt += "\nYOu could end the program by typing 'quit'.\n "
        message = ""
        while message != 'quit':
            message = input(prompt)
            if message != 'quit':   #BY ADDING THIS PROGRAM WILL NOT PRINT "quit" IT WILL JUST QUIT THE PROGRAM
                print(message)


#FLAG #FLAG #FLAG #FLAG #FLAG #FLAG #FLAG #FLAG #FLAG #FLAG #FLAG #FLAG




prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)




#break #break #break #break #break #break #break #break #break #break


        prompt = "\nPlease enter the name of a city you have visited:"
        prompt += "\n(Enter 'quit' when you are finished.) "

        while True:
            city = input(prompt)
            if city == 'quit':
                break
            else:
                print(f"I'd love to go to {city.title()}!")








                # Start with users that need to be verified,
                # and an empty list to hold confirmed users.
                unconfirmed_users = ['alice', 'brian', 'candace']
                confirmed_users = []
                # Verify each user until there are no more unconfirmed users.
                # Move each verified user into the list of confirmed users.
                while unconfirmed_users:
                    current_user = unconfirmed_users.pop()

                    print(f"Verifying user: {current_user.title()}")
                    confirmed_users.append(current_user)

                    # Display all confirmed users.
                print("\nThe following users have been confirmed:")
                for confirmed_user in confirmed_users:
                    print(confirmed_user.title())



# REMOVING ALL REPETATION OF A PERTICULAR Value

                    pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
                    print(pets)
                    while 'cat' in pets:
                        pets.remove('cat')
                    print(pets)





                    responses = {}
                    # Set a flag to indicate that polling is active.
                    polling_active = True
                    while polling_active:
                    # Prompt for the person's name and response.
                        name = input("\nWhat is your name? ")
                        response = input("Which mountain would you like to climb someday? ")

                        # Store the response in the dictionary.
                        responses[name] = response
                        # Find out if anyone else is going to take the poll.
                        repeat = input("Would you like to let another person respond? (yes/ no) ")
                        if repeat == 'no':
                            polling_active = False
                    # Polling is complete. Show the results.
                    print("\n--- Poll Results ---")
                    for name, response in responses.items():
                        print(f"{name} would like to climb {response}.")


                        RESULT

>>>>>>What is your name? Arsh
Which mountain would you like to climb someday? Raydih Pahad
Would you like to let another person respond? (yes/ no) yes

What is your name? Again Arsh
Which mountain would you like to climb someday? Damguru Pahad
Would you like to let another person respond? (yes/ no) no

--- Poll Results ---
Arsh would like to climb Raydih Pahad.
Again Arsh would like to climb Damguru Pahad.<<<<<<<<<<




format format format format format format format format format format format format format 



To make sure a string will display as expected, we can format the result with the format() method.

String format()
The format() method allows you to format selected parts of a string.

Sometimes there are parts of a text that you do not control, maybe they come from a database, or user input?

To control such values, add placeholders (curly brackets {}) in the text, and run the values through the format() method:


name=input("Please enter your name.")
#Type your answer here.
str="Hello!, {}".format(name)

 
print(str)
>>>>>>>>>>>>
Hello!, arsh

print("{}".format(1))
>>>>>>>>>>>>>>>>
1


str= "{}, {}, {}".format(1, 2, 3)

print(str)
>>>>>>>>>>>>>
1, 2, 3



str="One year has {2} months, {0} weeks and {1} days.".format(52, 365, 12)
print(str)
>>>>>>>>>>>>>>>>>>>>
One year has 12 months, 52 weeks and 365 days.



Example
Add a placeholder where you want to display the price:

price = 49
txt = "The price is {} dollars"
print(txt.format(price))


###Format the price to be displayed as a number with two decimals:
price = 49
txt = "The price is {:.2f} dollars"
print(txt.format(price))
>>>>>>>>>>>>>>>>>>>>>>>
The price is 49.00 dollars



#####Multiple Values
If you want to use more values, just add more values to the format() method:


quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))
>>>>>>>>>>>>>>>>>>>>
I want 3 pieces of item number 567 for 49.00 dollars.




######Index Numbers
You can use index numbers (a number inside the curly brackets {0}) to be sure the values are placed in the correct placeholders:

Example
quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))
>>>>>>>>>>>>>>>>>>>
I want 3 pieces of item number 567 for 49.00 dollars.





####Also, if you want to refer to the same value more than once, use the index number:
age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))
>>>>>>>>>>>>>>>>>>
His name is John. John is 36 years old.




######Named Indexes
You can also use named indexes by entering a name inside the curly brackets {carname}, but then you must use names when you pass the parameter values txt.format(carname = "Ford"):

Example
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))
>>>>>>>>>>>>>>>>>....
I have a Ford, it is a Mustang.










-----------------------------------------------------------------------------------------------------------------

FILE FILE FILE FILE FILE FILE FILE FILE FILE FILE FILE FILE FILE FILE FILE  

-----------------------------------------------------------------------------------------------------------------

###How to open an existing txt file.
#This code will give us a file handle The file handle is not the actual data contained in the file, but instead it is a “handle” that we can use to read the data. You are given a handle if the requested file exists and you have the proper permissions to read the file.
variable = open('mbox.txt')    
print(variable)
>>>>>>>>>>>>>>>>>>>>
<_io.TextIOWrapper name='mbox.txt' mode='r' encoding='UTF-8'>



####To Count the total line in a txt file.
text = open("mbox.txt")
count = 0
for line in text:
    count = count + 1
print(f"Total line in the file = {count}")
>>>>>>>>>>>>>>>>>>>>
Total line in the file = 132045
###The above program starts with "open" statement can count the lines in any size of file using very little memory since each line is read, counted, and then discarded.



###If you know the file is relatively small compared to the size of your main memory,
you can read the whole file into one string using the read method on the file handle.
bnb = open('mbox-short.txt')
x = bnb.read()
print(len(x))



#How to OPEN AND READ A COMPLETE FILE

bnb = open('mbox-short.txt')
x = bnb.read()              #This will read the complete file and store the output in x.
print(x)
###It is a good idea to store the output of read as a variable(x) because each call to read exhausts the resource.


Range
bnb = open('mbox-short.txt')
x = bnb.read()
print(x[100:400])



#LINE STARTSWITH 

str="There are no traffic jams along the extra mile."
#  Type your code here.

ans_1= str.startswith("A")


print(ans_1)
>>>>>>>>>>>>>>>>>>>>>
False



fhand = open('mbox-short.txt')
for line in fhand:
    if line.startswith('From:'):
        print(line)



fhand = open('mbox-short.txt')
for line in fhand:
    line = line.strip()             #To get line without blank lines in between.
    if line.startswith('From:'):
        print(line)



#Pattern of skipping uninteresting lines.
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
# Skip 'uninteresting lines' through continue statement.
    if not line.startswith('From:'):
        continue
# Process our 'interesting' line
    print(line)

###USAGE OF endswith()

str="There are no traffic jams along the extra mile."
#  Type your code here.


ans_1= str.endswith(".")


print(ans_1)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>.
True




####How to create a txt File.

myfile = open('myfile.txt', 'w')            #This will create an empty txt file and open it.
myfile.write("Hello Arsh, I am Arsh and I have created this file just now at 3:50 pm 20 Aprail. And also wrote this line to check if this line will execute in the myfile.txt or not. So, Let's try this.\n")                 #This will write a line of sentence in the txt file.

myfile.write("\tNow Goodbye! Have a Nice Day!\n")
myfile.close()           #this will close the file.



myfile = open("myfile.txt", "w")   
myfile.write("\n\t\tHello after opening myfile for the next time. But this will overwrite and replace existing line. typed last time\n")  #this will replace existing line. typed last time
myfile.close()           #this will close the file.

###how to open and READ file


myfile = open('myfile.txt')
print(myfile.readline())            #This will display first line.
print(myfile.readline())            #This will display second line.
print(myfile.readline())            #This will display third line.
print(myfile.readline())            #This will display the fourth line.

print(open("myfile.txt").read())      #This code will display all line at once.

bnb = open("pi.txt")
for b in bnb:
    print(b)


#####Line count:

bnb = open("pi.txt")
line = 0
for b in bnb:
    line = line + 1
print("Line Count: ", line)



#HOW TO OPEN A FILE THROUGH PYTHON

with open('pi.txt') as file_object:
    contents = file_object.read()
print(contents)

#to remove extra blank line at the end of the output(find it on print)

with open('pi.txt') as file_object:
    contents = file_object.read()
print(contents.rstrip())


#normal File Paths
with open('text_files/pi.txt') as file_object: # here text_files is a folder.
    contents = file_object.read()
print(contents.rstrip())



#complex File Paths
file_path = '/home/arsh/code/text_files/bnb/pi.txt'
# here home, code and text_files is a folder.
with open(file_path) as file_object:
    contents = file_object.read()
print(contents.rstrip())



#Reading Line by Line
filename = 'pi.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())


        #Making a List of Lines from a File
        filename = 'pi.txt'
        with open(filename) as file_object:
            lines = file_object.readlines()

        for line in lines:
            print(line.rstrip())


            #Writing to an Empty File
            filename = 'pi.txt'
            with open(filename, 'w') as file_object:
                file_object.write("I love programming.")
                #this code replace the existing text with this new text_files



                #Writing Multiple Lines
                filename = 'pi.txt'
                with open(filename, 'w') as file_object:
                    file_object.write("I love programming.\n")
                    file_object.write("And I am a Data Sceientist.\n")




#Writing Multiple Lines
filename = 'pi.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("And I am a Data Sceientist.\n")


     




















-----------------------------------------------------------------------------------------------------------------

CLASS/Object  CLASS/Object  CLASS/Object  CLASS/Object  CLASS/Object  CLASS
CLASS/Object  CLASS/Object  CLASS/Object  CLASS/Object  CLASS/Object  CLASS

-----------------------------------------------------------------------------------------------------------------


Almost everything in Python is an object, with its properties and methods.

A Class is like an object constructor, or a "blueprint" for creating objects.

Create a Class
To create a class, use the keyword class





####Create a class named MyClass, with a property named x:
class MyClass:
  x = 5
print(MyClass)
>>>>>>>>>>>>>
<class '__main__.MyClass'>



Create Object
Now we can use the class named MyClass to create objects:

Example
Create an object named p1, and print the value of x:


class MyClass:
    x = 5

p1 = MyClass()
print(p1.x)
>>>>>>>>>>>
5



The __init__() Function
The examples above are classes and objects in their simplest form, and are not really useful in real life applications.

To understand the meaning of classes we have to understand the built-in __init__() function.

All classes have a function called __init__(), which is always executed when the class is being initiated.

Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:


##########Create a class named Person, use the __init__() function to assign values for name and age:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
>>>>>>>>>>>>>>>>>>>>>>.
John
36

#####Note: The __init__() function is called automatically every time the class is being used to create a new object.




#Print the name of the first_item.
class Jets:


    def __init__(self, name, country):
        self.name = name
        self.origin = country
        
first_item = Jets("F16", "USA")

a= first_item.name
print(a)
>>>>>>>>>>>>>>>>>>>>>>>
F16



#Print name of all jets.
class Jets:
    model = None
    country = 0

    def __init__(self, name, country):
        self.name = name
        self.origin = country

first_item=Jets("F14", "USA")
second_item=Jets("SU33", "Russia")
third_item=Jets("AJS37", "Sweden")
fourth_item=Jets("Mirage2000", "France")
fifth_item=Jets("Mig29", "USSR")
sixth_item=Jets("A10", "USA")

first_army=[first_item.name,second_item.name,third_item.name,fourth_item.name
,fifth_item.name,sixth_item.name]

print(first_army)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
['F14', 'SU33', 'AJS37', 'Mirage2000', 'Mig29', 'A10']


#Adding another attribute called "quantity". Then Adding quantity of Jets
class Jets:
    model = None
    country = 0

    def __init__(self, name, country, quantity):
        self.name = name
        self.origin = country
        self.quantity = quantity


first_item= Jets("F14", "USA", 87) 
second_item= Jets("Mirage2000", "France", 35) 

total= first_item.quantity + second_item.quantity
print(total)
>>>>>>>>>>>>>>>>>>>>>>.
122


#Nobel price winner.
class Nobel:
    def __init__(self, categories, years, winners):
        self.category = categories
        self.year = years
        self.winner = winners

np2005=Nobel("Peace", 2005, "Muhammad Yunus")
print(np2005.category, np2005.year, np2005.winner)
>>>>>>>>>>>>>>>>>>>>.
Peace 2005 Muhammad Yunus



#Simple class and function
class myfunc:
    def fifth(x):
        return x ** 5


ans= myfunc.fifth(2)

print(ans)
>>>>>>>>>>>>
32
3125





#__str__ function can be used to return a string representation for the class when needed.
class Nobel:
    def __init__(self, categories, years, winners):
        self.category = categories
        self.year = years
        self.winner = winners
 
    def __str__ (self):
                return "{} was the winner of Nobel {} Prize in {}".format(self.winner, self.category, self.year)
           
np2005=Nobel("Peace", 2005, "Muhammad Yunus")
print(np2005)
>>>>>>>>>>>>>>>>>>>>>>>>>>
Muhammad Yunus was the winner of Nobel Peace Prize in 2005




#x will be the number being raised and y will be the power. add a string representation quickly, so that when a user prints the class they get a meaningful description.
class myfunc:
    def power(x, y):
        return x ** y

    def __str__(self):
        return "Myfunc is a class which is capable of mathematical operations like raising a number to a power with power function."

ans1 = myfunc.power(5, 6)
ans2 = myfunc()

print(ans1)
print(ans2)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
15625
Myfunc is a class which is capable of mathematical operations like raising a number to a power with power function.




#Class Inheritence from Scratch. From scratch create a new class named AJS37. Make it inherit from the parent class Jets. This jet should have an origin attribute of Sweden and name attribute of AJS37. Assign an instance of the new class to the variable b.

class Jets:
    model = None
    country = 0

    def __init__(self, name, country):
        self.type = "Jet"
        self.area = "Air"
        self.name = name
        self.origin = country
        
class AJS37(Jets):
    def __init__(self):
        self.name = "AJS37"
        self.origin = "Sweden"

b=AJS37()
print(b.name) 
print(b.origin)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


-----------------------------------------------------------------------------------------------------
###IS CODE KO SUDHARNA HAI AUR EASY BANANA HAI
class Person:

    def __init__(intro, name, roll_no):
        intro.name = name
        intro.roll_no = roll_no

p1 = Person("Arsh", "27")
p2 = Person("Zihan", "7")

want = input("What do you want ? Do you want your roll number?[y/n]: ")

if want.lower() == "y": 
    name = input("Happy to know that you are an tentetive student!\nNow please inter your name Here Please: ")
    if name.lower() == "arsh":
        print(p1.roll_no)
    elif name.lower() == "zihan":
        print(p2.roll_no)
    else:
        print("Unfortunately you are not in the list of Admission student")

else:
    print("Feeling sorry to know that you don't behave like a Good Student!")
---------------------------------------------------------------------------------------------------



Object Methods
Objects can also contain methods. Methods in objects are functions that belong to the object.

Let us create a method in the Person class:

#######Insert a function that prints a greeting, and execute it on the p1 object:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()
>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Hello my name is John


####Note: The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.


The self Parameter
The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:


########Use the words mysillyobject and abc instead of self:

class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()
>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Hello my name is John




#######Modify Object Properties
You can modify properties on objects like this:

##########Set the age of p1 to 40:                p1.age = 40

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)

p1.age = 40                            #######Set the age of p1 to 40

print(p1.age)
>>>>>>>>>>>>>>>>
40




######Delete the age property from the p1 object:     del p1.age  
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)

del p1.age                   ##############Delete the age property from the p1 object

print(p1.age)
>>>>>>>>>>>>>>>>>>>>>
Traceback (most recent call last):
  File "demo_class7.py", line 13, in <module>
    print(p1.age)
AttributeError: 'Person' object has no attribute 'age'



##########Delete the p1 object:    del p1 

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)

del p1                          ##########Delete the p1 object:

print(p1)
>>>>>>>>>>>>>>>>>>>>>>>>
Traceback (most recent call last):
  File "demo_class8.py", line 13, in <module>
    print(p1)
NameError: 'p1' is not defined





########The pass Statement
class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.

Example
class Person:
  pass
# having an empty class definition like this, would raise an error without the pass statement
>>>>>>>>>>>>>>>>>>>
















-----------------------------------------------------------------------------------------------------------------

INHERITANCE INHERITANCE INHERITANCE INHERITANCE INHERITANCE Inheritanc INHERITANCE INHERITANCE INHERITANCE INHERITANCE INHERITANCE Inheritanc

-----------------------------------------------------------------------------------------------------------------


Inheritance allows us to define a class that inherits all the methods and properties from another class.

Parent class is the class being inherited from, also called base class.

Child class is the class that inherits from another class, also called derived class.

Create a Parent Class
Any class can be a parent class, so the syntax is the same as creating any other class:

###Create a class named Person, with firstname and lastname properties, and a printname method:

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()
>>>>>>>>>>>>>>>>>>>>>>
John Doe



###Create a Child Class
To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class:

Example
Create a class named Student, which will inherit the properties and methods from the Person class:

class Student(Person):
  pass


########Now Use the Student class to create an object, and then execute the printname method:
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  pass

x = Student("Mike", "Olsen")        ####Use the Student class to create an object
x.printname()
>>>>>>>>>>>>>>>>>>>
Mike Olsen


####Add the __init__() Function
So far we have created a child class that inherits the properties and methods from its parent.

We want to add the __init__() function to the child class (instead of the pass keyword).

Add the __init__() function to the Student class:

class Student(Person):
  def __init__(self, fname, lname):
    #add properties etc.

########When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.

Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.

####To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

x = Student("Mike", "Olsen")
x.printname()
>>>>>>>>>>>>>>>>>>>>>
Mike Olsen


######Now we have successfully added the __init__() function, and kept the inheritance of the parent class, and we are ready to add functionality in the __init__() function.

Use the super() Function
Python also has a super() function that will make the child class inherit all the methods and properties from its parent:

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

x = Student("Mike", "Olsen")
x.printname()
>>>>>>>>>>>>>
Mike Olsen

By using the super() function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent.


#######Add Properties
Example
Add a property called graduationyear to the Student class:

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019

x = Student("Mike", "Olsen")
print(x.graduationyear)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
2019

########In the example below, the year 2019 should be a variable, and passed into the Student class when creating student objects. To do so, add another parameter in the __init__() function:

###Add a year parameter, and pass the correct year when creating objects:
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019)
print(x.graduationyear)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>
2019


######Add Methods
Example
Add a method called welcome to the Student class:

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2019)
x.welcome()
>>>>>>>>>>>>>>>>>>>>>>>>>>>
Welcome Mike Olsen to the class of 2019

##########If you add a method in the child class with the same name as a function in the parent class, the inheritance of the parent method will be overridden.







-----------------------------------------------------------------------------------------------------------------

RegEx RegEx RegEx RegEx RegEx RegEx RegEx RegEx RegEx RegEx RegEx RegEx   

-----------------------------------------------------------------------------------------------------------------

It's like a Programming Language for String Matching.



A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.

RegEx can be used to check if a string contains the specified search pattern.

RegEx Module
Python has a built-in package called re, which can be used to work with Regular Expressions.


####Import the re module:
import re

###When you have imported the re module, you can start using regular expressions:
###Search the string to see if it starts with "The" and ends with "Spain":
import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)



##RegEx Functions
The re module offers a set of functions that allows us to search a string for a match:

findall-	Returns a list containing all matches
search-	Returns a Match object if there is a match anywhere in the string
split	 -  Returns a list where the string has been split at each match
sub	 -  Replaces one or many matches with a string


###Metacharacters
Metacharacters are characters with a special meaning:

[]	A set of characters	                                                "[a-m]"	
\	Signals a special sequence (can also be used to escape special characters)	    "\d"	
.	Any character (except newline character)	                                "he..o"	
^	Starts with	                                                        "^hello"	
$	Ends with	                                                        "planet$"	
*	Zero or more occurrences	                                            "he.*o"	
+	One or more occurrences	                                            "he.+o"	
?	Zero or one occurrences	                                            "he.?o"	
{}	Exactly the specified number of occurrences	                            "he.{2}o"	
|	Either or	                                                        "falls | stays"	
()	Capture and group



##Special Sequences
A special sequence is a \ followed by one of the characters in the list below, and has a special meaning:

\A	Returns a match if the specified characters are at the beginning of the string	"\AThe"	

\b	Returns a match where the specified characters are at the beginning or at the end of a word
(the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\bain"
r"ain\b"	

\B	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
(the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\Bain"
r"ain\B"	

\d	Returns a match where the string contains digits (numbers from 0-9)	"\d"	

\D	Returns a match where the string DOES NOT contain digits	"\D"	

\s	Returns a match where the string contains a white space character	"\s"	

\S	Returns a match where the string DOES NOT contain a white space character	"\S"	

\w	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)	"\w"	

\W	Returns a match where the string DOES NOT contain any word characters	"\W"	

\Z	Returns a match if the specified characters are at the end of the string	"Spain\Z"


MATCHING AND  EXTRACTING DATA
#####Sets
A set is a set of characters inside a pair of square brackets [] with a special meaning:

[0-9]	Returns a match for any digit between 0 and 9
[a-zA-Z]	Returns a match for any character alphabetically between a and z, lower case OR upper case



#######The findall() Function
The findall() function returns a list containing all matches.

Example
Print a list of all matches:

import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)
#The list contains the matches in the order they are found.
#If no matches are found, an empty list is returned:


###Return an empty list if no match was found:
import re

txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)



#####The search() Function
The search() function searches the string for a match, and returns a Match object if there is a match.

If there is more than one match, only the first occurrence of the match will be returned:

Example
Search for the first white-space character in the string:

import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())
#########If no matches are found, the value None is returned:



#######Make a search that returns no match:
import re

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)


####The split() Function
The split() function returns a list where the string has been split at each match:

##Split at each white-space character:
import re

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)
#You can control the number of occurrences by specifying the maxsplit parameter:


###Split the string only at the first occurrence:
import re

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)



##The sub() Function
The sub() function replaces the matches with the text of your choice:
#Replace every white-space character with the number 9:
import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)
#You can control the number of replacements by specifying the count parameter:



#Replace the first 2 occurrences:
import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)



##Match Object
A Match Object is an object containing information about the search and the result.

Note: If there is no match, the value None will be returned, instead of the Match Object.

#Do a search that will return a Match Object:
import re

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) #this will print an object






The Match object has properties and methods used to retrieve information about the search, and the result:

.span() returns a tuple containing the start-, and end positions of the match.
.string returns the string passed into the function
.group() returns the part of the string where there was a match

#Print the position (start- and end-position) of the first match occurrence.
#The regular expression looks for any words that starts with an upper case "S":
import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())  
#.span() returns a tuple containing the start-, and end positions of the match.


#Print the string passed into the function:
import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)
#.string returns the string passed into the function

#Print the part of the string where there was a match.
#The regular expression looks for any words that starts with an upper case "S":
import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)g
print(x.group())
#.group() returns the part of the string where there was a match

#Note: If there is no match, the value None will be returned, instead of the Match Object.



-----------------------------------------------------------------------------------------------------------------

RANDOM RANDOM RANDOM RANDOM RANDOM RANDOM RANDOM RANDOM 

-----------------------------------------------------------------------------------------------------------------



##Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:


import random
print(random.randrange(1, 10))


import random              #This will import "random" module

print(random.random())          #This will give us a random number below 1 like 0.0223 



import random
print(random.randint(1, 100))       #This will give us a random number from 1 to 100



import random              
#This will give us a random password from the list
print(random.choice(['Arsh88099', '88099Arsh', 'Arsh88Ar0s99h']))



#This will shuffle the list and randomise a list.
import random
suits = ['hearts', 'clubs', 'diamonds', 'spades']
random.shuffle(suits)
print(suits)





------------------------------------------------------------------------------------------------------

SPACE in BITWEEN 

myjob = "hacker"
for c in myjob: print(c, end=' ')







Try / Except  |  Try / Except  |  Try / Except  |  Try / Except  |  Try / Except  |  Try / Except  |  Try / Except  |  Try / Except  |  Try / Except  |  Try / Except  |  




#.get() is not a list method. Place pass keyword to the right line so that program doesn't throw an error.
#Type your code here.

a = [1, 3, 5]
try:
    a.get()
except:
    pass

print(a)
>>>>>>>>>>>>>>>>>>
[1, 3, 5]




#Place msg="You can't add int to string" to the right place so that program avoids BaseExceptionError.
a="Hello World!"
try:
    a + 10
except: 
    msg="You can't add int to string"

print(msg)
>>>>>>>>>>>>>>>>>>>>>>
You can't add int to string




#Place msg="You're out of list range" to avoid IndexError.
lst=[5, 10, 20]

try:
    print(lst[5])
except:
    msg="You're out of list range"

print(msg)
>>>>>>>>>>>>>>>>>>>>>
You're out of list range










-----------------------------------------------------------------------------------------------------------------

NumPy NumPy NumPy NumPy NumPy NumPy NumPy NumPy NumPy NumPy NumPy 

-----------------------------------------------------------------------------------------------------------------




import numpy

x = numpy.array([1, 2, 3, 4, 5])

print(x)
>>>>>>>>>>>>>>>>>>>>>>>
[1 2 3 4 5]


NumPy as np
NumPy is usually imported under the np alias.

alias: In Python alias are an alternate name for referring to the same thing.
>>>>>>>>>>>import numpy as np




import numpy as np

x = np.array([1, 2, 3, 4, 5])

print(x)
>>>>>>>>>>>>>>>>>>>>>>>
[1 2 3 4 5]



NumPy is used to work with arrays. The array object in NumPy is called ndarray.

We can create a NumPy ndarray object by using the array() function.




import numpy as np 

x = np.array([1, 2, 3, 4])
print(x)

print(type(x))
>>>>>>>>>>>>>>>>
[1 2 3 4]
<class 'numpy.ndarray'>




##Use a tuple to create a NumPy array:

import numpy as np

x = np.array((1, 2, 4, 6, 6))

print(x)

print(type(x))
>>>>>>>>>>>>>>>>>>>>>>>>>>>.
[1 2 4 6 6]
<class 'numpy.ndarray'>




#0-D arrays, or Scalars, are the elements in an array. Each value in an array is a 0-D array.
#Create a 0-D array with value 42

import numpy as np

arr = np.array(42)

print(arr)
>>>>>>>>>>>>>>>>>>
42
<class 'numpy.ndarray'>



####1-D Arrays
An array that has 0-D arrays as its elements is called uni-dimensional or 1-D array.

These are the most common and basic arrays.

Example
Create a 1-D array containing the values 1,2,3,4,5:

import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)
>>>>>>>>>>>>>>>>>>>>>>>>
[1 2 3 4 5]


####2-D Arrays
An array that has 1-D arrays as its elements is called a 2-D array.

These are often used to represent matrix or 2nd order tensors.



import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr)

>>>>>>>>>>>>>>>>>>>>
[[1 2 3]
 [4 5 6]]


3-D arrays
An array that has 2-D arrays (matrices) as its elements is called 3-D array.

These are often used to represent a 3rd order tensor.


#Example
#Create a 3-D array with two 2-D arrays, both containing two arrays with the values 1,2,3 and 4,5,6:

import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(arr)
>>>>>>>>>>>>>>>>>>>>
[[[1 2 3]
  [4 5 6]]

 [[1 2 3]
  [4 5 6]]]






###Check Number of Dimensions?
NumPy Arrays provides the ndim attribute that returns an integer that tells us how many dimensions the array have.

Example
Check how many dimensions the arrays have:

import numpy as np

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)
>>>>>>>>>>>>>>>>>>>>>>>>>
0
1
2
3





#Higher Dimensional Arrays
An array can have any number of dimensions.

import numpy as np

e = np.array([[[[[1, 2, 3, 4], [2, 4, 5, 9], [3,4, 5, 8], [0, 7, 3, 5]]]]])


print(e.ndim)
print("\n")
print(e)
>>>>>>>>>>>>>>>>>>>>
5

[[[[[1 2 3 4]
    [2 4 5 9]
    [3 4 5 8]
    [0 7 3 5]]]]]



When the array is created, you can define the number of dimensions by using the "ndmin" argument.

##Create an array with 5 dimensions and verify that it has 5 dimensions:

import numpy as np

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('number of dimensions :', arr.ndim)
>>>>>>>>>>>>>>>>>>>
[[[[[1 2 3 4]]]]]
number of dimensions : 5



Example
Get the first element from the following array:

import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr[0])
>>>>>>>>>>>>>>>>>>>>>>>>>
1


Get the fourth, first and second element from the following array.

import numpy as np

x = np.array([2, 4, 5, 6])

print(x[3], x[0], x[1])
>>>>>>>>>>>>>>>>.
6 2 4


Get third and fourth elements from the following array and add them.

import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr[2] + arr[3])
>>>>>>>>>>>>>>>>>>>>>>>
7




Access 2-D Arrays
To access elements from 2-D arrays we can use comma separated integers representing the dimension and the index of the element.

Access the element on the first row, second column:

import numpy as np

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('2nd element on 1st row: ', arr[0, 1])

>>>>>>>>>>>>>>>>>>>>>>>>>>
2nd element on 1st dim:  2



Access the element on the 2nd row, 5th column:

import numpy as np

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('5th element on 2nd row: ', arr[1, 4])
>>>>>>>>>>>>>>>>>>>>>.
5th element on 2nd dim:  10


###Access 3-D Arrays
To access elements from 3-D arrays we can use comma separated integers representing the dimensions and the index of the element.

Example
Access the third element of the second array of the first array:

import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr[0, 1, 2])
>>>>>>>>>>>>>>>>>>>>>>>.
6          

^^^^^
Example Explained
arr[0, 1, 2] prints the value 6.

And this is why:

The first number represents the first dimension, which contains two arrays:
[[1, 2, 3], [4, 5, 6]]
and:
[[7, 8, 9], [10, 11, 12]]
Since we selected 0, we are left with the first array:
[[1, 2, 3], [4, 5, 6]]

The second number represents the second dimension, which also contains two arrays:
[1, 2, 3]
and:
[4, 5, 6]
Since we selected 1, we are left with the second array:
[4, 5, 6]

The third number represents the third dimension, which contains three values:
4
5
6
Since we selected 2, we end up with the third value:
6


###Negative Indexing
Use negative indexing to access an array from the end.

Example
Print the last element from the 2nd dim:

import numpy as np

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('Last element from 2nd dim: ', arr[1, -1])
>>>>>>>>>>>>>>>>>>>>>>>>>>.
Last element from 2nd dim:  10




####Slicing arrays
Slicing in python means taking elements from one given index to another given index.

We pass slice instead of index like this: [start:end].

We can also define the step, like this: [start:end:step].

If we don't pass start its considered 0

If we don't pass end its considered length of array in that dimension

If we don't pass step its considered 1




###Slice elements from index 1 to index 5 from the following array:

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5])
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[2 3 4 5]
Note: The result includes the start index, but excludes the end index.



Slice elements from index 4 to the end of the array:

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[4:])
>>>>>>>>>>>>>>>>>>
[5 6 7]


##Slice elements from the beginning to index 4 (not included):

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[:4])
>>>>>>>>>>>>>>>>>>>>>>
[1 2 3 4]



##Slice from the index 3 from the end to index 1 from the end:

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[-3:-1])
>>>>>>>>>>>>>>>>>>>..
[5 6]



STEP
Use the step value to determine the step of the slicing:

Example
Return every other element from index 1 to index 5:

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5:2])
>>>>>>>>>>>>>>>>>>>>>>>>
[2 4]



Return every other element from the entire array:

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[::2])
>>>>>>>>>>>>>>>>..
[1 3 5 7]



##Slicing 2-D Arrays
Example
From the second element, slice elements from index 1 to index 4 (not included):

import numpy as np

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[1, 1:4])
>>>>>>>>>>>>>>>>>>>>>>>>>>>.
[7 8 9]



From both elements, return index 2:

import numpy as np

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[0:2, 2])
>>>>>>>>>>>>>>>>>>>>>>>>>
[3 8]


From both elements, slice index 1 to index 4 (not included), this will return a 2-D array:

import numpy as np

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[0:2, 1:4]) #You could also write "print(arr[0:, 1:4])".
>>>>>>>>>>>>>>>>>>>>>>>>>>>>.
[[2 3 4]
 [7 8 9]]


##Shape of an Array
The shape of an array is the number of elements in each dimension.

Get the Shape of an Array
NumPy arrays have an attribute called shape that returns a tuple with each index having the number of corresponding elements.


Print the shape of a 2-D array:

import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(arr.shape)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.
(2, 4)

The example above returns (2, 4), which means that the array has 2 dimensions, where the first dimension has 2 elements and the second has 4.
Means,
2 row and 4 columns.


Create an array with 5 dimensions using ndmin using a vector with values 1,2,3,4 and verify that last dimension has value 4:

import numpy as np

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('shape of array :', arr.shape)
>>>>>>>>>>>>>>>>>>>>>>>>.
[[[[[1 2 3 4]]]]]
shape of array : (1, 1, 1, 1, 4)


Integers at every index tells about the number of elements the corresponding dimension has.

In the example above at index-4 we have value 4, so we can say that 5th ( 4 + 1 th) dimension has 4 elements.


###Reshaping arrays
Reshaping means changing the shape of an array.

The shape of an array is the number of elements in each dimension.

By reshaping we can add or remove dimensions or change number of elements in each dimension.


#Reshape From 1-D to 2-D
Convert the following 1-D array with 12 elements into a 2-D array.
The outermost dimension will have 4 arrays, each with 3 elements:


import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
print(newarr)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[[ 1  2  3]
 [ 4  5  6]
 [ 7  8  9]
 [10 11 12]]


###Reshape From 1-D to 3-D
Convert the following 1-D array with 12 elements into a 3-D array.

The outermost dimension will have 2 arrays that contains 3 arrays, each with 2 elements:

import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(2, 3, 2)
print(newarr)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[[[ 1  2]
  [ 3  4]
  [ 5  6]]

 [[ 7  8]
  [ 9 10]
  [11 12]]]


Iterating Arrays
Iterating means going through elements one by one.

As we deal with multi-dimensional arrays in numpy, we can do this using basic for loop of python.

If we iterate on a 1-D array it will go through each element one by one.

Example
Iterate on the elements of the following 1-D array:

import numpy as np

arr = np.array([1, 2, 3])

for x in arr:
  print(x)
>>>>>>>>>>>>>>>>>.
1
2
3



Iterating 2-D Arrays
In a 2-D array it will go through all the rows.

Example
Iterate on the elements of the following 2-D array:

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
  print(x)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>..
[1 2 3]
[4 5 6]



To return the actual values, the scalars, we have to iterate the arrays in each dimension.

Example
Iterate on each scalar element of the 2-D array:

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
  for y in x:
    print(y)
>>>>>>>>>>>>>>>>>>>...
1
2
3
4
5
6


Iterating 3-D Arrays
In a 3-D array it will go through all the 2-D arrays.

Example
Iterate on the elements of the following 3-D array:

import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
  print("x represents the 2-D array:")
  print(x)
>>>>>>>>>>>>>>>>>>>>>>>>>>>...
x represents the 2-D array:
[[1 2 3]
 [4 5 6]]
x represents the 2-D array:
[[ 7  8  9]
 [10 11 12]]



To return the actual values, the scalars, we have to iterate the arrays in each dimension.

Example
Iterate down to the scalars:

import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
  for y in x:
    for z in y:
      print(z)
>>>>>>>>>>>>>>>>>>>>>>>>>...
1
2
3
4
5
6
7
8
9
10
11
12



########Iterating Arrays Using nditer()
The function nditer() is a helping function that can be used from very basic to very advanced iterations. It solves some basic issues which we face in iteration, lets go through it with examples.

Iterating on Each Scalar Element
In basic for loops, iterating through each scalar of an array we need to use n for loops which can be difficult to write for arrays with very high dimensionality.

Example
Iterate through the following 3-D array:

import numpy as np

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):
  print(x)
>>>>>>>>>>>>>>>>>>>.
1
2
3
4
5
6
7
8


Iterating Array With Different Data Types
We can use "op_dtypes" argument and pass it the expected datatype to change the datatype of elements while iterating.

NumPy does not change the data type of the element in-place (where the element is in array) so it needs some other space to perform this action, that extra space is called buffer, and in order to enable it in nditer() we pass flags=['buffered'].

Example
Iterate through the array as a string:

import numpy as np

arr = np.array([1, 2, 3])

for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
  print(x)
>>>>>>>>>>>>>>>>>>>>>>....
b'1'
b'2'
b'3'



Iterating With Different Step Size
We can use filtering and followed by iteration.

Example
Iterate through every scalar element of the 2D array skipping 1 element:

import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for x in np.nditer(arr[:, ::2]):
  print(x)
>>>>>>>>>>>>>>>>>>>.....
1
3
5
7



Enumerated Iteration Using ndenumerate()
Enumeration means mentioning sequence number of somethings one by one.

Sometimes we require corresponding index of the element while iterating, the 
"ndenumerate()" method can be used for those usecases.

Example
Enumerate on following 1D arrays elements:

import numpy as np

arr = np.array([1, 2, 3])

for idx, x in np.ndenumerate(arr):
  print(idx, x)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>...
(0,) 1
(1,) 2
(2,) 3


Enumerate on following 2D array's elements:

import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for idx, x in np.ndenumerate(arr):
  print(idx, x)
>>>>>>>>>>>>>>>>>>>>>>...
(0, 0) 1
(0, 1) 2
(0, 2) 3
(0, 3) 4
(1, 0) 5
(1, 1) 6
(1, 2) 7
(1, 3) 8



#######Joining NumPy Arrays
Joining means putting contents of two or more arrays in a single array.

In SQL we join tables based on a key, whereas in NumPy we join arrays by axes.

We pass a sequence of arrays that we want to join to the concatenate() function, along with the axis. If axis is not explicitly passed, it is taken as 0.


Join two arrays

import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))

print(arr)
>>>>>>>>>>>>>>>.....
[1 2 3 4 5 6]


Join two 2-D arrays along rows (axis=1):

import numpy as np

arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7, 8]])

arr = np.concatenate((arr1, arr2), axis=1)

print(arr)
>>>>>>>>>>>>>>>>>>>>>>>>
[[1 2 5 6]
 [3 4 7 8]]



#oining Arrays Using Stack Functions
Stacking is same as concatenation, the only difference is that stacking is done along a new axis.

We can concatenate two 1-D arrays along the second axis which would result in putting them one over the other, ie. stacking.

We pass a sequence of arrays that we want to join to the stack() method along with the axis. If axis is not explicitly passed it is taken as 0.

Example
import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.stack((arr1, arr2), axis=1)

print(arr)
>>>>>>>>>>>>>>>>>.
[[1 4]
 [2 5]
 [3 6]]


Stacking Along Rows
NumPy provides a helper function: hstack() to stack along rows.

Example
import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.hstack((arr1, arr2))

print(arr)
>>>>>>>>>>>>>>>>>>>>...
[1 2 3 4 5 6]


Stacking Along Columns
NumPy provides a helper function: vstack()  to stack along columns.

Example
import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.vstack((arr1, arr2))

print(arr)
>>>>>>>>>>>>>>>>>>>>>>>.
[[1 2 3]
 [4 5 6]]



Stacking Along Height (depth)
NumPy provides a helper function: dstack() to stack along height, which is the same as depth.

Example
import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.dstack((arr1, arr2))

print(arr)
>>>>>>>>>>>>>>>>>>>>>>>>.
[[[1 4]
  [2 5]
  [3 6]]]




####Splitting NumPy Arrays
Splitting is reverse operation of Joining.

Joining merges multiple arrays into one and Splitting breaks one array into multiple.

We use array_split() for splitting arrays, we pass it the array we want to split and the number of splits.

Example
Split the array in 3 parts:

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print(newarr)
>>>>>>>>>>>>>>>>>>>>>>.....
[array([1, 2]), array([3, 4]), array([5, 6])]

Note: The return value is an array containing three arrays.

If the array has less elements than required, it will adjust from the end accordingly.



Split the array in 4 parts:

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 4)

print(newarr)
>>>>>>>>>>>>>>>>>>>>>>....
[array([1, 2]), array([3, 4]), array([5]), array([6])]

Note: We also have the method split() available but it will not adjust the elements when elements are less in source array for splitting like in example above, array_split() worked properly but split() would fail.



Split Into Arrays
The return value of the array_split() method is an array containing each of the split as an array.

If you split an array into 3 arrays, you can access them from the result just like any array element:

Example
Access the splitted arrays:

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print(newarr[0])
print(newarr[1])
print(newarr[2])
>>>>>>>>>>>>>>>>>>>
[1 2]
[3 4]
[5 6]


Splitting 2-D Arrays
Use the same syntax when splitting 2-D arrays.

Use the array_split() method, pass in the array you want to split and the number of splits you want to do.

Example
Split the 2-D array into three 2-D arrays.

import numpy as np

arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

newarr = np.array_split(arr, 3)

print(newarr)
>>>>>>>>>>>>>>>>>>>>>.
[array([[1, 2],
       [3, 4]]), array([[5, 6],
       [7, 8]]), array([[ 9, 10],
       [11, 12]])]


The example above returns three 2-D arrays.

Let's look at another example, this time each element in the 2-D arrays contains 3 elements.


Split the 2-D array into three 2-D arrays.

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.array_split(arr, 3)

print(newarr)
>>>>>>>>>>>>>>>>>>>>...
[array([[1, 2, 3],
       [4, 5, 6]]), array([[ 7,  8,  9],
       [10, 11, 12]]), array([[13, 14, 15],
       [16, 17, 18]])]

The example above returns three 2-D arrays.

In addition, you can specify which axis you want to do the split around.

The example below also returns three 2-D arrays, but they are split along the row (axis=1).

Example
Split the 2-D array into three 2-D arrays along rows.

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.array_split(arr, 3, axis=1)

print(newarr)
>>>>>>>>>>>>>>>>>>>>>>>.
[array([[ 1],
       [ 4],
       [ 7],
       [10],
       [13],
       [16]]), array([[ 2],
       [ 5],
       [ 8],
       [11],
       [14],
       [17]]), array([[ 3],
       [ 6],
       [ 9],
       [12],
       [15],
       [18]])]



An alternate solution is using hsplit() opposite of hstack()

Example
Use the hsplit() method to split the 2-D array into three 2-D arrays along rows.

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.hsplit(arr, 3)

print(newarr)

>>>>>>>>>>>>>>>>>>>>>>>
[array([[ 1],
       [ 4],
       [ 7],
       [10],
       [13],
       [16]]), array([[ 2],
       [ 5],
       [ 8],
       [11],
       [14],
       [17]]), array([[ 3],
       [ 6],
       [ 9],
       [12],
       [15],
       [18]])]
Note: Similar alternates to vstack() and dstack() are available as vsplit() and dsplit().


###Searching Arrays
You can search an array for a certain value, and return the indexes that get a match.

To search an array, use the where() method.

Example
Find the indexes where the value is 4:

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 4, 4])

x = np.where(arr == 4)

print(x)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>.
(array([3, 5, 6]),)

The example above will return a tuple: (array([3, 5, 6],)

Which means that the value 4 is present at index 3, 5, and 6.

Example
Find the indexes where the values are even:

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

x = np.where(arr%2 == 0)

print(x)
>>>>>>>>>>>>>
(array([1, 3, 5, 7]),)



Find the indexes where the values are odd:

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

x = np.where(arr%2 == 1)

print(x)
>>>>>>>>>>>>>>>>>>>
(array([0, 2, 4, 6]),)



Search Sorted
There is a method called searchsorted() which performs a binary search in the array, and returns the index where the specified value would be inserted to maintain the search order.

The searchsorted() method is assumed to be used on sorted arrays.

Example
Find the indexes where the value 7 should be inserted:

import numpy as np

arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7)

print(x)
>>>>>>>>>>>>>>>>>>>>>>>
1



Example explained: The number 7 should be inserted on index 1 to remain the sort order.

The method starts the search from the left and returns the first index where the number 7 is no longer larger than the next value.

Search From the Right Side
By default the left most index is returned, but we can give side='right' to return the right most index instead.

Example
Find the indexes where the value 7 should be inserted, starting from the right:

import numpy as np

arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7, side='right')

print(x)
>>>>>>>>>>>>>>>>>>.
2


Example explained: The number 7 should be inserted on index 2 to remain the sort order.

The method starts the search from the right and returns the first index where the number 7 is no longer less than the next value.

Multiple Values
To search for more than one value, use an array with the specified values.

Find the indexes where the values 2, 4, and 6 should be inserted:

import numpy as np

arr = np.array([1, 3, 5, 7])

x = np.searchsorted(arr, [2, 4, 6])

print(x)
>>>>>>>>>>>>>>>>...
[1 2 3]

The return value is an array: [1 2 3] containing the three indexes where 2, 4, 6 would be inserted in the original array to maintain the order.




####Sorting Arrays
Sorting means putting elements in an ordered sequence.

Ordered sequence is any sequence that has an order corresponding to elements, like numeric or alphabetical, ascending or descending.

The NumPy ndarray object has a function called sort(), that will sort a specified array.

Example
Sort the array:

import numpy as np

arr = np.array([3, 2, 0, 1])

print(np.sort(arr))
>>>>>>>>>>>>>>>>>>>>>>>>....
[0 1 2 3]



Note: This method returns a copy of the array, leaving the original array unchanged.

You can also sort arrays of strings, or any other data type:

Example
Sort the array alphabetically:

import numpy as np

arr = np.array(['banana', 'cherry', 'apple'])

print(np.sort(arr))
>>>>>>>>>>>>>>>>>>>>>>>>..
['apple' 'banana' 'cherry']


Sort a boolean array:

import numpy as np

arr = np.array([True, False, True])

print(np.sort(arr))
>>>>>>>>>>>>>>>>>>>>>>>>>>>..
[False True True]


Sorting a 2-D Array
If you use the sort() method on a 2-D array, both arrays will be sorted:

Example
Sort a 2-D array:

import numpy as np

arr = np.array([[3, 2, 4], [5, 0, 1]])

print(np.sort(arr))
>>>>>>>>>>>>>>>>>
[[2 3 4]
 [0 1 5]]



Filtering Arrays
Getting some elements out of an existing array and creating a new array out of them is called filtering.

In NumPy, you filter an array using a boolean index list.

A boolean index list is a list of booleans corresponding to indexes in the array.

If the value at an index is True that element is contained in the filtered array, if the value at that index is False that element is excluded from the filtered array.

Example
Create an array from the elements on index 0 and 2:

import numpy as np

arr = np.array([41, 42, 43, 44])

x = [True, False, True, False]

newarr = arr[x]

print(newarr)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.
[41 43]

The example above will return [41, 43], why?

Because the new filter contains only the values where the filter array had the value True, in this case, index 0 and 2.



##########Creating the Filter Array
In the example above we hard-coded the True and False values, but the common use is to create a filter array based on conditions.

Example
Create a filter array that will return only values higher than 42:

import numpy as np

arr = np.array([41, 42, 43, 44])

# Create an empty list
filter_arr = []

# go through each element in arr
for element in arr:
  # if the element is higher than 42, set the value to True, otherwise False:
  if element > 42:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)
>>>>>>>>>>>>>>>>>>>>>>.........
[False, False, True, True]
[43 44]



Create a filter array that will return only even elements from the original array:

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

# Create an empty list
filter_arr = []

# go through each element in arr
for element in arr:
  # if the element is completely divisble by 2, set the value to True, otherwise False
  if element % 2 == 0:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)
>>>>>>>>>>>>>>>>>>>>>>>>>>>..
[False, True, False, True, False, True, False]
[2 4 6]



Creating Filter Directly From Array
The above example is quite a common task in NumPy and NumPy provides a nice way to tackle it.

We can directly substitute the array instead of the iterable variable in our condition and it will work just as we expect it to.

Example
Create a filter array that will return only values higher than 42:

import numpy as np

arr = np.array([41, 42, 43, 44])

filter_arr = arr > 42

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)
>>>>>>>>>>>>>>>>>>>>>.
[False False  True  True]
[43 44]



Create a filter array that will return only even elements from the original array:

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

filter_arr = arr % 2 == 0

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)
>>>>>>>>>>>>>>>>>>>>>>.....
[False  True False  True False  True False]
[2 4 6]



#Generate Random Array
In NumPy we work with arrays, and you can use the two methods from the above examples to make random arrays.

Integers
The randint() method takes a size parameter where you can specify the shape of an array.




#Generate a 1-D array containing 5 random integers from 0 to 100:

from numpy import random

x=random.randint(100, size=(5))

print(x)
>>>>>>>>>>>>>>>>>>>>>>>>>>..
[10 69 13 60 67]



Generate a 2-D array with 3 rows, each row containing 5 random integers from 0 to 100:

from numpy import random

x = random.randint(100, size=(3, 5))

print(x)
>>>>>>>>>>>>>>>>>>>>.
[[34 94 41 26  5]
 [41 16 71 90 35]
 [65  5 75 63  9]]



Floats
The rand() method also allows you to specify the shape of the array.

#Generate a 1-D array containing 5 random floats:

from numpy import random

x = random.rand(5)

print(x)
>>>>>>>>>>>>>>>>>>>>>>>>>
[0.5936533  0.92531576 0.64479772 0.5348125  0.88886547]


Generate a 2-D array with 3 rows, each row containing 5 random numbers:

from numpy import random

x = random.rand(3, 5)

print(x)
>>>>>>>>>>>>>>>>>.
[[0.64384489 0.65309662 0.89583909 0.89011174 0.75035926]
 [0.43476732 0.83895076 0.36787689 0.92814137 0.67767383]
 [0.50322514 0.35703105 0.51281298 0.61065871 0.56402877]]


#Generate Random Number From Array
The choice() method allows you to generate a random value based on an array of values.

The choice() method takes an array as a parameter and randomly returns one of the values.

Example
Return one of the values in an array:

from numpy import random

x = random.choice([3, 5, 7, 9])

print(x)
>>>>>>>>>>>>>>>>>>>>>>>>>...
5




#The choice() method also allows you to return an array of values.

Add a size parameter to specify the shape of the array.

Example
Generate a 2-D array that consists of the values in the array parameter (3, 5, 7, and 9):

from numpy import random

x = random.choice([3, 5, 7, 9], size=(3, 5))

print(x)
>>>>>>>>>>>>>>>>>>>>>>>>>...
[[5 7 5 3 9]
 [5 3 5 5 7]
 [3 5 3 3 3]]



#What is Data Distribution?
Data Distribution is a list of all possible values, and how often each value occurs.

Such lists are important when working with statistics and data science.

The random module offer methods that returns randomly generated data distributions.


#Random Distribution
A random distribution is a set of random numbers that follow a certain probability density function.

Probability Density Function: A function that describes a continuous probability. i.e. probability of all values in an array.

We can generate random numbers based on defined probabilities using the choice() method of the random module.

The choice() method allows us to specify the probability for each value.

The probability is set by a number between 0 and 1, where 0 means that the value will never occur and 1 means that the value will always occur.



Generate a 1-D array containing 100 values, where each value has to be 3, 5, 7 or 9.

The probability for the value to be 3 is set to be 0.1

The probability for the value to be 5 is set to be 0.3

The probability for the value to be 7 is set to be 0.6

The probability for the value to be 9 is set to be 0

from numpy import random

x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))

print(x)
>>>>>>>>>>>>>>>>>>>>...
[7 5 3 5 7 5 5 5 5 5 7 7 7 5 7 7 7 7 7 3 7 5 5 7 7 7 3 7 5 3 7 5 7 7 5 5 7
 7 5 5 5 7 7 7 7 7 5 7 3 5 7 7 7 5 5 7 7 7 7 7 5 5 5 3 5 7 7 7 7 5 7 5 7 5
 7 5 3 5 7 5 7 7 3 5 7 7 5 7 7 3 7 7 7 3 7 5 7 7 3 7]

The sum of all probability numbers should be 1.

Even if you run the example above 100 times, the value 9 will never occur.

You can return arrays of any shape and size by specifying the shape in the size parameter.



#Same example as above, but return a 2-D array with 3 rows, each containing 5 values.

from numpy import random

x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5))

print(x)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>...
[[7 5 7 7 5]
 [7 5 5 7 5]
 [7 7 5 7 7]]



#####Random Permutations of Elements
A permutation refers to an arrangement of elements. e.g. [3, 2, 1] is a permutation of [1, 2, 3] and vice-versa.

The NumPy Random module provides two methods for this: shuffle() and permutation().

Shuffling Arrays
Shuffle means changing arrangement of elements in-place. i.e. in the array itself.

Example
Randomly shuffle elements of following array:

from numpy import random
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

random.shuffle(arr)

print(arr)
>>>>>>>>>>>>>>>>>>>>>>>>>.
[5 2 3 1 4]



###Generating Permutation of Arrays
Example
Generate a random permutation of elements of following array:

from numpy import random
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(random.permutation(arr))
>>>>>>>>>>>>>>>>>>>>>>>........
[4 3 5 1 2]



Note: The permutation() method returns a re-arranged array (and leaves the original array un-changed).
Note: The shuffle() method makes changes to the original array.






################################Matplotlib VS Seaborn##########################################


Matplotlib: It is a Python library used for plotting graphs with the help of other libraries like Numpy and Pandas.
    Matplotlib is well connected with Numpy and Pandas and acts as a graphics package for data visualization in python. Pyplot provides similar features and syntax as in MATLAB. Therefore, MATLAB users can easily study it.
    Matplotlib is a highly customized and robust.
    
Matplotlib is mainly deployed for basic plotting. Visualization using Matplotlib generally consists of bars, pies, lines, scatter plots and so on.
Matplotlib has multiple figures can be opened, but need to be closed explicitly. plt.close() only closes the current figure. plt.close(‘all’) would close em all.   


Seaborn: It is also a Python library used for plotting graphs with the help of Matplotlib, Pandas, and Numpy. It is built on the roof of Matplotlib and is considered as a superset of the Matplotlib library.It uses beautiful themes for decorating Matplotlib graphics. It acts as an important tool in picturing Linear Regression Models. It eliminates the overlapping of graphs and also aids in their beautification.
    Seaborn is more comfortable in handling Pandas data frames. It uses basic sets of methods to provide beautiful graphics in python.
    Seaborn avoids overlapping of plots with the help of its default themes.

Seaborn, on the other hand, provides a variety of visualization patterns. It uses fewer syntax and has easily interesting default themes. It specializes in statistics visualization and is used if one has to summarize data in visualizations and also show the distribution in the data. 
Seaborn automates the creation of multiple figures. This sometimes leads to OOM (out of memory) issues.
    If one is doing statistics then Seaborn is a good choice because it has a lot of things suitable for statistical tasks, built-in.


###Seaborn

Distplots
Distplot stands for distribution plot, it takes as input an array and plots a curve corresponding to the distribution of points in the array.

Import Matplotlib
Import the pyplot object of the Matplotlib module in your code using the following statement:
import matplotlib.pyplot as plt

#Import Seaborn
Import the Seaborn module in your code using the following statement:
    import seaborn as sns



#Plotting a Distplot

import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot([0, 1, 2, 3, 4, 5])

plt.show()



##Plotting a Distplot Without the Histogram

import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot([0, 1, 2, 3, 4, 5], hist=False)

plt.show()

Note: We will be using: sns.distplot(arr, hist=False) to visualize random distributions in this tutorial.



###Addition
The add() function sums the content of two arrays, and return the results in a new array.

Example
Add the values in arr1 to the values in arr2:

import numpy as np

arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])

newarr = np.add(arr1, arr2)

print(newarr)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>..
[30 32 34 36 38 40]




###Subtraction
Subtract the values in arr2 from the values in arr:

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([20, 21, 22, 23, 24, 25])

newarr = np.subtract(arr1, arr2)

print(newarr)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[-10  -1   8  17  26  35]


The example above will return [-10 -1 8 17 26 35] which is the result of 10-20, 20-21, 30-22 etc.


##Multiplication

import numpy as np

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([20, 21, 22, 23, 24, 25])

newarr = np.multiply(arr1, arr2)

print(newarr)
>>>>>>>>>>>>>>>>>>>>.....
[ 200  420  660  920 1200 1500]


##Division

Divide the values in arr1 with the values in arr2:

import numpy as np

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 5, 10, 8, 2, 33])

newarr = np.divide(arr1, arr2)

print(newarr)
>>>>>>>>>>>>>>>>...........
[ 3.33333333  4.          3.          5.         25.          1.81818182]

The example above will return [3.33333333 4. 3. 5. 25. 1.81818182] which is the result of 10/3, 20/5, 30/10 etc.




#######Power
The power() function rises the values from the first array to the power of the values of the second array, and return the results in a new array.

Example
Raise the valules in arr1 to the power of values in arr2:

import numpy as np

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 5, 6, 8, 2, 33])

newarr = np.power(arr1, arr2)

print(newarr)
>>>>>>>>>>>>>>>>>>>>>...
[         1000       3200000     729000000 6553600000000          2500
             0]

The example above will return [1000 3200000 729000000 6553600000000 2500 0] which is the result of 10*10*10, 20*20*20*20*20, 30*30*30*30*30*30 etc.



Remainder
Both the mod() and the remainder() functions return the remainder of the values in the first array corresponding to the values in the second array, and return the results in a new array.

Example
Return the remainders:

import numpy as np

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 7, 9, 8, 2, 33])

newarr = np.mod(arr1, arr2)

print(newarr)
>>>>>>>>>>>>>>>>>>.....
[ 1  6  3  0  0 27]

The example above will return [1 6 3 0 0 27] which is the remainders when you divide 10 with 3 (10%3), 20 with 7 (20%7) 30 with 9 (30%9) etc.





You get the same result when using the remainder() function:

Return the remainders:

import numpy as np

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 7, 9, 8, 2, 33])

newarr = np.remainder(arr1, arr2)

print(newarr)
>>>>>>>>>>>>>>>>>>>>>..
[ 1  6  3  0  0 27]



###Quotient and Mod
The divmod() function return both the quotient and the the mod. The return value is two arrays, the first array contains the quotient and second array contains the mod.

Example
Return the quotient and mod:

import numpy as np

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 7, 9, 8, 2, 33])

newarr = np.divmod(arr1, arr2)

print(newarr)
>>>>>>>>>>>>>>>>>>>>>>...
(array([ 3,  2,  3,  5, 25,  1]), array([ 1,  6,  3,  0,  0, 27]))

The example above will return:
(array([3, 2, 3, 5, 25, 1]), array([1, 6, 3, 0, 0, 27]))
The first array represents the quotients, (the integer value when you divide 10 with 3, 20 with 7, 30 with 9 etc.
The second array represents the remainders of the same divisions.


Return the quotient and mod:

import numpy as np

arr = np.array([-1, -2, 1, 2, 3, -4])

newarr = np.absolute(arr)

print(newarr)
>>>>>>>>>>>>>>>>>>>>>>>..
[1 2 1 2 3 4]

The example above will return [1 2 1 2 3 4].



####Rounding Decimals
There are primarily five ways of rounding off decimals in NumPy:

truncation
fix
rounding
floor
ceil
Truncation

Remove the decimals, and return the float number closest to zero. Use the trunc() and fix() functions.

Example
Truncate elements of following array:

import numpy as np

arr = np.trunc([-3.1666, 3.6667])

print(arr)
>>>>>>>>>>>>>>>>>>>...
[-3.  3.]



Rounding
The around() function increments preceding digit or decimal by 1 if >=5 else do nothing.

E.g. round off to 1 decimal point, 3.16666 is 3.2


import numpy as np

arr = np.around([-3.1666, 3.6667])

print(arr)
>>>>>>>>>>>>>>>>>>>>>
[-3.  4.]




###NumPy Logs
NumPy provides functions to perform log at the base 2, e and 10.

###Log at Base 2
Use the log2() function to perform log at the base 2.

Find log at base 2 of all elements of following array:

import numpy as np

arr = np.arange(1, 10)

print(np.log2(arr))
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>..
[0.         1.         1.5849625  2.         2.32192809 2.5849625
 2.80735492 3.         3.169925  ]

Note: The arange(1, 10) function returns an array with integers starting from 1 (included) to 10 (not included).



####Log at Base 10
Use the log10() function to perform log at the base 10.

Example
Find log at base 10 of all elements of following array:

import numpy as np

arr = np.arange(1, 10)

print(np.log10(arr))
>>>>>>>>>>>>>>>>>>>>>>>>>>>>...
[0.         0.30103    0.47712125 0.60205999 0.69897    0.77815125
 0.84509804 0.90308999 0.95424251]



###Natural Log, or Log at Base e
Use the log() function to perform log at the base e.

Example
Find log at base e of all elements of following array:

import numpy as np

arr = np.arange(1, 10)

print(np.log(arr))
>>>>>>>>>>>>>>>>>>>........
[0.         0.69314718 1.09861229 1.38629436 1.60943791 1.79175947
 1.94591015 2.07944154 2.19722458]



########Log at Any Base
NumPy does not provide any function to take log at any base, so we can use the frompyfunc() function along with inbuilt function math.log() with two input parameters and one output parameter:

Example
from math import log
import numpy as np

nplog = np.frompyfunc(log, 2, 1)

print(nplog(100, 15))
>>>>>>>>>>>>>>>>>>>.......
1.7005483074552052




####Summations
What is the difference between summation and addition?

Addition is done between two arguments whereas summation happens over n elements.


@Add the values in arr1 to the values in arr2: #this is an addition not summation.

import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])

newarr = np.add(arr1, arr2)

print(newarr)
>>>>>>>>>>>>>>>>>>>>>>>...
[2 4 6]

Returns: [2 4 6]




###Sum the values in arr1 and the values in arr2: #This is a summation not a normal addition.

import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])

newarr = np.sum([arr1, arr2])

print(newarr)
>>>>>>>>>>>>>>>>>>>>>>>>
12




Summation Over an Axis
If you specify axis=1, NumPy will sum the numbers in each array.

Example
Perform summation in the following array over 1st axis:

import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])

newarr = np.sum([arr1, arr2], axis=1)

print(newarr)
>>>>>>>>>>>>>>>>>>>>..
[6 6]



####Products
To find the product of the elements in an array, use the prod() function.

Example
Find the product of the elements of this array:

import numpy as np

arr = np.array([1, 2, 3, 4])

x = np.prod(arr)

print(x)
>>>>>>>>>>>>>>>>>>>>>>>...
24
Returns: 24 because 1*2*3*4 = 24



##import numpy as np

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])

x = np.prod([arr1, arr2])

print(x)
>>>>>>>>>>>>>>>>>>.
40320

Returns: 40320 because 1*2*3*4*5*6*7*8 = 40320


###Product Over an Axis
If you specify axis=1, NumPy will return the product of each array.

Example
Perform summation in the following array over 1st axis:

import numpy as np

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])

newarr = np.prod([arr1, arr2], axis=1)

print(newarr)
>>>>>>>>>>>>>>>>>>>>>>>...
[  24 1680]



###Differences
A discrete difference means subtracting two successive elements.

E.g. for [1, 2, 3, 4], the discrete difference would be [2-1, 3-2, 4-3] = [1, 1, 1]

To find the discrete difference, use the diff() function.

Example
Compute discrete difference of the following array:

import numpy as np

arr = np.array([10, 15, 25, 5])

newarr = np.diff(arr)

print(newarr)
>>>>>>>>>>>>>>>>>>>>>>>>>>......
[  5  10 -20]

because 15-10=5, 25-15=10, and 5-25=-20


###We can perform this operation repeatedly by giving parameter n.

E.g. for [1, 2, 3, 4], the discrete difference with n = 2 would be [2-1, 3-2, 4-3] = [1, 1, 1] , then, since n=2, we will do it once more, with the new result: [1-1, 1-1] = [0, 0]
Example
Compute discrete difference of the following array twice:

import numpy as np

arr = np.array([10, 15, 25, 5])

newarr = np.diff(arr, n=2)

print(newarr)
>>>>>>>>>>>>>>>>>>>.....
[5 -30]

[5 -30] because: 15-10=5, 25-15=10, and 5-25=-20 AND 10-5=5 and -20-10=-30


###Finding LCM (Lowest Common Multiple)
The Lowest Common Multiple is the least number that is common multiple of both of the numbers.

Find the LCM of the following two numbers:

import numpy as np

num1 = 4
num2 = 6

x = np.lcm(num1, num2)

print(x)
>>>>>>>>>>>>>>>>>>>>...
12

because that is the lowest common multiple of both numbers (4*3=12 and 6*2=12).


###Finding LCM in Arrays
To find the Lowest Common Multiple of all values in an array, you can use the reduce() method.

The reduce() method will use the ufunc, in this case the lcm() function, on each element, and reduce the array by one dimension.

Example
Find the LCM of the values of the following array:

import numpy as np

arr = np.array([3, 6, 9])

x = np.lcm.reduce(arr)

print(x)
>>>>>>>>>>>>>>>>>>>>>>....
18
Returns: 18 because that is the lowest common multiple of all three numbers (3*6=18, 6*3=18 and 9*2=18).




##Find the LCM of all of an array where the array contains all integers from 1 to 10:

import numpy as np

arr = np.arange(1, 11)

x = np.lcm.reduce(arr)

print(x)
>>>>>>>>>>>>>>>>...
2520





####Trigonometric Functions
NumPy provides the ufuncs sin(), cos() and tan() that take values in radians and produce the corresponding sin, cos and tan values.

Example
Find sine value of PI/2:

import numpy as np

x = np.sin(np.pi/2)

print(x)
>>>>>>>>>>>>>>>>>>..
1.0



##Find sine values for all of the values in arr:

import numpy as np

arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])

x = np.sin(arr)

print(x)
>>>>>>>>>>>>>>>>>>>.....
[1.         0.8660254  0.70710678 0.58778525]



#######Convert Degrees Into Radians

Note: radians values are pi/180 * degree_values.


import numpy as np

arr = np.array([90, 180, 270, 360])

x = np.deg2rad(arr)

print(x)
>>>>>>>>>>>>>>>>>>>.....
[1.57079633 3.14159265 4.71238898 6.28318531]



###Radians to Degrees
Example
Convert all of the values in following array arr to degrees:

import numpy as np

arr = np.array([np.pi/2, np.pi, 1.5*np.pi, 2*np.pi])

x = np.rad2deg(arr)

print(x)
>>>>>>>>>>>>>>>>>>>..
[ 90. 180. 270. 360.]



Finding Angles
Finding angles from values of sine, cos, tan. E.g. sin, cos and tan inverse (arcsin, arccos, arctan).

NumPy provides ufuncs arcsin(), arccos() and arctan() that produce radian values for corresponding sin, cos and tan values given.

Example
Find the angle of 1.0:

import numpy as np

x = np.arcsin(1.0)

print(x)
>>>>>>>>>>>>>>>>>.....
1.5707963267948966



Angles of Each Value in Arrays
Example
Find the angle for all of the sine values in the array

import numpy as np

arr = np.array([1, -1, 0.1])

x = np.arcsin(arr)

print(x)
>>>>>>>>>>>>>>>>>>>>>>...
[ 1.57079633 -1.57079633 0.10016742]



#####Hypotenues
Finding hypotenues using pythagoras theorem in NumPy.

NumPy provides the hypot() function that takes the base and perpendicular values and produces hypotenues based on pythagoras theorem.

Example
Find the hypotenues for 4 base and 3 perpendicular:

import numpy as np

base = 3
perp = 4

x = np.hypot(base, perp)

print(x)
>>>>>>>>>>>>>>>>>>>>>>>>>...
5.0




#####What is a Set
A set in mathematics is a collection of unique elements.

Sets are used for operations involving frequent intersection, union and difference operations.

Create Sets in NumPy
We can use NumPy's unique() method to find unique elements from any array. E.g. create a set array, but remember that the set arrays should only be 1-D arrays.

Example
Convert following array with repeated elements to a set:

import numpy as np

arr = np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])

x = np.unique(arr)

print(x)
>>>>>>>>>>>>>............
[1 2 3 4 5 6 7]



###Finding Union
To find the unique values of two arrays, use the union1d() method.

Example
Find union of the following two set arrays:

import numpy as np

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])

newarr = np.union1d(arr1, arr2)

print(newarr)
>>>>>>>>>>>>>>>>>>>>>>>>..
[1 2 3 4 5 6]






-----------------------------------------------------------------------------------------------------------------

Matplotlib Matplotlib Matplotlib Matplotlib Matplotlib Matplotlib Matplotlib Matplotlib  

-----------------------------------------------------------------------------------------------------------------


##checking version of matplotlib:

import matplotlib
print(matplotlib.__version__)


##Pyplot
Most of the Matplotlib utilities lies under the pyplot submodule, and are usually imported under the plt alias:

import matplotlib.pyplot as plt


import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.show()




###Plotting x and y points
The plot() function is used to draw points (markers) in a diagram.

By default, the plot() function draws a line from point to point.

The function takes parameters for specifying points in the diagram.

Parameter 1 is an array containing the points on the x-axis.

Parameter 2 is an array containing the points on the y-axis.

If we need to plot a line from (1, 3) to (8, 10), we have to pass two arrays [1, 8] and [3, 10] to the plot function.


Draw a line in a diagram from position (1, 3) to position (8, 10):

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints)
plt.show()




###Plotting Without Line
To plot only the markers, you can use shortcut string notation parameter 'o', which means 'rings'.

Example
Draw two points in the diagram, one at position (1, 3) and one in position (8, 10):

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints, 'o')
plt.show()



###Multiple Points
You can plot as many points as you like, just make sure you have the same number of points in both axis.

Example
Draw a line in a diagram from position (1, 3) to (2, 8) then to (6, 1) and finally to position (8, 10):

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])

plt.plot(xpoints, ypoints)
plt.show()



##Default X-Points
If we do not specify the points in the x-axis, they will get the default values 0, 1, 2, 3, (etc. depending on the length of the y-points.

So, if we take the same example as above, and leave out the x-points, the diagram will look like this:

Example
Plotting without x-points:

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10, 5, 7])

plt.plot(ypoints)
plt.show()


###Markers
You can use the keyword argument marker to emphasize each point with a specified marker:

Example
Mark each point with a circle:

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o')
plt.show()
>>>>>>>>>>>>>>.
It will show line and point dots in the line.



####Format Strings fmt
You can use also use the shortcut string notation parameter to specify the marker.

This parameter is also called fmt, and is written with this syntax:

marker | line | color
Example
Mark each point with a circle:

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, 'o:r')                #This o:r = marker | line | color
plt.show()


###Marker Size
You can use the keyword argument markersize or the shorter version, ms to set the size of the markers:

Example
Set the size of the markers to 20:

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o', ms = 20)
plt.show()


###You can use the keyword argument markerfacecolor or the shorter mfc to set the color inside the edge of the markers:

Example
Set the FACE color to red:

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o', ms = 20, mfc = 'r')
plt.show()



####Use both the mec and mfc arguments to color of the entire marker:

Example
Set the color of both the edge and the face to red:

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r', mfc = 'r')
plt.show()



###You can also use Hexadecimal color values:

Example
Mark each point with a beautiful green color:

...
plt.plot(ypoints, marker = 'o', ms = 20, mec = '#4CAF50', mfc = '#4CAF50')




##Or any of the 140 supported color names.

Example
Mark each point with the color named "hotpink":

...
plt.plot(ypoints, marker = 'o', ms = 20, mec = 'hotpink', mfc = 'hotpink')
plt.show()





####Multiple Lines
You can plot as many lines as you like by simply adding more plt.plot() functions:

Example
Draw two lines by specifying a plt.plot() function for each line:

import matplotlib.pyplot as plt
import numpy as np

y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])

plt.plot(y1)
plt.plot(y2)

plt.show()




###Draw two lines by specifiyng the x- and y-point values for both lines:

import matplotlib.pyplot as plt
import numpy as np

x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])

plt.plot(x1, y1, x2, y2)
plt.show()






######Create Labels and Title for a Plot
With Pyplot, you can use the xlabel() and ylabel() functions to set a label for the x- and y-axis.
With Pyplot, you can use the title() function to set a title for the plot.

Example
Add labels to the x- and y-axis:

import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x, y, 'o--g')

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.show()




####Add Grid Lines to a Plot
With Pyplot, you can use the grid() function to add grid lines to the plot.
Add grid lines to the plot:
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x, y, 'o--g')

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.grid() #Grid Here
plt.show()



###Setting Line Properties for the Grid:

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.plot(x, y, 'o--g')

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.grid(color = 'green', linestyle = '--', linewidth = 0.5) #Grid Here
plt.show()



Display Multiple Plots With the subplot() function

1
#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
​
plt.subplot(1, 2, 1)
plt.plot(x,y, 'o-')
​
#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])
​
plt.subplot(1, 2, 2)
plt.plot(x,y, 'o-')
​
plt.show()


###The subplot() function takes three arguments that describes the layout of the figure.
###plt.subplot(1, 2, 1) #the figure has 1 row, 2 columns, and this plot is the first plot.
####plt.subplot(1, 2, 2) #the figure has 1 row, 2 columns, and this plot is the second plot.




###Title and Super Title
You can add a title to each plot with the title() and suptitle() function:

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])


plt.subplot(1, 2, 1)
plt.plot(x,y, 'o-')
plt.title("SALES")

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])


plt.subplot(1, 2, 2)
plt.plot(x,y, 'o-')
plt.title("INCOME")

plt.suptitle("Amazon")
plt.show()






##########Creating Scatter Plots
With Pyplot, you can use the scatter() function to draw a scatter plot.

The scatter() function plots one dot for each observation. It needs two arrays of the same length, one for the values of the x-axis, and one for values on the y-axis:

A simple scatter plot:

import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

plt.scatter(x, y)
plt.show()



####The observation in the example above is the result of 13 cars passing by.

The X-axis shows how old the car is.

The Y-axis shows the speed of the car when it passes.

Are there any relationships between the observations?

It seems that the newer the car, the faster it drives, but that could be a coincidence, after all we only registered 13 cars.

Compare Plots
In the example above, there seems to be a relationship between speed and age, but what if we plot the observations from another day as well? Will the scatter plot tell us something else?

Example
Draw two plots on the same figure:

import matplotlib.pyplot as plt
import numpy as np

#day one, the age and speed of 13 cars:
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y)

#day two, the age and speed of 15 cars:
x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x, y)

plt.show()



Size: You can change the size of the dots with the s argument. 
Alpha: You can adjust the transparency of the dots with the alpha argument. 
ColorMap: You can specify the colormap with the keyword argument cmap with the value of the colormap You can include the colormap in the drawing by including the plt.colorbar() statement.

import matplotlib.pyplot as plt
import numpy as np
​
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])
​
plt.scatter(x, y, c = "hotpink", s=sizes, alpha=0.5, cmap= "nipy_spectral")
​
plt.colorbar()
plt.show()



Bars
Creating Bars With Pyplot, you can use the bar() function to draw bar graphs:

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
​
plt.bar(x,y)
plt.show()



Horizontal Bars If you want the bars to be displayed horizontally instead of vertically, use the barh() function:

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
​
plt.barh(x, y)
plt.show()
​


Best Colors:
r, g, b
        less noticable: Olive, DarkGoldenRod, Chocolate, sandybrown, indianred, FireBrick,

        Middle Color:   DodgerBlue, RoyalBlue, teal, 

        Bright uplifting: DarkOrange, orange, OrangeRed, Deeppink, springgreen, Fuchsia, gold, Lime, Magenta, Crimson, MediumSpringGreen, LimeGreen,


        Male & Femal:      Firebrick, Deeppink,      "Crimson", "Fuchsia"

        Rich, Middleclass, Poor : "Chocolate", "DodgerBlue", "springgreen"


###Bar Width: 
The bar() takes the keyword argument width to set the width of the bars.

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
​
plt.bar(x, y, color = "SpringGreen", width = 0.1)
plt.show()

Note: The default width value is 0.8



####Histogram
A histogram is a graph showing frequency distributions.
import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(170, 10, 250)

plt.hist(x)
plt.show()




###Creating Pie Charts:
With Pyplot, you can use the pie() function to draw pie charts:
x = np.array([35, 25, 25, 15])

plt.pie(x)
plt.show()

Note: By default the plotting of the first wedge starts from the x-axis and move counterclockwise.


###Labels
Add labels to the pie chart with the label parameter.

The label parameter must be an array with one label for each wedge:


y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.show() 




###Explode
Maybe you want one of the wedges to stand out? The explode parameter allows you to do that.

The explode parameter, if specified, and not None, must be an array with one value for each wedge.

Each value represents how far from the center each wedge is displayed:

Example
Pull the "Apples" wedge 0.2 from the center of the pie:

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0]

plt.pie(y, labels = mylabels, explode = myexplode)
plt.show() 




###Shadow
Add a shadow to the pie chart by setting the shadows parameter to True:


import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0]

plt.pie(y, labels = mylabels, explode = myexplode, shadow = True)
plt.show() 




###Colors
You can set the color of each wedge with the colors parameter.

The colors parameter, if specified, must be an array with one value for each wedge:

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
mycolors = ["black", "hotpink", "b", "#4CAF50"]
myexplode = [0.2, 0, 0, 0]

plt.pie(y, labels = mylabels, colors = mycolors, explode = myexplode)
plt.show() 





###Legend
To add a list of explanation for each wedge, use the legend() function:


y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
mycolors = ["SpringGreen", "RoyalBlue", "LimeGreen", "Dodgerblue"]
myexplode = [0.2, 0, 0, 0]


plt.pie(y, labels = mylabels, colors = mycolors, explode = myexplode)
plt.legend(title = "Four Fruits:")
plt.show()




-----------------------------------------------------------------------------------------------------------------

Pandas Pandas Pandas Pandas Pandas Pandas Pandas Pandas Pandas Pandas Pandas Pandas 

------------------------------------------------------------------------------------------------------------


###Series:
A Pandas Series is like a column in a table.

It is a one-dimensional array holding data of any type.




import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a)

print(myvar)



###Create Labels
With the index argument, you can name your own labels.

a = [1, 7, 2]

myvar = pd.Series(a, index = ["x", "y", "z"])

print(myvar)


####Key/Value Objects as Series
You can also use a key/value object, like a dictionary, when creating a Series.

Example
Create a simple Pandas Series from a dictionary:

import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories)

print(myvar)





###DataFrames
Data sets in Pandas are usually multi-dimensional tables, called DataFrames.

Series is like a column, a DataFrame is the whole table.

#
#Create a DataFrame from two Series:
​
import pandas as pd
​
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
​
myvar = pd.DataFrame(data)
​
print(myvar)

#A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.



###Locate Row
As you can see from the result above, the DataFrame is like a table with rows and columns.

Pandas use the loc attribute to return one or more specified row(s)


Return row 0:

#refer to the row index:
print(df.loc[0])

###Return row 0 and 1:

#use a list of indexes:
print(df.loc[[0, 1]])






###Read CSV Files

Load a comma separated file (CSV file) into a DataFrame:

import pandas as pd
data = pd.read_csv("/home/arsh/code/csv_file/data.csv")
print(data)

@@@Note: CSV file me Title har column ke liye hona chahiye. nahi to csv file open hi nahi hoga aur na hi load hoga.




####Load and print the entire DataFrame:

data = pd.read_csv("/home/arsh/code/csv_file/data.csv")
print(data.to_string()) 
#use to_string() to print the entire DataFrame.



####Read JSON
Big data sets are often stored, or extracted as JSON.

JSON is plain text, but has the format of an object, and is well known in the world of programming, including Pandas.

In our examples we will be using a JSON file called 'data.json'.

df = pd.read_json('/home/arsh/code/data.js')
​
print(df.to_string()) 




####Dictionary as JSON
JSON = Python Dictionary

JSON objects have the same format as Python dictionaries.

If your JSON code is not in a file, but in a Python Dictionary, you can load it into a DataFrame directly:



Dictionary as JSON

JSON = Python Dictionary
JSON objects have the same format as Python dictionaries.

If your JSON code is not in a file, but in a Python Dictionary, you can load it into a DataFrame directly:

data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}
​
df = pd.DataFrame(data)
​
print(df) 





####Data Cleaning
Bad data could be:

Empty cells

Data in wrong format

Wrong data

Duplicates




###Empty Cells:

Empty cells can potentially give you a wrong result when you analyze data.

Remove Rows:

One way to deal with empty cells is to remove rows that contain empty cells.

This is usually OK, since data sets can be very big, and removing a few rows will not have a big impact on the result.


df = pd.read_csv('/home/arsh/code/csv_file/data.csv')

new_df = df.dropna()

print(new_df.to_string())



Note: By default, the dropna() method returns a new DataFrame, and will not change the original.

If you want to change the original DataFrame, use the inplace = True argument:

#Remove all rows with NULL values:
​
import pandas as pd
​
df = pd.read_csv('/home/arsh/code/csv_file/dirtydata.csv')
​
df.dropna(inplace = True)
​
print(df.to_string())




####Replace Empty Values
Another way of dealing with empty cells is to insert a new value instead.

This way you do not have to delete entire rows just because of some empty cells.

The fillna() method allows us to replace empty cells with a value:

#Replace NULL values with the number 130:
​
import pandas as pd
​
df = pd.read_csv('/home/arsh/code/csv_file/dirtydata.csv')
​
df.fillna(130, inplace = True)
​
print(df.to_string())





####Replace Only For Specified Columns
To only replace empty values for one column, specify the column name for the DataFrame:

#Replace NULL values in the "Calories" columns with the number 130:
​
import pandas as pd
​
df = pd.read_csv('/home/arsh/code/csv_file/dirtydata.csv')
​
df["Calories"].fillna(130, inplace = True)
​
print(df.to_string())
​
#This operation inserts 130 in empty cells in the "Calories" column (row 18 and 28).




####Replace Using Mean, Median, or Mode
Pandas uses the mean() median() and mode() methods to calculate the respective values for a specified column:

#Calculate the MEAN, and replace any empty values with it:
​
df = pd.read_csv('/home/arsh/code/csv_file/dirtydata.csv')
​
x = df["Calories"].mean()
​
df["Calories"].fillna(x, inplace = True)
​
print(df.to_string())
​
#As you can see in row 18 and 28, the empty values from "Calories" was replaced with the mean: 304.68





####Mean = the average value (the sum of all values divided by number of values).

#Calculate the MEDIAN, and replace any empty values with it:
​
import pandas as pd
​
df = pd.read_csv('/home/arsh/code/csv_file/dirtydata.csv')
​
x = df["Calories"].median()
​
df["Calories"].fillna(x, inplace = True)
​
print(df.to_string())
​
#As you can see in row 18 and 28, the empty values from "Calories" was replaced with the median: 291.2






Median = the value in the middle, after you have sorted all values ascending.

Calculate the MODE, and replace any empty values with it:

df = pd.read_csv('/home/arsh/code/csv_file/dirtydata.csv')
​
x = df["Calories"].mode()[0]
​
df["Calories"].fillna(x, inplace = True)
​
print(df.to_string())
​
#As you can see in row 18 and 28, the empty value from "Calories" was replaced with the mode: 300.0






#####Mode = the value that appears most frequently.




####Data of Wrong Format
To fix it, you have two options:

remove the rows, 

or convert all cells in the columns into the same format.
Pandas has a to_datetime() method for this:

'/home/arsh/code/csv_file/dirtydata.csv'
df = pd.read_csv('/home/arsh/code/csv_file/dirtydata.csv')
​
df['Date'] = pd.to_datetime(df['Date'])
​
print(df.to_string())



#####we can remove the row by using the dropna() method.

df = pd.read_csv(
df = pd.read_csv('/home/arsh/code/csv_file/dirtydata.csv')
​
df['Date'] = pd.to_datetime(df['Date'])
​
df.dropna(subset=['Date'], inplace = True)
​
print(df.to_string())



###Wrong Data
"Wrong data" does not have to be "empty cells" or "wrong format", it can just be wrong, like if someone registered "199" instead of "1.99".

Sometimes you can spot wrong data by looking at the data set, because you have an expectation of what it should be.

If you take a look at our data set, you can see that in row 7, the duration is 450, but for all the other rows the duration is between 30 and 60.

It doesn't have to be wrong, but taking in consideration that this is the data set of someone's workout sessions, we conclude with the fact that this person did not work out in 450 minutes.

##Replacing Values:

One way to fix wrong values is to replace them with something else.

In our example, it is most likely a typo, and the value should be "45" instead of "450", and we could just insert "45" in row 7:

df = pd.read_csv('/home/arsh/code/csv_file/dirtydata.csv')

df.loc[7,'Duration'] = 45

print(df.to_string())



For small data sets you might be able to replace the wrong data one by one, but not for big data sets.

To replace wrong data for larger data sets you can create some rules, e.g. set some boundaries for legal values, and replace any values that are outside of the boundaries.

Loop through all values in the "Duration" column.

If the value is higher than 60, set it to 60:

df = pd.read_csv('/home/arsh/code/csv_file/dirtydata.csv')
​
for x in df.index:
  if df.loc[x, "Duration"] > 60:
    df.loc[x, "Duration"] = 60
​
print(df.to_string())



Removing Rows:

Another way of handling wrong data is to remove the rows that contains wrong data.

This way you do not have to find out what to replace them with, and there is a good chance you do not need them to do your analyses.

df = pd.read_csv('/home/arsh/code/csv_file/dirtydata.csv')
​
for x in df.index:
  if df.loc[x, "Duration"] > 60:
    df.drop(x, inplace = True)
​
#remember to include the 'inplace = True' argument to make the changes in the original DataFrame object instead of returning a copy
​
print(df.to_string())




###Discovering Duplicates
Duplicate rows are rows that have been registered more than one time.

To discover duplicates, we can use the duplicated() method.

The duplicated() method returns a Boolean values for each row:

###Returns True for every row that is a duplicate, othwerwise False:
​
df = pd.read_csv('/home/arsh/code/csv_file/dirtydata.csv')
​
print(df.duplicated())




##To remove duplicates, use the drop_duplicates() method.

#Remove all duplicates:
​
df = pd.read_csv('/home/arsh/code/csv_file/dirtydata.csv')
​
df.drop_duplicates(inplace = True)
​
print(df.to_string())
​
#Notice that row 12 has been removed from the result





####Remember: The (inplace = True) will make sure that the method does NOT return a new DataFrame, but it will remove all duplicates from the original DataFrame.

Pandas - Plotting
Pandas uses the plot() method to create diagrams.

We can use Pyplot, a submodule of the Matplotlib library to visualize the diagram on the screen.

import matplotlib.pyplot as plt
​
df = pd.read_csv('/home/arsh/code/csv_file/data.csv')
​
df.plot()
​
plt.show()




####Specify that you want a scatter plot with the kind argument:

kind = 'scatter'

A scatter plot needs an x- and a y-axis.

df = pd.read_csv('/home/arsh/code/csv_file/data.csv')
​
df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')
​
plt.show()





#####Remember: In the previous example, we learned that the correlation between "Duration" and "Calories" was 0.922721, and we conluded with the fact that higher duration means more calories burned.

By looking at the scatterplot, I will agree.

Let's create another scatterplot, where there is a bad relationship between the columns, like "Duration" and "Maxpulse", with the correlation 0.009403:

###A scatterplot where there are no relationship between the columns:
​
df = pd.read_csv('/home/arsh/code/csv_file/data.csv')
​
df.plot(kind = 'scatter', x = 'Duration', y = 'Maxpulse')
​
plt.show()




######Histogram
Use the kind argument to specify that you want a histogram:

kind = 'hist'

A histogram needs only one column.

A histogram shows us the frequency of each interval, e.g. how many workouts lasted between 50 and 60 minutes?

In the example below we will use the "Duration" column to create the histogram:

import pandas as pd
import matplotlib.pyplot as plt
​
df = pd.read_csv('/home/arsh/code/csv_file/data.csv')
​
df["Duration"].plot(kind = 'hist')
​
plt.show()

Note: The histogram tells us that there were over 100 workouts that lasted between 50 and 60 minutes
















-----------------------------------------------------------------------------------------------------------------

SciPy SciPy SciPy SciPy SciPy SciPy SciPy SciPy SciPy SciPy SciPy SciPy SciPy SciPy 

-----------------------------------------------------------------------------------------------------------------




    What is SciPy?

SciPy is a scientific computation library that uses NumPy underneath.

SciPy stands for Scientific Python.


    Import SciPy

Once SciPy is installed, import the SciPy module(s) you want to use in your applications by adding the from scipy import module statement:

>>>from scipy import constants



    Constants in SciPy:

As SciPy is more focused on scientific implementations, it provides many built-in scientific constants.

These constants can be helpful when you are working with Data Science.

PI is an example of a scientific constant.

Example
Print the constant value of PI:


    from scipy import constants

    print(constants.pi)



List all constants:

    from scipy import constants

    print(dir(constants))























-----------------------------------------------------------------------------------------------------------------

PROJECTS PROJECTS PROJECTS PROJECTS PROJECTS PROJECTS PROJECTS PROJECTS  

-----------------------------------------------------------------------------------------------------------------




##YouTube Survey

print("""\n Hey! Aluxurs! what would you like to watch in the next stream?\nPlease, take some time to fill this out and help me decide what to play
next!\n""")

a = "Days gone"
b = "Resident Evil 2"
c = "Fortnite"
d = "Apex Legends"
e = "Death Stranding"
f = "Surprise Us!"

selected = input(f"""\nKindly Remember! Please select only one! 
\n\n\t a){a}
\n\t b){b}
\n\t c){c}
\n\t d){d}
\n\t e){e}
\n\t f){f}
\n\n> Type Your selection here: """)

print(f"""\n You have chosen "{selected.title()}". I appreciate your time and hope to see you in
the next one!""")





#Dentist shop Service:


print("\nWelcome to the patient portal!")

a = "Root Canal Therapy" 
b = "Oral Hygiene Check" 
c = "Emergency Injury Treatment" 
d = "Post-Procedure Check-up"
e = "Routine Check-ups and Consultation" 

print("\nPlease select the service you would like to come in for:")
selected = input(f""" 
\n\t a){a}
\n\t b){b}
\n\t c){c}
\n\t d){d}
\n\t e){e}
\n\n> Choose your Service here by typing    a   b   c   d   or  e           :   """)

if selected.lower() == "a":
    total = 250
    print(f"\n\tYou have Choose \"{selected}\"\n\tYour Fee is: ${total}")
elif selected.lower() == "b":
    total = 50
    print(f"\n\tYou have Choose \"{selected}\"\n\tYour Fee is: ${total}")
elif selected.lower() == "c":
    total = 100
    print(f"\n\tYou have Choose \"{selected}\"\n\tYour Fee is: ${total}")
elif selected.lower() == "d":
    total = 150
    print(f"\n\tYou have Choose \"{selected}\"\n\tYour Fee is: ${total}")
else:
    total = 75
    print(f"\n\tYou have Choose \"{selected}\"\n\tYour Fee is: ${total}")

new_total = total * 0.5

print(f"\n\tBut,\n\tIf you pay now. You will get 50% discount. And You have to pay just: ${new_total}")
print("\nSo,  Could you pay Now!")

discount = input("\ny/n\n>")

if discount.lower() == "y":
    print(f"\nCongratulation! Now, Your total payable amount is: ${new_total}") 
elif discount.lower() == "yes":
    print(f"\nCongratulation! Now, Your total payable amount is: ${new_total}")
else:
    print(f"\nYou will need to pay ${new_total} at the counter.")

print("\nThankYou! have a great Day!")





COLLEGE ADMISSION
###A program that will determine the eligibility of an applicant based on a few questions and
conditions.


print("\nWelcome to the Applicant’s eligibility checker!")

first_name = input("\nPlease enter your First Name: ")
last_name = input("\nPlease enter your Last Name: ")
age      = input("\nPlease enter your Age: ")
marks    = float(input("\nPlease enter your Overall marks(out of 600): "))
total_marks = 600
passing_marks = total_marks * 0.6
marks_for_scholarship = total_marks * 0.8

if marks >= passing_marks:
    print(f"\n\t>>>Congratulation \"{first_name.title()}\"! You are eligible for Admission!")

    scholarship = input("\nAre you seeking a scholarship? [Y/N]: ")
    
    if scholarship.lower() == "y" and marks >= marks_for_scholarship:
        print(f"\n\t>>>Congratulation \"{first_name.title()}\"! You are also eligible for Scholarship!!!")
    elif scholarship.lower() != "y":
        pass
    else:
        print(f"\n\t>>>Sorry \"{first_name.title()}\" Your marks is below \"{marks_for_scholarship}\" You are not eligible for scholarship at this moment")

else:
    print(f"\n\t>>>Sorry \"{first_name.title()}\", You are not eligible for Admission!")

print("\nThank you for your input and we wish you good luck!")




####HIGHEST NUMBER

"""A programmer came up with a program that would find the highest
number from a given set of numbers.The numbers provided were stored
as a list in a list variable called ‘number_data’ and the program that he
designed looked like this:"""

number_data = [323, 209, 5900, 31092, 3402, 39803, 78341, 79843740, 895,
6749, 2870984]

highest = 0
for number in number_data:
    if highest < number:
        highest = number
print(highest)




###LOAN ELIGIBILITY

"""A freelance programmer was tasked with creating a simple
program to determine the eligibility of a profile for an auto-loan. Based
on some specific information and conditions, such as the candidate
should be less than 45 years of age, must have a minimum of a certain
number as income and should not have any criminal records, the
program was to determine if the same person was eligible for a loan or
not. The programmer wrote the following program:"""

print("Your doorway to auto-loan eligibility check!")
print("Please provide complete information for best results")

name = input("Please enter your full name: ")
age = int(input("Enter your age: "))
income = int(input("Please enter your income per month: "))
nature_of_job = input("Do you work full-time, part-time or as a freelancer?: ")
has_license = input("Do you have a valid license? [y/n]: ")


if has_license.lower() == "y":
    has_license = True
else:
    has_license = False

has_criminal_record = input("In the last 5 years, do you have any criminal records? [y/n]: ")

if has_criminal_record.lower() != "y":
    has_criminal_record = False
else:
    has_criminal_record = True

if age > 45 and income >= 20000 and has_license == True and has_criminal_record == False:
    print("You are eligible for a loan")

elif age < 45 and income >= 15000 and has_license == True and has_criminal_record == False:
    print("You are eligible to apply for a loan")

elif has_criminal_record:
    print("You are not eligible for a loan")

elif income < 10000:
    print("You are not eligible at this time")

else:
    print("Please be patient as one of our specialists will be in touch!")


#########EVEN OR ODD

print("Setting the ODDS, EVEN!")
num = int(input("Enter a number: "))
if (num % 2) == 0:
    print(f"{num} is Even")
else:
    print(f"{num} is Odd")






############ROCK PAPER SCISSORS

from random import randint
t = ["Rock", "Paper", "Scissors"]
computer = t[randint(0, 2)]
tries = 0
player = " "
while tries <= 9:
    player = input("Rock, Paper, Scissors?")
    tries += 1
    if player == computer:
        print("Tie!")
    elif player.title() == "Rock":

        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player.title() == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player.title() == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("That's not a valid play. Check your spelling!")

    computer = t[randint(0, 2)]




#DIGIT TO TEXT or NUMBER TO TEXT


number = input("Phone number: ")

words = {
 "1" : "One",
 "2" : "Two",
 "3" : "Three",
 "4" : "Four",
 "5" : "Five",
 "6" : "Six",
 "7" : "Seven",
 "8" : "Eight",
 "9" : "Nine",
 "0" : "Zero",
 }

output = ""
for character in number:
    output = output + words.get(character) + " "
print(output)





#SHIPPING COST

total = int(input("Please enter the total amount: "))
country = input("Country [US/AU/CA/UK]: ")
if country.upper() == "US":
    if total >=50 and total < 100:
        print("Shipping Cost is $10")
    elif total >= 100 and total < 250:
        print("Shipping Cost is $25")
    elif total >= 250:
        print("Shipping Costs $50")
    else:
        print("FREE")

elif country.upper() == "AU":
    if total >=50 and total < 100:
        print("Shipping Cost is $20")
    elif total >= 100 and total < 250:
        print("Shipping Cost is $50")
    elif total >= 250:
        print("Shipping Costs $100")
    else:
        print("Shipping Cost is $10")
elif country.upper() == "CA":
    if total >=50 and total < 100:
        print("Shipping Cost is $15")
    elif total >= 100 and total < 250:
        print("Shipping Cost is $30")
    elif total >= 250:
        print("Shipping Costs $75")
    else:
        print("Shipping Cost is $5")
elif country.upper() == "UK":
    if total >=50 and total < 100:
        print("Shipping Cost is $25")
    elif total >= 100 and total < 250:
        print("Shipping Cost is $55")
    elif total >= 250:
        print("Shipping Costs $110")
    else:
        print("Shipping Cost is $20")


##########NAME GUESS!

name = 'James'
guess = input("I have a name. Can you try to guess it?: ")
guess_num = 0
max_guess = 5
while guess != name and guess_num != max_guess:
    print(f"I am afraid, that's not quite right! Hint: letter {guess_num +1} ")
    print(guess_num + 1, "is", name[guess_num] + ". ")
    guess = input("Have another go: ")
    guess_num = guess_num + 1

if guess_num == max_guess and name != guess:
    print("Alas! You failed. The name was", name + ".")
else:
    print("Great, you got it in", guess_num + 1, "guesses!")



>>>>>>>>>>>>>>>>>>>>>>>
I have a name. Can you try to guess it?: arsh
I am afraid, that's not quite right! Hint: letter 1 
1 is J. 
Have another go: bbnb
I am afraid, that's not quite right! Hint: letter 2 
2 is a. 
Have another go: dlskjf
I am afraid, that's not quite right! Hint: letter 3 
3 is m. 
Have another go: sdlfkjsd;l
I am afraid, that's not quite right! Hint: letter 4 
4 is e. 
Have another go: sdfjk
I am afraid, that's not quite right! Hint: letter 5 
5 is s. 
Have another go: sdjkj
Alas! You failed. The name was James.


>>>>>>>>>>
I have a name. Can you try to guess it?: james
I am afraid, that's not quite right! Hint: letter 1 
1 is J. 
Have another go: James
Great, you got it in 2 guesses!

>>>>>>>>>>>
I have a name. Can you try to guess it?: arsh
I am afraid, that's not quite right! Hint: letter 1 
1 is J. 
Have another go: Jarsh
I am afraid, that's not quite right! Hint: letter 2 
2 is a. 
Have another go: sfajkd
I am afraid, that's not quite right! Hint: letter 3 
3 is m. 
Have another go: Jam 
I am afraid, that's not quite right! Hint: letter 4 
4 is e. 
Have another go: Jame
I am afraid, that's not quite right! Hint: letter 5 
5 is s. 
Have another go: James
Great, you got it in 6 guesses!







#######DISTANCE FARE TAXI

"""You are to create a function that calculates a taxi fare. The taxi fare
is comprised of a base fare of $3.00 and then $0.10 for every 100 meters
traveled. Create a function that takes distance as its only parameter (in
km) and returns the value of the total applicable fare. Follow up with a
program to show the functioning nature of the function."""

def calculate_fare():
    distance = float(input("Enter the distance in kms: "))
    fare = 3 + distance   #Because there is $1 for every 1km  
    return fare

print(f"Your total Taxi fare is ${calculate_fare()}")


OR 

def calculate_fare():
    distance = float(input("Enter the distance in kms: "))
    distance = distance * 1000 #Convert kms into meters
    fare = 3.0 + ((distance / 100) * 0.1) # extra fare charged at every 100 meters
    
    return fare
print(f"Your total taxi fare is ${calculate_fare()}")


##NUMBER GUESSING GAME for 5 times

import random

num = random.randint(1, 20)             #You can also use randrange here!
tries = 0
while tries <= 5:
    guess = int(input("Please guess a number between 1 to 20: "))
    tries = tries + 1
    if guess < num:
        print("\n\tYou have guessed little bit lower.\n")

    elif guess > num:
        print("\n\tYour guess is slightly bigger than the expected number\n")

    else:
        print("\n\tCongratulation You have guessed 100% Accurate!\n")





####Number guessing game until you guessed 100% True guess or enter "x"


######

import random

num = random.randint(1, 20)             #You can also use randrange here!

while True:
    user_input = input("Please guess a number between 1 to 20: ")
    if user_input.lower() == "x":           #If user will enter "x" program close!
        exit()

    guess = int(user_input)
    if guess < num:
        print("\n\tYou have guessed little bit lower.\n")

    elif guess > num:
        print("\n\tYour guess is slightly bigger than the expected number\n")

    else:
        print("\n\tCongratulation You have guessed 100% Accurate!\n")
        break               #Break endicates that util gess is 100% true loop would not stop and when you will guessed 100% accurate number. The program would stop!



########NUMBER GUESSING WITH A CHEAT

import random

num = random.randint(1, 20)             #You can also use randrange here!

cheat = input("Do you want to know Hidden value [y/n]: ")
if cheat.lower() == "y":
    print(num)              #this is a cheat to know the hidden value!
else:
    pass
while True:
    user_input = input("Please guess a number between 1 to 20: ")
    if user_input.lower() == "x":           #If user will enter "x" program close!
        exit()


    guess = int(user_input)
    if guess < num:
        print("\n\tYou have guessed little bit lower.\n")

    elif guess > num:
        print("\n\tYour guess is slightly bigger than the expected number\n")

    else:
        print("\n\tCongratulation You have guessed 100% Accurate!\n")
        break               #Break endicates that util gess is 100% true loop would not stop and when you will guessed 100% accurate number. The program would stop!


###RANDOM SALAD SUGGESTION

import random

fruits = ["Apple", "Banana", "Peach", "Orange", "Durian", "Papaya"]

salad = random.sample(fruits, 3)        #Use sample to pick random element more than 1
print(salad)
#You could also use : print(random.sample(fruits, 3)) instead of "salad"




###COMPARING TWO NUMBERS 


print("Now! You have to inter two number one by one and I will tell some information about your number\n")

num_1 = int(input("Please input your First Number\n> "))
num_2 = int(input("Please input your Second Number\n> "))

if num_1 > num_2:
    print("\n\tYour First Number is Greater than you second!")

elif num_1 < num_2:
    print("\n\tYour Second Number is Greater than your first!")

else:
    print("\n\tYour Both Numbers are equal to one another!")







##FUNNY NAME GENERATOR

import random

print("\nWelocme, We are here to generate a funny name for you to see!")

first = ('Baby Oil', 'Bad News', 'Big Burps', "Bill 'Beenie­Weenie'",
"Bob 'Stinkbug'", 'Bowel Noises', 'Boxelder', "Bud 'Lite' ",
'Butterbean', 'Buttermilk', 'Buttocks', 'Chad', 'Chesterfield',
'Chewy', 'Chigger", "Cinnabuns', 'Cleet', 'Cornbread', 'Crab Meat',
'Crapps', 'Dark Skies', 'Dennis Clawhammer', 'Dicman', 'Elphonso',
'Fancypants', 'Figgs', 'Foncy', 'Gootsy', 'Greasy Jim', 'Huckleberry', 'Huggy', 'Ignatious', 'Jimbo', "Joe 'Pottin Soil'", 'Johnny',
'Lemongrass', 'Lil Debil', 'Longbranch', '"Lunch Money"',
'Mergatroid', '"Mr Peabody"', 'Oil­Can', 'Oinks', 'Old Scratch',
'Ovaltine', 'Pennywhistle', 'Pitchfork Ben', 'Potato Bug',
'Pushmeet','Rock Candy', 'Schlomo', 'Scratchensniff', 'Scut',
"Sid 'The Squirts'", 'Skidmark', 'Slaps', 'Snakes', 'Snoobs',
'Snorki', 'Soupcan Sam', 'Spitzitout', 'Squids', 'Stinky',
'Storyboard', 'Sweet Tea', 'TeeTee', 'Wheezy Joe',
"Winston 'Jazz Hands'", 'Worms')



last = ('Appleyard', 'Bigmeat', 'Bloominshine', 'Boogerbottom',
'Breedslovetrout', 'Butterbaugh', 'Clovenhoof', 'Clutterbuck',
'Cocktoasten', 'Endicott', 'Fewhairs', 'Gooberdapple', 'Goodensmith',
'Goodpasture', 'Guster', 'Henderson', 'Hooperbag', 'Hoosenater',
'Hootkins', 'Jefferson', 'Jenkins', 'Jingley­Schmidt', 'Johnson',
'Kingfish', 'Listenbee', "M'Bembo", 'McFadden', 'Moonshine', 'Nettles',
'Noseworthy', 'Olivetti', 'Outerbridge', 'Overpeck', 'Overturf',
'Oxhandler', 'Pealike', 'Pennywhistle', 'Peterson', 'Pieplow',
'Pinkerton', 'Porkins', 'Putney', 'Quakenbush', 'Rainwater',
'Rosenthal', 'Rubbins', 'Sackrider', 'Snuggleshine', 'Splern',
'Stevens', 'Stroganoff', 'Sugar­Gold', 'Swackhamer', 'Tippins',
'Turnipseed', 'Vinaigrette', 'Walkingstick', 'Wallbanger', 'Weewax',
'Weiners', 'Whipkey', 'Wigglesworth', 'Wimplesnatch', 'Winterkorn',
'Woolysocks')

while True:
    first_name = random.choice(first)

    last_name = random.choice(last)

    enter = input("\nPlease press \"Enter\" to generate a funny name! or press \"x\" to exit\n>>>")

    if enter.lower() != "x":            #This is to exit a loop or a program!
        print(f"\n\t{first_name} {last_name}\n")
    else:
        break



####Maximum of two numbers in Python

# Python program to find the
# maximum of two numbers
 
 
def maximum(a, b):
     
    if a > b:
        return a
    else:
        return b
     
# Driver code
a = 2
b = 4
print(maximum(a, b))

# Driver code
a = 8
b = 4
print(maximum(a, b))

# Driver code
a = 8
b = 19
print(maximum(a, b))
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.
4
8
19



# Python program to find the
# maximum of two numbers
 
 
a = 2
b = 4
 
maximum = max(a, b)
print(maximum)












Dynamic Array:

Size : How many elements. an array is currently storing.
Capacity: How many elements. an array could store. maximum limit or capacity of holding an element of that array.

Maximum capacity of an array is : 10 to the power 7.


    
