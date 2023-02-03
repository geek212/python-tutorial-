# Integer e:g like -5, -4, 4 ,3, 45, 0, 7 etc numbers with no decimal 
# mobilenumber = 123456789
# a = 89
# b = "98"
# c = '456'
# userage =57657

# float e:g such as 1.2345,-02.56,89.5,1.45 etc 
# a = 5.5
# b = 6.78
# userheight = 5.46
# userweghit = 7.89
# c = 6.56
# d = 67.7
# e= 45.8

# String refers to text To declare a string, you can either use variableName = ‘initial value’ (single quotes) or variableName = “initial value”(double quotes)

# eg: variablename ='intial value'
# variable name = "intial value"
# variable name = '''intial value'''

# username = 'peter'
# userage = "56"
# userspousename = '''alycia'''

# In the  example, if we wrote userAge = ‘56’, userAge is a
# string. In contrast, if you wrote userAge = 56 (without quotes),
# userAge is an integer.

''' Booleans represent one of two values: True or False.'''

# In programming you often need to know if an expression is True or False.

# You can evaluate any expression in Python, and get one of two answers, True or False.

# When you compare two values, the expression is evaluated and Python returns the Boolean answer:
# a >= 0 a <= 100
# 5 < 6  b < 6  c < 6

# The Boolean values in Python are True and False,
# typically used to control if-statements and while-loops.


""" Boolean operators 
The Boolean operators work with Boolean values (True or False) and are used to 
determine if one or more things is True or False."""

# Python Boolean Operators #

# Operator Code Example What It Determines #

# or x or y Either x or y is true
# and x and y Both x and y are true
# not not x x is not full


# None/not

'''The None keyword is used to define a null value, or no value at all.
None is not the same as 0, False, or an empty string. None is a data type
of its own (NoneType) and only None can be None.'''

# x = None
# print(x)

# Types of variables in print 

# a = '56'   # string type
#c = 9.5    # float type
#d = = 89     # int type    ''' this is numeric data types int, / float .
#b False  # bool type
#d = None  # none type
#e = 9>78   # bool type

# printing this variables
# print(a)
# print(b)
# rint(c)
# printp(d)
# print(d)
# print(e)

# # now we use types ith print function

# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
#print(type(e))


a = 67                        # its a integer numeric 
print (type(a))

b = 7.56                       # its a float numeric
print (type(b))

c = 67j                        # its a complex numeric
print (type(c))


# Understanding Complex Data Type in Python

'''A complex number has two parts, real part and imaginary part. 
 numbers are represented as A+Bi or A+Bj, 
 A is real part and B is imaginary part.

Python supports complex data type as built-in feature which means we 
 directly perform different operations on complex number in python.
 python uses A+Bj notation to represent complex number
 meaning python will recognize 3+4j as a valid number but 3+4i is not valid.'''

 # Creating Complex Data Type Using complex()

user_age = 78
user_size = 9

overallsize =complex(user_age,user_size)
print(overallsize)     # output was 78+9j

# Reading Complex Number From User

"""We can read complex number directly from user using built-in function input().
 Since function input() returns STRING we must convert result to complex 
 using function complex(). Try following example"""

user_age = complex(input("Entercomplex number"))
print('Given complex number is',user_age)

# list data type
# Tuple data type
# Dictionary type
# set type 

