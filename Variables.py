# What are variables?

'''Variables are names given to data  that we need to store and manipulate
in our programs'''

#  To do that, we can name this data userAge and define the variable userAge 

userage = 0 
 
'''After you define the variable userAge, your program will allocate a
certain area of your computer's storage space to store this data. You can
then access and modify this data by referring to it by its name, userAge.
Every time you declare a new variable, you need to give it an initial value.
In this example, we gave it the value 0. We can always change this value
in our program later'''

a= 8                 # Variables contains for store of value
b= "Ashwin"           # Keywords reserved in python identifies = class / function
b = '''Ashwin'''      # We can also define multiple variables
c=89.98
print(a)
print(b)
print(c)

userage = 9,             # A variable name in Python can only contain letters (a - z, A - B), numbers
UserWarning = 9          # or underscores (_). However, the first character cannot be a number.
username = 'Ashwin'
print (userage)
print (username)
print  (UserWarning)

userName = 9                  # variable names are case sensitive. username is not the same as username
this_Is_AVariable_Name = 87
print (userName)
print (this_Is_AVariable_Name)

# Variables are a big part of Python and all computer programming languages. 
# A  variable is simply a placeholder for information that may vary (change). For 
# example, when you browse Amazon today, you can see your name and “member 
# since” date appear on their home page 


#### Creating valid variable names ####


# In our explanation of what a variable is we used names like Quantity and Unit 
# Price, and this is certainly fine for a general example. Those are names we just 
# made up. In Python, you can also make up your own variable names. But the rules 
# are more stringent than when making them up in plain English. Python variable 
# names have to conform to certain rules to be recognized as variable names. The 
# rules are . #

#  The variable name must start with a letter or underscore (_).

##  After the first letter you can use letters, numbers, or underscores.

###  Variable names are case-sensitive, so once you make up a name, any other 
#  reference to that variable must use the same uppercase and lowercase letters 
#  as the name you originally made up.

####  Variable names cannot be enclosed in, or contain, single or double quotation 
#  marks.

""" Praticeing manipulating variables """

# Praticeing my python variable
# This variable contains integer
quantity = 10

# This variable contains float
unit_price = 1.99

# This variable contains the result of multiplying quantity times of unit price
extended_price = quantity * unit_price

# Show the result
print (extended_price)

""" That’s because 
you’re just getting started and so need to keep things simple. The only indication 
that the app ran at all is the number 19.9 in the results. This is the output from 
print(extendedprice) in the code, and it’s 19.9 because the quantity (10) times 
the unit price (1.99) is 19.9 """


# Praticeing my python variable 2
# This variable contains integer
quantity = 20

#This variable contains float
unit_price = 2.88

# This variable contains the result of division quantity times of unit price
extended_price = quantity / unit_price

# Show the result
print (extended_price) 

# variables with operators and strings u should use string either double quote or single quote

frist_name = "Ashwin"
last_name = "nair"
full_name = frist_name + " " + last_name
print("hello"+ " "+ full_name)

frist_name = "sabin"
last_name = "nair"
full_name = frist_name + " " + last_name    
print("yo yo"+ " "+ full_name)


frist_name = "ashwin"
last_name = "nao"
full_name = frist_name + " " + last_name
print("hi"+ " " + full_name)

frist_name = "ashwin"
last_name = "kumar sudhakar nair"
full_name = frist_name + " " + last_name
print("hello how are you"+ " " + full_name)

username = "akash"
userlast_name = "kumar"
full_name = username + "  " + userlast_name
print("welcome to google akash kumar")


# quantity_price = 24
# unit_price = "45.34"                          u cannot use int and str for arthemtic operation
# overall_cost = quantity_price + unit_price     it shows error in variables chapter
# print("profit margin is ")





# Variables in strings

name = "ada lovelace"
print(name.title())
# The title() method changes each word to title case, where each word 
# begins with a capital letter



#  you can change a string to all uppercase or all lowercase
name = "Ada Lovelace"
print(name.upper())

name = "ADA LOVELACE"
print(name.lower())





# To insert a variable’s value into a string, place the letter f immediately 
# before the opening quotation mark. Put braces around the name or names 
# of any variable you want to use inside the string. Python will replace each 
# variable with its value when the string is displayed.
# These strings are called f-strings. The f is for format, because Python 
# formats the string by replacing the name of any variable in braces with its 
# value.

name = "Ashwin"
last_name = "nair"
full_name = f"{name} {last_name}"
print(full_name)
# F-strings were first introduced in Python 3.6.




# Constant change  in variable of python 

# A constant is like a variable whose value stays the same throughout the life 
# of a program. Python doesn’t have built-in constant types, but Python programmers use all capital 
# letters to indicate a variable should be treated as a 
# constant and never be changed.a

MAXCR = 456
print(MAXCR)

# When you want to treat a variable as a constant in your code, make the 
# name of the variable all capital letters.





