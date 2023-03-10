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
# print(student_dict.get(student_name)) error output

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
 
# Rename or change  a Key in a Python Dictionary

#   dictionary
ini_dict = {

    'kunal': 1, 
    'harry': 5,
	'jhonny': 10,
    'akshat': 15
             
}

# printing 
print("initial 1st dictionary", ini_dict)

# changing keys of dictionary
ini_dict['akash'] = ini_dict['akshat']
del ini_dict['akshat']


# printing final result
print("final dictionary", str(ini_dict))


# Rename a Key in a Python Dictionary using Python pop() 

#  dictionary
ini_dict = {

    'nikhil': 1,         
    'vashu': 5,
	'manjeet': 10,
    'akshat': 15
}

# printing initial json
print("initial 1st dictionary", ini_dict)

# changing keys of dictionary
ini_dict['akash'] = ini_dict.pop('akshat')

# printing final result
print("final dictionary", str(ini_dict))

    
    
       
    
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


#  make a drictionories of two names

Employee_name = {
    "Gary" : "neel",
    "yasav": "janet"
} 

# Change the value of "yasav"

Employee_name.update({"yasav":"berttman"})

#  update the dridtioner with new pair
Employee_name.update({"Danny":"King"})

print(Employee_name)

#  Adding the following lines to the 
# end of that code displays everything in the dictionary:

# Show what is in dictionaries
for person in Employee_name.keys() :
    print(person + "'='" + Employee_name[person] )
# "'='" is only for spaces

# As you may have guessed, you can loop through a dictionary in much the same 
# way you loop through lists, tuples, and sets.


#  IMP
# If the key already exists in the dictionary, then its value is updated, because no 
# two items in a dictionary are allowed to have the same key

# IMP
# If the key does not already exist, then the key-value pair is added because 
# there is nothing in the dictionary that already has that key, so the only choice 
# is to add it.

 


#  Looping through a Dictionary

# You can loop through each item in a dictionary in much the same way you can loop 
# through lists and tuples. But you have some extra options. If you just specify the 
# dictionary name in the for loop, you get all the keys

student_name = {



    #Keys  : values

    "Harry":"jaket",
    "Janet":"jackson",
    "mike":"ken",
    "karan":"shrama",
    "harry":"coder"
}

for students in student_name:
    print(students)

#  Above is looping dictionaries for keys with [ for] and [in]


# If you want to see the value of each item, keep the for loop the same, but print 
# dictionaryname[key] where dictionary name is the name of the dictionary this
# way with syntax dictionaries_name[key]


for students in student_name:
    print(student_name[students])


# You can also get all the names just by using a slightly different syntax in the for
# loop: . . . add .{values()} to the dictionary name as in the following. Then you can 
# just print the variable name (students), and you will still see the value before you’re 
# looping through the values. 


for students in student_name.values():
    print(students)



#  loop through the keys and values at the same time by using 
# {items()} after the dictionary name in the for loop. But you will need two variables 
# after the for as well, one to reference the key, the other to reference the 
# value. If you want so see both as you’re looking through, then you’ll need to use 
# those same names inside the parentheses of the print

for key , values in student_name.items():
    print(key,  '=', values)



# Data Dictionary Methods

# Method  :       What it Does

# clear() : Empties the dictionary by remove all keys and values.

# copy() : Returns a copy of the dictionary.

# fromkeys() : Returns a new copy of the dictionary but with only specified keys 
#               and values.

# get() : Returns the value of the specified key, or None if it doesn’t exist.

# items() : Returns a list of items as a tuple for each key-value pair.

# keys() :Returns a list of all the keys in a dictionary.

# pop() : Removes the item specified by the key from the dictionary, and stores 
#         it in a variable.

# popitem() : Removes the last key-value pair


# setdefault() : Returns the value of the specified key. If the key does not exist: insert 
#                the key, with the specified value.

# update() : Updates the value of an existing key, or adds a new key-value pair if 
#             the specified key isn’t already in the dictionary.

# values() : Returns a list of all the values in the dictionary.

#   all()    : Return True if all keys of the dictionary are True (or if the dictionary is empty)

#   any()	 : Return True if any key of the dictionary is true. If the dictionary is empty, return False.




#  now some reaming methods like copying in dictionaries

