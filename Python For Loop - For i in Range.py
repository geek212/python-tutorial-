
'''
Loops are one of the main control structures in any programming language, and Python is no different.

we will look at a couple of examples using for loops with Python's range() function.

for loops work slightly differently than they do in languages such as JavaScript or C.

A [for] loop sets the iterator variable to each value in a provided list, array, or string and repeats
the code in the body of the [for] loop for each value of the (iterator) variable.

'''

#  In the example below, we use a for loop to print every number

for i in [1, 2, 3, 4, 5]:
    print(i , end=", ") # prints output [1, 2,  3, 4, 5]

# "i" is a temporary variable used to store the integer value of the current position in the
#  range of the for loop that only has scope within its for loop.
#  You could use any other variable name in place of "i" such as "count" or "x" or "number".

# What does end=’ do in Python?

# The end parameter in the print function is used to add any string. At the end of the output
#  of the print statement in python .

# Passing the whitespace to the end parameter (end=‘ ‘) indicates that the end character has to 
# be identified by whitespace and not a newline .

# Example 1
print("Welcome to" , end = ' ')
print("prutor.ai", end = ' ')

# Example 2
print("Hello how are you", end= ' ')
print("i m fine",end= ' ' )

# What is for ?

'''
A for loop is used for iterating over a sequence 
(that is either a list, a tuple, a dictionary, a set, or
a string).This is less like the for keyword in other programming languages, 
and works more like an iterator method as found in other object-orientated programming languages.
With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.


iterating meaning :

is the repetition of a process in order to generate a sequence of outcomes
Each repetition of the process is a single iteration, and the outcome of each iteration
is then the starting point of the next iteration. 
[In mathematics and computer science, iteration is a standard element of algorithms]

in simple word  is the repetition of a process in order to generate a sequence of outcomes.
or u can say "to say or do again or again and again" 


Python “in” operator

Basically, the in operator in Python checks whether a specified 
value is a constituent element of a sequence like string, array, list, or tuple etc.

When used in a condition, the statement returns a Boolean result evaluating 
into either True or False. When the specified value is found inside the sequence,
the statement returns True. Whereas when it is not found, we get a False.


'''
# Example for "in" 

list1 = [1 , 2 , 3, 4]
string1 = "My name is ashwin"
tuple1 = (1, 4, 5, 6)


# Firstly, we have initialised a list list1, a string string1 and a tuple tuple1 with some values.
# Then we use the in operator to check whether some values are part of the above sequences or not.

print( 3 in list1)
print("name"in string1)
print(6 in tuple1)

#  Example  2 for in 

list1= [1,2,3,4,5]
string1= "My name is AskPython"
tuple1=(11,22,33,44)
 
print(5 in list1) #True
print("is" in string1) #True
print(88 in tuple1) #False

# Example 3 for in 

user_no= [45, 5, 5, 43, 45]
user_name= "My name is not ashwin"
tuple2= (34, 343, 345, 2345,)

print(45555 in user_no)  # this a int
print("not" in user_name) # use str for print output for string variable
print(0 in tuple2)  # this a int

