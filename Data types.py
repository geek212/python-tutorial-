# Integer e:g like -5, -4, 4 ,3, 45, 0, 7 etc numbers with no decimal 

'''An integer is any whole number, positive or negative. There is no limit to its size. 
 Numbers like 0, -1, and 999999999999999 are all perfectly valid integers. From 
 your perspective, an integer is just any valid number that doesn’t contain a decimal point.'''

# mobilenumber = 123456789
# a = 89
# b = "98"
# c = '456'
# userage =57657

# float e:g such as 1.2345,-02.56,89.5,1.45 etc 

''' A floating point number, often called a float for short, is just any valid number that contains a decimal point. Again, there is no size limit, 1.1 and -1.1 and 
123456.789012345 are all perfectly valid floats.

If you happen to work with very large scientific numbers, you can put an e in a 
number to indicate the power of 10. For example, 234e1000 is a valid number, and 
will be treated as a float even if there’s no decimal point. If you’re familiar with 
scientific notation, you know 234e3 is 234,000 (replace the e3 with 3 zeroes). If 
you’re not familiar with scientific notation, don’t worry about it. If you’re not 
using it in your day-to-day work now, chances are you’ll never need it in Python 
either '''


# a = 5.5
# b = 6.78
# userheight = 5.46
# userweghit = 7.89
# c = 6.56
# d = 67.7
# e= 45.8

# String refers to text To declare a string, you can either use variableName = ‘initial value’ (single quotes) or variableName = “initial value”(double quotes)
# string is text data type

# variablename ='intial value'
# variable name = "intial value"
# variable name = '''intial value'''

# username = 'peter'
# userage = "56"
# userspousename = '''alycia'''

# In the  example, if we wrote userAge = ‘56’, userAge is a
# string. In contrast, if you wrote userAge = 56 (without quotes),
# userAge is an integer. or u write 6.56 its a float 

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

# x or y Either x or y is true
# and x and y Both x and y are true
# not not x x is not false 


# None/not

'''The None keyword is used to define a null value, or no value at all.
None is not the same as 0, False, or an empty string. None is a data type
of its own (NoneType) and only None can be None.'''

# x = None
# print(x)

# Types of variables in print 

a = '56'   # string type
c = 9.5    # float type
d =  78    # int type    this is numeric data types int / float / str / bool / none / complex.
b = False  # bool type
e = None  # none type
f = 9>78   # bool type
g = 78j    # complex type

k = range(6)

'''What Is Range In Python?'''

#  It is an in-built function in Python which returns a sequence of
#  numbers starting from 0 and
#  increments to 1 until it reaches a specified number.
#  The most common use of range function is to iterate sequence type.

u = ("name” : “John”, “age” : 36")
# # printing this variables

print(a)
print(c)
print(d)
print(b)
print(e)
print(f)
print(g)


print(k)
print(u)
# # now we use types ith print function

print(type(a))
print(type(c))
print(type(d))
print(type(b))
print(type(e))
print(type(f))
print(type(g))


print(type(k))
print(type(u))

# a = 67                        # its a integer numeric 
# print (type(a))

# b = 7.56                       # its a float numeric
# print (type(b))

# c = 67j                        # its a complex numeric
# print (type(c))


# Understanding Complex Data Type in Python

''' Just about any kind of number can be expressed as an integer or float, so being 
familiar with those is sufficient for just about everyone. Though in the interest 
of being accurate we should point out that Python also supports complex numbers. 
These bizarre little charmers always end with the letter j, which is the imaginary
part of the number. If you have absolutely no idea what we’re talking about, then 
you’re a normal person because only people who are really “out there” in math 
land care about these. If you’ve never heard of them before now, chances are you 
won’t be using them in your computer work or Python programming '''


# Python supports complex data type as built-in feature which means we 
#  directly perform different operations on complex number in python.
#  python uses A+Bj notation to represent complex number
#  meaning python will recognize 3+4j as a valid number but 3+4i is not valid.'''

#  # Creating Complex Data Type Using complex()

# user_age = 78
# user_size = 9

# overallsize =complex(user_age,user_size)
# print(overallsize)     # output was 78+9j

# # Reading Complex Number From User

# """We can read complex number directly from user using built-in function input().
#  Since function input() returns STRING we must convert result to complex 
#  using function complex(). Try following example"""

# user_age = complex(input("Entercomplex number"))
# print('Given complex number is',user_age)

# # Python has various built-in data types

# # Numeric - int, float, complex
# # String - str
# # Sequence - list, tuple, range
# # Binary - bytes, bytearray, memoryview
# # Mapping - dict
# # Boolean - bool
# # Set - set, frozenset
# # None - None
# """ Sequence """
 
 
 