# If you need to make a copy of a data dictionary to work with, use this syntax:
# newdictionaryname = dictionaryname.copy()
# Replace newdictionaryname with whatever you want to name the new dictionary. 
# Replace dictionaryname with the name of the existing dictionary that you want 
# to copy


share_market = {

    "Tata":"Motors",
    "mahindra":"motors",
    "maruti":"suzuki",
    "lanser":"turbo"
}

# Make a copy of this dictionaries of share_market put in motors_market
motors_market = share_market.copy()

# show the output of both share_market and motors_market
print(share_market)
print(motors_market)

#  we created another dictionary named motors_market as a copy of thatcompanys
# dictionary. Printing the contents of each dictionary shows that they are indeed 
# identical.




# Deleting Dictionary Items #



# There are several ways to remove data from data dictionaries. The del keyword 
# (short for delete) can remove any item based on its key. The syntax is as follows:
# del dictionaryname[key]


Games = {

    "contra":"japan",
    "street_fighter":"japan",
    "mariobros":"usa"

}

#  i just have used some random  games and the countrys as 
#   keys and values its not specificly correct its just for
#  understanding the Dictionaries deleting methods which i will do 


# Showin orginal games keys and values with output
print(Games)

# Now i m useing del methods to earse one key and values
del Games["street_fighter"]         


# now print the del method
print(Games)

# output
# {'contra': 'japan', 'mariobros': 'usa'}

# If you forget to include a specific key with the del keyword, and specify only the 
# dictionary name, then the entire dictionary is deleted, even its name. For example, 
# if you executed del people instead of using del Games["street_fighter"] in the preceding code,
# the output of the second print(Games) would be an error, as in the 
# following, because after it’s deleted the people dictionary no longer exists and its 
# content cannot be displayed


# Clear method in Dictionaries

# To remove all key-value pairs from a dictionary without deleting the entire 
# dictionary, use the clear method with this syntax:
# dictionaryname.clear()

Mumbai = {
    "Thane":"CR",
    "Navi_mumbai":"HBR",
    "Bandra":"WR"
}

# show the orginal dictionaries of Mumbai

print(Mumbai)


# Now using clear method
Mumbai.clear()


# output 
print(Mumbai)

# {} final output with this method.
# Running this code shows that initially the people data dictionary 
# contains three property:value pairs. After using Mumbai.clear() to wipe it 
# clear, printing the people dictionary displays {}, which is Python’s way of telling 
# you that the dictionary is empty.




# Using pop() with Data Dictionaries


# The pop() method offers another way to remove data from a data dictionary. 
# It actually does two things:

# » If you store the results of the pop() to a variable, that variable gets the value 
# of the popped key.
# » Regardless of whether you store the result of the pop in a variable, the 
# specified key is removed from the dictionary.


# Cerate the Dictionaries of customers names as key and values as their surnames

Customers = {
    "Mike":"Tyson",
    "Danny":"king",
    "Henry":"leon",
    "kai":"jackson"

}

# show the real output before useing pop()
print(Customers)


# now use a variable for pop() method for dictionarie
login = Customers.pop("Henry")

# now print the variable login
print(login)

# now with popitem()
logins = Customers.popitem()
print(logins)
# If you store the results of popitem to a variable, you don’t get that item’s value, 
# which is different from the way pop() works. Instead, you get both the key and its 
# value. The dictionary no longer contains that key-value pair with popitem().


# Data dictionaries offer a variation on pop() that uses this syntax:
# dictionaryname = popitem()
# This one is tricky because in some earlier versions of Python it would remove some 
# item at random. That’s kind of weird unless you’re writing a game or something 
# and you do indeed want to remove things at random




# all() method in dictionary 

# The all() function returns True if all items in an iterable are true, otherwise it returns False.
# If the iterable object is empty, the all() function also returns True.

# Syntax
# all(iterable)

# The Python all() function returns true if all the elements of a 
# given iterable (List, Dictionary, Tuple, set, etc.) are True otherwise it returns False.
# It also returns True if the iterable object is empty. Sometimes while working on some code 
# if we want to ensure that user has not entered a False value then we use the all() function

# Iterable: It is an iterable object such as a dictionary,tuple,list,set,etc.


# All elements of dictionary are true
d = {1: "Hello", 2: "Hi"}
print(all(d))

# All elements of dictionary are false
d = {0: "Hello", False: "Hey"}
print(all(d))

# Some elements of dictionary
# are true while others are false
d = {0: "yo", 1: "Hello", 2: "Hi"}
print(all(d))

