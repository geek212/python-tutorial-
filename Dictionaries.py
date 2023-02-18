'''
Data dictionaries are kind of 
like lists.But instead of each item in the list 
being identified by its position in the list, each item is uniquely identified 
by a key. You can define the key, which can be a string or a number, yourself. All 
that matters is that it be unique to each item in the dictionary

The key in a dictionary represents one unique thing, and you can associate a value
with that key. The value can be a number, string, list, tuple — just about anything, 
really. So you can think of a data dictionary as being kind of like a table where the 
first column contains a single item of information that’s unique to that item and 
the second column, the value, contains information that’s relevant to, and perhaps 
unique to, that key

'''



'''Creating a Data Dictionary'''

'''The code for creating a data dictionary follows the basic syntax:

name = {"key":"value","key":"value","key":"value",...}

The name is a name you make up and generally describes to whom or what the 
key-value pairs refer. The key:value pairs are enclosed in curly braces. The key
values are usually strings enclosed in quotation marks, but you can use integers 
instead if you like. Each colon (:) separates the key name from the value assigned 
to it. The value is whatever you want to store for that key name, and can be a 
number, string, list...pretty much anything. The ellipsis (...) just means that 
you can have as many key-value pairs as you want. Just remember to separate the 
key-value pairs with commas, as shown in the syntax example


To make the code more readable, developers often place each key-value pair on a 
separate line. But the syntax is still the same.

name = {
    "key":"value",
    "key":"value",
    "key":"value",
    ...
}

'''
mydict = {
   "fast" : "my car is fast as horse",
    "ashwin": "is takla man",
    "names": "rahvana",
     "marks": [3,4,5,6],    # u can store list
     "anotherdict": {"harry": "is a coder"}   # 

}

print(mydict['fast'])
print(mydict['ashwin'])
print(mydict['names'])
print(mydict['marks'])
print(mydict["anotherdict"]["harry"])


# python Dictionries properties

# its a unorderd
# its mutable
# its indexed
# Cannot conatains duplicate keys

# Cerate dictionary of names 

students_dict = {
    "standrand x":"Rahul",
    "standrand XII":"Suraj",
    "standrand XI":"DAniel",
    "standrand XIII":"Rashaa"
}

print(students_dict["standrand x"])
# print(students_dict["standrand XII"]) 
# print(students_dict["standrand XI"])
# print(students_dict["standrand XIII"])
 
#  print(student_dict[students]) # this output will showcase error

# Dictionary methods


# Getting the length of a dictionary
# The number of items in a dictionary is considered its length. As with lists, you can 
# use the len() statement to determine a dictionary’s length. The syntax is:
# len(dictionaryname)
# As always, replace dictionaryname with the name of the dictionary you’re checking. For example, 
# the following code creates a dictionary, then stores its length in 
# a variable

# len(dictionaryname)

students_dict = {
    "standrand x":"Rahul",
    "standrand XII":"Suraj",
    "standrand XI":"DAniel",
    "standrand XIII":"Rashaa"
}

 # Count the number of key:value pairs and put in a variable.
how_manystudents = len(students_dict)
print(how_manystudents) # Both output will give 4 keys and value

# or u can use simple method for len output
print(len(students_dict))

# Seeing whether a key exists in a dictionary

# You can use the in keyword to see whether a key exists. If the key exists, then 
# in returns True. If the key does not exist, in returns False.


print("standrand x" in students_dict)   # True
print("Suraj" in students_dict)          # False
print("standrand XIII" in students_dict) # True


# Getting dictionary data with get()

'''
Getting dictionary data with get()
Having the program kind of crash and burn when you look for something that 
isn’t in the dictionary is a little harsh. A more elegant way to handle that is to use 
the .get() method of a data dictionary. The syntax is:
dictionaryname.get(key)
Replace dictionaryname with the name of the dictionary you’re searching. Replace 
key with the thing you’re looking for. Notice that get() uses parentheses, not 
square brackets. If you look for something that is in the dictionary, such as this

'''



students_dict = {

    "standrand x":"Sumit",
    "standrand XII":"Sunil",
    "standrand XI":"DAnny",
    "standrand XIII":"Rahul"

}

student_name = "harry"
print(students_dict.get(student_name))
# What makes .get() different is what happens when you search for a nonexistent name. 
# You don’t get an error, and the program doesn’t just crash and burn. 
# Instead, get() just gracefully returns the word None to let you know that no person 
# named "harry" is in the students_dict dictionary



# student_name = "jaky"
# print(student_dict.get(student_name))

# You can actually pass two values to get(), the second one being what you want it 
# to return if the get fails to find what you’re looking for. For instance,
#  in the following line of code we search for jaky again, but this time if it doesn’t 
# find that student_name it doesn’t display the word None. Instead, it displays the rather 
# more pompous message (error)


# Changing the value of a key

'''
Dictionaries are mutable, which means you can change the contents of the 
dictionary from code (not that you can make the dictionary shut up). The syntax 
is simply:
dictionaryname[key] = newvalue
Replace dictionaryname with the name of the dictionary, key with the key that 
identifies that item, and newvalue with whatever you want the new value to be.

'''

# print(students_dict["standrand XI"])

# students_dict["standrand XI"] = "Arjun"
# print(students_dict["standrand XI"])
 


# Adding or changing dictionary data

'''
You can use the dictionary update() method to add a new item to a dictionary, or 
to change the value of a current key. The syntax is
dictionaryname.update(key, value)
Replace dictionaryname with the name of the dictionary. Replace key with the 
key of the item you want to add or change. If the key you specify doesn’t already 
exist with the dictionary, it will be added as a new item with the value you specify. 
If the key you specify does exist, then nothing will be added. The value of the key 
will be changed to whatever you specify as the value

'''





 