# Type_casting is type of function is used to find datatypes of given variable in python

a = 976   # Example 1 of typcasting
a = int(a)
print(a+34)
print(type(a))

b = "ashwin"
b = str(b)
print(b)
print(type(b))

c = "678"
c = int(c)
print(c-78)
print(type(c))


# Why to Use Type-Casting in Python?

#  Let us take a real world example to understand the need of type
#  casting in Python. Suppose a person is travelling to America 
#  from India and that person wants to buy something from a store 
#  in America. But that person only has cash in INR(Indian Rupees). 
#  So, the person goes to get their money converted from INR to USD 
#  (American Dollar) from a local bank in America. This analogy is simialr
#   to what type casting in python is.

# If we have a specified value or an object and we want to convert it into a string 
# , we use the str() method in python. Similarly, we use the float() method to convert
#  a specified value or an object into a floating-point number or a floating object,
#   and the int() method to convert an object into an integer value or an integer object.

# So, to convert one data type into another data type, we use the typecasting in python


# There are two varieties of typecasting in python namely -

# Explicit Conversion(Explicit type casting in python), and
# Implicit Conversion(Implicit type casting in python). '''

# Explict Conversion

'''The conversion of one data type into another data type,
done via developer or programmer intervention or manually as per the
requirement, is known as explicit type conversion. It can be achieved with 
the help of Python’s built-in type conversion functions such as int(), float(), hex(), 
(), str(), etc .

Explicit type conversion is also known as 
Explicit Type Casting in Python or simply Type 
Casting in Python.'''

# implicit Conversion

""" Data types is not the same in Python. Data types have a certain ordering in which Python handles them. 
of the data types have higher-order, and some have lower order. While performing any operations on 
variables with different data types in Python, one of the variable's data types will be changed to 
higher data type. According to the level, one data type is converted into other by the Python interpreter 
(automatically). This is called, implicit type casting in python. 
Python converts a smaller data type to a higher data type to prevent data loss."""


# Example 2 of  typecasting

string = "78"
number = 6

# Converting string to integer

string_number = int(string)

sum_of_numbers = number + string_number
print("the Sum of both numbers is:", sum_of_numbers)

# Example 3 of typecasting 

integer = 89
number = 98

# Converting integer to string

integer_number = int(string)

sum_of_numbers = integer_number * number
print("the Sum of both numbers is : ", sum_of_numbers)

# u can use variables with datatypes also like this also refer to typcasting with str ()


age = 21
age+= 1
print("your age is : "+ " " , str(age))


user_age = 7
user_length = 9.7
print("user age matchs with length" + " " , str(age))
 