# Empty dictionary
d = {}
print(all(d))

# all() with condition - to check if all letters of word 'time' are there
l = {"t":1, "i":1, "m":2, "e":0}
print(all(ele > 0 for ele in l.values()))


# Note: In the case of a dictionary if all the keys of the dictionary are true 
# or the dictionary is empty the all() returns True, else it returns False.


# IMP
# i have use this function on list and tuple see how to performs




# Python any() method of dictionary  

# The any() function only checks the keys (not values) in the passed dictionary. 
# If any of the key is true in the dictionary then any() function returns true, else it returns false. 
# The any() function returns false for empty dictionary as well.


# all keys are true
dict1 = {1: 'False', 2: 'True'}
print(any(dict1))

# all keys are false
dict2 = {0: 'False', False: 'True'}
print(any(dict2))

# one key is false, other is true
dict3 = {0: 'False', 1: 0}
print(any(dict3))

# One key is true, '0' is not false its True
# because '0' is a string not a number
# if it is 0 without quotes then its false
dict4 = {'0': 'False'}
print(any(dict4))

# empty dictionary
dict5 = {}
print(any(dict5))

# IMP
# i have use this function on list and tuple see how to performs



# Python Dictionary fromkeys() Method

#   fromkeys() method uses this syntax:
# newdictionaryname = dict(iterable[,value])

# Replace newdictionary name with whatever you want to name the new dictionary. 
# It doesn’t have to be a generic name like product. It can be something that 
# uniquely identifies the product, such as a UPC (Universal Product Code) or SKU 
# (Stock Keeping Unit) that’s specific to your own business.
# Replace the iterable part with any iterable — meaning, something the code can 
# loop through; a simple list will do. The value part is optional. If omitted, each key 
# in the dictionary gets a value of None, which is simply Python’s way of saying no 
# value has been assigned to this key in this dictionary yet


# Returns : A newdictionary with keys mapped to None if no value is provided, 
# else to the value provided in the field.

Dcw0001 = dict.fromkeys(['name','unitprice','quantity','clearity_one','magogo'])
print(Dcw0001)

# output 
# {'name': None, 'unitprice': None, 'quantity': None, 'clearity_one': None, 'magogo': None}


#  let’s say you don’t want to type out all those key names. You just want 
# to use the same keys you’re using in other dictionaries. In that case, you can 
# use dictionary.keys() for your iterable list of key names, so long as dictionary
#  refers to another dictionary that already exists in the program. For example, in 
#  the following code, we created a dictionary named product that has some 
# key names and nothing specific for the values. Then we used DWC001 = dict.
# fromkeys(product.keys()) to create a new dictionary with the specific name 
# DWC001 that has the same keys as the generic product dictionary. We didn’t specify 
# any values in the dict.fromkeys(product.keys()) line, so each of those keys in 
# the new dictionary will have values set to None.

# Cerate a genric product ditionaries

product = {

    'name': '',
    'Unitprice': 0,
    'taxable': True,
    'in_stock': 0,
    'models': []


}

# Cerate same name Dcw0001 dictionaries that has same key values as product
Dcw0001 = dict.fromkeys(product.keys())


# output
print(Dcw0001)

# {'name': None, 'Unitprice': None, 'taxable': None, 'in_stock': None, 'models': None}

# The final print() statement shows what’s in the new dictionary. You can see it 
# has all the same keys as the product dictionary, with each value set to None.


# setdefault() method #

# lets you add a new key to a dictionary, with a predefined value.
# It only adds a new key and value, though. It will not alter the value 
# for an existing key, even if that key’s value is None. So it could come in handy 
# after the fact if you defined dictionaries and then later wanted to add a another 
# property:value pair, but only to dictionaries that don’t already have that property in them.


# useing same Dcw0001 dictinories for setdefault()


# we created the Dcw00001 dictionary 
# using the same keys as the product dictionary. After the dictionary is created, 
# setdefault('taxable',True) adds a key named taxable and sets its value to 
# True — but only if that dictionary doesn’t already have a key named taxable. It 
# also adds a key named reorder_point and sets its value to 10, but again, only if 
# that key doesn’t already exist.

product = {

    'name': '',
    'Unitprice': 0,
    'taxable': True,
    'in_stock': 0,
    'models': []


}


