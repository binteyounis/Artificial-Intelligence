print("Hello World!")
Hello World!

x=1
#The initial value of x is 1
if x>0:
  print("These are two comments") #Print a string
These are two comments

txt = input("Type something to test this out")
print (txt)
Hey

print("Statement1")
print("Statement2")
#you can write the above two statements in the following way
print("Statement3");print("Statement4")
Statement1
Statement2
Statement3
Statement4

#indentation

x=1
if x>0
print("This statement has no Indentation") #print a string

#this will display an error message "Expected an indented block"

#correct way:
x=1
if x>0 
 print("This statement has a single space indentation.")

#correct way no. 2
x=1
if x>0
  print("This statement has single Tab Indentation.")

#correct way no. 3

x=1
if x>0
   print("This statement has a single space+tab indentation.")

#data types

a=752
b=3.15
c=9+5j
d= true

print(type(a))
print(type(b))
print(type(c))
print(type(d))

#outputs
<class 'int'>
<class 'float'>
<class 'complex'>
<class 'bool'>

#complex numbers

x = complex(2,5)
print(type(x))

<class 'complex'>

#strings

str1 = "String1"
print(str1)
print(type(str1))

String1
<class 'str'>

#special characters

print("This is a backslash (\\) sign")
print("This is a tab \t key")
print("These are \' single quotes\' ")
print("These are \"double quotes\"")
print("This is a a new line \n New Line")

This is a backslash (\) sign
This is a tab    key
These are 'single quotes'
These are "double quotes"
This is a new line
New Line

#String Indices

string1 = "PYTHON TUTORIAL"
print(string1[0])
print(string1[1])
print(string1[3])
print(string1[-8])
print(string1[15])

#output

P
Y
H
T
L

#Lists

list1 = [1,2,3,4,5]
print(list1)
print(type(list1))

list2 = [1.1,2.2,3.3,4.4,5.5]
print(list2)
print(type(list2))

list3 = [100, 'color', True]
print(list3)
print(type(list3))

#output

[1, 2, 3, 4, 5]
<class 'list'>
[1.1, 2.2, 3.3, 4.4, 5.5]
<class 'list'>
[100, 'color', True]
<class 'list'>

#list indices

print(list3[2])

True

# list slices
print(list1[: 3])
print(list2[-3: -1])

#output

[1, 2, 3]
[3.3, 4.4]
