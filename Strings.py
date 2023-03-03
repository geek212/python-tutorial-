# Manipulating Strings #

# In Python and other programming languages, we refer to words and chunks of 
# text as strings, short for “a string of characters,” which has no numeric meaning 
# or value.

# Example 1

a = "Ashwin" # Double quote string
b = 'Ashwin' # single quote string
c = '''Ashwin''' # Triple quote string
print(a)
print(b)
print(c)

# Example 2

Frist_username = 'Ashwin'
Last_name = "Nair"
full_name = Frist_username + " " + Last_name  # u can use double quote string for spaces in the output
print(full_name)

# Because Python won’t automatically put in spaces where you think they should 
# go, you’ll have to put them in yourself. The easiest way to represent a single space 
# is by using a pair of quotation marks with one space between them.

####################################################################################################



# [Getting the length of a string
# To determine how many characters are in a string, use the built-in len() function 
# (short for length). The length includes spaces because spaces are characters, each 
# one having a length of one. An empty string — that is, a string with nothing in it, 
# not even a space — has a length of zero.
# Here are some examples. In the first line we define a variable named s1 and put 
# an empty string in it (a pair of quotation marks with nothing in between). The 
# s2 variable gets a space (a pair of quotation marks with a space between). The s3
# variable gets a string with some letters and spaces. Then, three print() functions 
# display the length of each string']

# Example 1 

a = "ashwin"
b = "arjun"
c = "sabin"

print(len(a)) 
print(len(b))
print(len(c))

# Here is the output from that code, when executed, which makes perfect sense 
# when you understand how len() measures the length of strings as the number of 
# characters (including spaces) contained within the string [6,5,5] is the output


""" Python offers several operators for working with sequences of data. One weird 
thing about strings in Python (and in most other programming languages) is that 
when you’re counting characters, the first character counts as zero, not one. 
This makes no sense to us """



# String slicing


'''String in python can be sliced in string'''

#  Ashwin A:0 S:1 H:2 W:3 I:4 N:5
# 012345  index in string start from 0 to 1 in python

# # Example 1 
user_ashwin = "Ashwin"

print(user_ashwin[0])
print(user_ashwin[1])
print(user_ashwin[2])
print(user_ashwin[3])
print(user_ashwin[4])
print(user_ashwin[5])

# u can use string slicing

print(user_ashwin[0:4])
print(user_ashwin[0:5])
print(user_ashwin[0:6])
# one more example how u can slice the string
print(user_ashwin[2:4])
print(user_ashwin[3:2])
print(user_ashwin[1:5])
print(user_ashwin[000:32454])  
print(user_ashwin[0::2]) # skip value
print(user_ashwin[3:4:2]) # skip value

# # Negative indexis #

print(user_ashwin[0])
# 


print(user_ashwin[-3])
print(user_ashwin[-0:4])
print(user_ashwin[-0:-4])




# # u cannot change string like name[4] = "guik" this will show error



# Built-In Methods for Python Strings sequence

# Method Purpose

# s.capitalize() Returns a string with the first letter capitalized, the rest lowercase.

# s.count(x,[y.z]) Returns the number of times string x appears in string s. Optionally you can add y as 
# a starting point and z as an ending point to search only a portion of the string.

# s.find(x,[y.z]) Returns a number indicating the first position at which string x can be found in string 
# s. Optional y and z parameters allow you to limit the search to a portion of the 
# string. Returns –1 if none found.

# s.index(x,[y.z]) Similar to find but returns a “substring not found” error if string x can’t be found 
# in string y.

# s.isalpha() Returns True if s is at least one character long and contains only letters (A-Z or a-z).
# s.isdecimal() Returns True if s is at least one character long and contains only numeric 
# characters (0-9).

# s.islower() Returns True if s contains letters and all those letters are lowercase.
# s.isnumeric() Returns True if s is at least one character long and contains only numeric 
# characters (0-9).

# s.isprintable() Returns True if string s contains only printable characters.

# s.istitle() Returns True if string s contains letters and the first letter of each word is uppercase 
# followed by lowercase letters.

# s.isupper() Returns True if all letters in the string are uppercase.

# s.lower() Returns s with all letters converted to lowercase.

# s.lstrip() Returns s with any leading spaces removed.


# s.replace(x,y) Returns a copy of string s with all characters x replaced by character y.

# s.rfind(x,[y,z]) Similar to find but searches backwards from the start of the string. If y and z are 
# provided, searches backwards from position z to position y. Returns –1 if string x
# not found.

# s.rindex() Same as .rfind but returns an error if the substring isn’t found.

# s.rstrip() Returns string x with any trailing spaces removed.

# s.strip() Returns string x with leading and trailing spaces removed.

# s.swapcase() Returns string s with uppercase letters converted to lowercase and lowercase letters 
# converted to uppercase.

# s.title() Returns string s with the first letter of every word capitalized and all other letters 
# lowercase.

# s.upper() Returns string s with all letters converted to uppercase.

'''String function'''

a = "Ashwin was loser of all time he have no job , no carrer , or mooney"

print(len(a))
print(a.endswith("job")) # output will be either true or false
print(a.count("mooney"))  # output will "mooney" like word count 1 or 4 on words 
print(a.capitalize())
print(a.replace("Ashwin was loser", "Ashwin was a hero"))  # it replace the words
print(a.find(" mooney"))     # it finds te word in number like 60
print(a.casefold())     # converts text into small letters
print(a.isspace())  # bool output 
print(a.isnumeric()) # bool output
#  there more str function


# String escape sequence
# Escape squence character comprises more than one character but represent more than one character 
# when used witin the string Eg: \n , \\ , \t , etc

story = "Harry is good\n.\nHe\tis ve\\ry go\\od"
print(story)

notes = "computer understa\nnd the language \tof numbers of binar\\y"
print(notes)


# pratice with input and replace str function

Addmission = '''Dear <|NAME|>
your are selected for the interview in 
cod in mumbai
Date : <|DATE|>
'''
name = input("Enter your name\n")
date = input("Enter date\n")

Addmission = Addmission.replace("<|NAME|>", name)
Addmission = Addmission.replace("<|DATE|>", date)

print(Addmission)


letter = '''Dear name
your are selected for the interview
in mumbai for interinship
DATE : <|DATE|>
'''
NAME = input("Enter your name")
date = input("Enter DATE")

letter = letter.replace("name", NAME)
letter = letter.replace("<|DATE|>", date)

print(letter)




# Avoiding Syntax Errors with Strings

# One kind of error that you might see with some regularity is a syntax error. 
# A syntax error occurs when Python doesn’t recognize a section of your program as valid Python code.
#  For example, if you use an apostrophe within 
# single quotes, you’ll produce an error. 
# This happens because Python interprets everything between the first single quote and the apostrophe as a 
# string. It then tries to interpret the rest of the text as Python code, which 
# causes errors

# Example 1 Avoid synatax error with strings

# name = 'ashwin'.'
# print(name)
# # Python can’t identify where the string 
# should end

name = "ashwin ."  # this is apostrophe
print(name)
# The apostrophe appears inside a set of double quotes, so the Python 
# interpreter has no trouble reading the string correctly