# Cerate a dictionery for product
Dcw0001 = dict.fromkeys(product.keys())
Dcw0001.setdefault('taxable',True)
Dcw0001.setdefault('models',[])
Dcw0001.setdefault('reorder',100)

# Show in the dictionery output with fromkeys() and setdefault()
print("Dictionary after fromkeys() and setdefault()")
print(Dcw0001)

# output
# {'name': None, 'Unitprice': None, 'taxable': None, 'in_stock': None, 'models': None, 'reorder': 100}


# So what if you really did want to set the default of taxable to True, rather than none. 
# The simple solution there would be to use the standard syntax, dictionaryname
# [key] = newvalue to change the value of the extant taxable key from None to True. 
# The second output proves that changing the value of the key in that 
# manner did work.

# Cerate a dicitionary to change taxable field from none to true
print("\nDictinoray after fromkeys() and setdefault()")
Dcw0001 ["taxable"] = True

# output
print(Dcw0001)



#  Multi-Key Dictionaries #



# For example, suppose that just knowing the person’s full name isn’t enough. You 
# want to also know the year they were hired, their date of birth, and whether or 
# not that employee has been issued a company laptop. The dictionary for any one 
# person may look more like this:

# employee = {
#  'name' : 'Haru Tanaka',
#  'year_hired' : 2005,
#  'dob' : '11/23/1987',
#  'has_laptop' : False
# }


# Suppose you need a dictionary of products that you sell. For each product you 
# want to know its name, its unit price, whether or not it’s taxable, and how many 
# you currently have in stock. The dictionary may look something like this (for one 
# product):

# product = {
#  'name' : 'Ray-Ban Wayfarer Sunglasses',
#  'unit_price' : 112.99,
#  'taxable' : True,
#  'in_stock' : 10
# }


# Notice that in each example, the key name is always enclosed in quotation marks. 
# We even enclosed the date in dob (date of birth) in quotation marks. If you don’t, it 
# may be treated as a set of numbers, as in “11 divided by 23 divided by 1987” which 
# isn’t useful information. Booleans are either True or False (initial caps) with no 
# quotation marks. Integers (2005, 10) and floats (112.99) are not enclosed in quotation marks either. 
# It’s important to make sure you always do these correctly, as 
# shown in the examples above.
# The value for a property can be a list, tuple, or set; it doesn’t have to be a single value. 
# For example, for the sunglasses product, maybe you offer two models 
# (color), black and tortoise. You could add a colors or model key and list the items 
# as a comma-separated list in square brackets like this:

product = {
 'name' : 'Ray-Ban Wayfarer Sunglasses',
 'unit_price' : 112.99,
 'taxable' : True,
 'in_stock' : 10,
 'models' : ['Black', 'Tortoise']
}


# Next let’s look at how you may display the dictionary data. You can use the simple 
# dictionaryname[key] syntax to print just the value of each key. For example, 
# using that last product example, the output of this code:

print(product['name'])
print(product['unit_price'])
print(product['taxable'])
print(product['in_stock'])
print(product['models'])

# output would be:

# Ray-Ban Wayfarer Sunglasses
# 112.99
# True
# 10
# ['Black', 'Tortoise']



# You could fancy it up by adding some descriptive text to each print statement, 
# followed by a comma and the code. You could also loop through the list to print 
# each model on a separate line. And you can use an f-string to format any data if 
# you like. For example, here is a variation on the print()


product = {

 'name' : 'Ray-Ban Wayfarer Sunglasses',
 'unit_price' : 112.99,
 'taxable' : True,
 'in_stock' : 10,
 'models' : ['Black', 'Tortoise']

}

print('Name: ', product['name'])
print('Price: ',f"${product['unit_price']:.2f}")

# A formatted string literal or f-string is a string literal that is prefixed with 'f' or 'F'. 
# These strings may contain replacement fields, which are expressions delimited by curly braces {}. 
# While other string 
# literals always have a constant value, formatted strings are really expressions evaluated at run time.
# for futher in f strings Google  python_docs for more 


print('Taxable: ',product['taxable'])
print('In Stock:',product['in_stock'])
print('Models:')

for model in product['models']:

 print(" " * 10 + model)

# The " " * 10 on the last line of code says to print a space (“ ”) ten times. In other 
# words, indent ten spaces. If you don’t put exactly one space between those quotation marks, 
# you won’t get 10 spaces. You’ll get 10 of whatever is between the 
# quotation marks, which also means you’ll get nothing if you don’t put anything 
# between the quotation marks.





