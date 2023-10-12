# Python
**Why Python?** 
	1. Easy to Read and Learn
	2. Various Existing Libraries and frameworks
	3. Large Community and documentation
	4. Automate our day to day task
	5. Can Create GUI based apps, websites and games.



Printing in Python using print() function.

print("HelloWorld")
print(100)
print(10*3)

print(f 'Sum of two numbers are:{10+20}')

**Comments in Python
**
Using #  --> Single Line Comment
""" Code """ --> Multi Line Comment


**Variables in Python**

length_of_rect=10
width_of_rect=20

**#the variables are stored inside the memory, they are allotted some space inside the memory.
#when we call the variable, it is retrieved from that memory location and its value is displayed**

user_name='Tanmay'

print(f' Area of Rectangle is:{length_of_rect*width_of_rect}')
print(f 'My name is{user_name}')


**Rules for declaring Variables:** 
	1. Should not start with a number
	2. No space
	3. No Special character
	4. Cannot use build in keywords


**Types of data in Variables**

Name = "Paul"    --> char/ string
Age = 30  --> Int
Price = 25.5  --> Floating point(double/decimal)
Bol = True/False  --> only 2 values (0--> False, 1-->True)


As in python we are not defining any specific type by using keywords but python itself understand the type of the variable value

Example: 

Num1 = 10   #Interger
Num2 = '10'  #String

When we try to add them and then print
Print(Num1+Num2)

Output-->Type Error: unsupported operand type(s) for +: 'int' and 'string'


Python is a Strongly type Language.
Type() method is used to check the type of the variable
Print(type(Num1)  //<class 'int>
Print(type(Num2) //<class 'string'>


Print(3**5)  #3^5
Print(10/3)  #3.3333333333333
But if we want only the integer result then 
Print(10//3) #3



**Strings in Python**

	1. Strings are immutable
	2. We can use 'Hello' or "Hello"
	3. Use + to add two string 'Hello' + 'World'

-ve indexing can be done in python. Then the value of index will start from behind.


**Lists**

How to define a List?
Users = ['raju','sham','paul']

How to get value from a List
Users[0]
Users[1]
Users[2]

Adding Item to a List?
Users.append('paul')

How to delete values from a List?
Users.remove('raju)

How to modify values from a List?
Users[1] = "shan"

Adding item to a list at a given position?
Users.insert(1,'shanu')

How to delete values from list using index number?
Del users[2]

Length of list
Len(users)

Sorting the items in List?
Users.sort()
Users.sort(reverse = True) or users.reverse()

Temporary sorting of items?
Print(users.sorted())

Popping the values from list
Users.pop()
Print(users)

Also the index value can be given for popping the value out

Remove method does not store the value , its completely deleted or removed, but with pop the value can be stored to some variable and can be displayed in the result

**Slicing of List**

Getting first two items
Users[:2]

Getting middle 3 items
Users.[1:4]

Getting last 2 items
Users.[-2:]

#NumericLists
sell=[2,9,13,28,35,4,56]

#Gettingminormax
print(min(sell))
print(max(sell))

#Gettingsumofitems
print(sum(sell))


**Tuples**

Same as list, however you can't modify the items of Tuple

	- Immutable
	- Ordered
	
Days = ('mon', 'tue', 'wed')

**Logical Operators**

Condition 1 and Condition 2
If both the conditions are true then true else false

Condition 1 or Condition 2
If both the conditions are false then false else true


**!!!!!!!!!!!!!!!!!!Further Explanation is provided along with the Code Only!!!!!!!!!!!!!!!!!!!!!!**
