# What’s a Tuple ?

''' In addition to lists, Python supports a data type {u can call data structure also} known 
as a tuple. Some people pronounce that like two-pull.

A tuple is just an immutable list

The syntax for creating a tuple is the same as the syntax for creating a list, except 
you don’t use square brackets. You have to use parentheses

like this:

numbers = (23,34,4,567,234,23)

Most of the techniques and methods that apply on list , tuple otherhand is imputable
or u can say u cannot modified tuple like list '''

# Cerate a tuple ()
t = (23,34,4,567,234,23)

# print the tuple
print(t[0])

# cannot modified tuple
# t[0] = 34   this will show error

# Cerate a tuple ()

student_idno = (1,34.34, 345, 234)
# u can use numbers only on tuple if use let say student_name like mike , raj, with () it will show error 
print(type(student_idno))

# Cerate a tuple 
number = (2)
print(type(number))   
# imp if u use (2) without , it will be not tuple datatype it will be int
number = (2,)
print(type(number))
# if u use (2,) it will recoginze that its tuple datatype 



# There are some methods but its minimum compare to list 

'''Any of the methods that alter data, or even just copy data, from a list cause an 
error when you try them with a tuple. This incudes .append(), .clear(), .copy(), 
.extend(), .insert(), .pop(), .remove(), .reverse(), and .sort(). In short, 
a tuple makes sense if you want to show data to users without giving them any 
means to change any of the information.'''

# lets start with the methods for Tuple data type

# 1.len()
sold_value = (34.4,3421,123,56,56,76,345,7865,45.454,3421)
# print(len(4))  # dont use this type of output remember tuple is imputable
print(len(sold_value))
print(sold_value.count(3421))  # this means how many times 3421 counts in the tuple
print(sold_value.index(123))  # this search numbers index were it is located 123 is 2 in index 