#  Python Nested Dictionary


# A dictionary can contain another dictionary, 
# which in turn can contain dictionaries themselves, 
# and so on to arbitrary depth. This is known as nested dictionary.

# Nested dictionaries are one of many ways to represent structured 
# information (similar to ‘records’ or ‘structs’ in other languages).

# Create a Nested Dictionary
# A nested dictionary is created the same way a normal dictionary is created.
#  The only difference is that each value is another dictionary.

# Let’s build a dictionary that stores employee record.

D = {'emp1': {'name': 'Bob', 'job': 'Mgr'},
     'emp2': {'name': 'Kim', 'job': 'Dev'},
     'emp3': {'name': 'Sam', 'job': 'Dev'}}

# The dict() Constructor
# There are several ways to create a nested dictionary using a type constructor called dict().

# To create a nested dictionary, simply pass dictionary key:value pair as keyword arguments to
# dict() Constructor.

D = dict(emp1 = {'name': 'Bob', 'job': 'Mgr'},
         emp2 = {'name': 'Kim', 'job': 'Dev'},
         emp3 = {'name': 'Sam', 'job': 'Dev'})

print(D)
# Prints {'emp1': {'name': 'Bob', 'job': 'Mgr'},
#         'emp2': {'name': 'Kim', 'job': 'Dev'},
#         'emp3': {'name': 'Sam', 'job': 'Dev'}}
# You can use dict() function along with the zip() function, to combine separate lists 
# of keys and values obtained dynamically at runtime.

IDs = ['emp1','emp2','emp3']

EmpInfo = [{'name': 'Bob', 'job': 'Mgr'},
           {'name': 'Kim', 'job': 'Dev'},
           {'name': 'Sam', 'job': 'Dev'}]

D = dict(zip(IDs, EmpInfo))

print(D)
# Prints {'emp1': {'name': 'Bob', 'job': 'Mgr'},
#         'emp2': {'name': 'Kim', 'job': 'Dev'},
#         'emp3': {'name': 'Sam', 'job': 'Dev'}}
# You’ll often want to create a dictionary with default values for each key. 
# The fromkeys() method offers a way to do this.

IDs = ['emp1','emp2','emp3']
Defaults = {'name': '', 'job': ''}

D = dict.fromkeys(IDs, Defaults)

print(D)
# Prints {'emp1': {'name': '', 'job': ''},
#         'emp2': {'name': '', 'job': ''},
#         'emp3': {'name': '', 'job': ''}}

# Access Nested Dictionary Items
# You can access individual items in a nested dictionary by specifying key in multiple square brackets.

D = {'emp1': {'name': 'Bob', 'job': 'Mgr'},
     'emp2': {'name': 'Kim', 'job': 'Dev'},
     'emp3': {'name': 'Sam', 'job': 'Dev'}}

print(D['emp1']['name'])
# Prints Bob

print(D['emp2']['job'])
# Prints Dev
# If you refer to a key that is not in the nested dictionary, an exception is raised.

# print(D['emp1']['salary']) error 
# Triggers KeyError: 'salary'
# To avoid such exception, you can use the special dictionary get() method. 
# This method returns the value for key if key is in the dictionary, else None,
#  so that this method never raises a KeyError.

# key present
print(D['emp1'].get('name'))
# Prints Bob

# key absent
print(D['emp1'].get('salary'))
# PrintsNone
# Change Nested Dictionary Items
# To change the value of a specific item in a nested dictionary, refer to its key.

D = {'emp1': {'name': 'Bob', 'job': 'Mgr'},
     'emp2': {'name': 'Kim', 'job': 'Dev'},
     'emp3': {'name': 'Sam', 'job': 'Dev'}}

D['emp3']['name'] = 'Max'
D['emp3']['job'] = 'Janitor'

print(D['emp3'])
# Prints {'name': 'Max', 'job': 'Janitor'}
# Add or Update Nested Dictionary Items
# Adding or updating nested dictionary items is easy. 
# Just refer to the item by its key and assign a value. 
# If the key is already present in the dictionary, its value is replaced by the new one.

D = {'emp1': {'name': 'Bob', 'job': 'Mgr'},
     'emp2': {'name': 'Kim', 'job': 'Dev'},
     'emp3': {'name': 'Sam', 'job': 'Dev'}}

D['emp3'] = {'name': 'Max', 'job': 'Janitor'}

print(D)
# Prints {'emp1': {'name': 'Bob', 'job': 'Mgr'},
#         'emp2': {'name': 'Kim', 'job': 'Dev'},
#         'emp3': {'name': 'Max', 'job': 'Janitor'}}
# If the key is new, it is added to the dictionary with its value.

D = {'emp1': {'name': 'Bob', 'job': 'Mgr'},
     'emp2': {'name': 'Kim', 'job': 'Dev'},
     'emp3': {'name': 'Sam', 'job': 'Dev'}}

D['emp4'] = {'name': 'Max', 'job': 'Janitor'}

print(D)
# Prints {'emp1': {'name': 'Bob', 'job': 'Mgr'},
#         'emp2': {'name': 'Kim', 'job': 'Dev'},
#         'emp3': {'name': 'Sam', 'job': 'Dev'},
#         'emp4': {'name': 'Max', 'job': 'Janitor'}}
# Merge Two Nested Dictionaries
# Use the built-in update() method to merge the keys and values of one nested dictionary into another. 
# Note that this method blindly overwrites values of the same key if there’s a clash.

D1 = {'emp1': {'name': 'Bob', 'job': 'Mgr'},
      'emp2': {'name': 'Kim', 'job': 'Dev'}}

D2 = {'emp2': {'name': 'Sam', 'job': 'Dev'},
      'emp3': {'name': 'Max', 'job': 'Janitor'}}

D1.update(D2)

print(D1)
# Prints {'emp1': {'name': 'Bob', 'job': 'Mgr'},
#         'emp2': {'name': 'Sam', 'job': 'Dev'},
# #         'emp3': {'name': 'Max', 'job': 'Janitor'}}
# Here the ’emp2′ record is updated while ’emp3′ is added to the dictionary.

# Remove Nested Dictionary Items
# There are several ways to remove items from a nested dictionary.

# Remove an Item by Key
# If you know the key of the item you want, you can use pop() method. It removes the key and returns its value.

D = {'emp1': {'name': 'Bob', 'job': 'Mgr'},
     'emp2': {'name': 'Kim', 'job': 'Dev'},
     'emp3': {'name': 'Sam', 'job': 'Dev'}}

x = D.pop('emp3')

print(D)
# Prints {'emp1': {'name': 'Bob', 'job': 'Mgr'},
#         'emp2': {'name': 'Kim', 'job': 'Dev'}}

# get removed value
print(x)
# Prints {'name': 'Sam', 'job': 'Dev'}
# If you don’t need the removed value, use the del statement.

D = {'emp1': {'name': 'Bob', 'job': 'Mgr'},
     'emp2': {'name': 'Kim', 'job': 'Dev'},
     'emp3': {'name': 'Sam', 'job': 'Dev'}}

del D['emp3']

print(D)
# Prints {'emp1': {'name': 'Bob', 'job': 'Mgr'},
#         'emp2': {'name': 'Kim', 'job': 'Dev'}}
# Remove Last Inserted Item
# The popitem() method removes and returns the last inserted item as a tuple.

D = {'emp1': {'name': 'Bob', 'job': 'Mgr'},
     'emp2': {'name': 'Kim', 'job': 'Dev'},
     'emp3': {'name': 'Sam', 'job': 'Dev'}}

x = D.popitem()

print(D)
# Prints {'emp1': {'name': 'Bob', 'job': 'Mgr'},
#         'emp2': {'name': 'Kim', 'job': 'Dev'}}

# get removed pair
print(x)
# Prints ('emp3', {'name': 'Sam', 'job': 'Dev'})
# In versions before 3.7, popitem() would remove a random item.

# Iterate Through a Nested Dictionary
# You can iterate over all values in a nested dictionary using nested for loop.

D = {'emp1': {'name': 'Bob', 'job': 'Mgr'},
     'emp2': {'name': 'Kim', 'job': 'Dev'},
     'emp3': {'name': 'Sam', 'job': 'Dev'}}

for id, info in D.items():
    print("\nEmployee ID:", id)
    for key in info:
        print(key + ':', info[key])

# Prints Employee ID: emp1
#        name: Bob
#        job: Mgr

#        Employee ID: emp2
#        name: Kim
#        job: Dev

#        Employee ID: emp3
#        name: Sam
#        job: Dev























    
    
    
    
    
    
    
    
    
