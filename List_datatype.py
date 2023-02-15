# # Defining and Using Lists

# # The simplest data collection in Python is a list.

# '''
# A list is any list of data items, separated by commas, inside
# square ([]) brackets. Typically, you assign a name to the list using an = sign, just as
# you would with variables. If the list contains numbers, then don’t use quotation
# marks around them.

# '''

# # for Example if the list contains numbers, then don’t use quotation marks around them. 
# # scores = [88, 92, 78, 90, 98, 84]

# # If the list contains strings then, as always, those strings should be enclosed in
# # single or double quotation marks

# # E.g :students = ["Harry", "Rahul", "Anita", "Ashish"]

# # if you print this variable the ouput will be same

# # "Harry", "Rahul", "Anita", "Ashish"

# ''' 
# Referencing list items by position
# Each item in a list has a position number, starting with zero, even though you
# don’t see any numbers. You can refer to any item in the list by its number using
# the name for the list followed by a number in square brackets. In other words, use
# this syntax:
# list_name[x]

# '''
# # Remember, the first item is always number zero, not one.

# students_name = ["Harry", "jackie", "Ken", "Rohan"]
# print(students_name[0])
# # output will be Harry

# #  it will be like [Harry (0)] [jackie (1)] [Ken(2)] [Rohan(3)]

# # In this example we will use numbers 

# scores = [ 80 , 56 , 43 , 223 ]
# print (scores[3])  # when i entered 4 in the bracket it shows error for output

# # If you try to access a list item that doesn’t exist, you get an “index out of range” error


# # 1. Looping through a list

# scores = [ "80" , "56" , "43" , "223" ]
# for score in scores :
#    print (score)       # score & scores 

# fruits = ["Apple", "Mango", "Pineapple", "Jackfruit"]
# for fruit in fruits :
#     print(fruit)    # fruit & fruits 

# '''Here, the for loop has printed each of the list items. In other words, the loop has
# called the print() function four times, each time printing the current item in the list – i.e.
# the name of a fruit or Score. 
# '''
# # IMP
# ''' Lists are changeable objects
# It's important to know that lists are changeable — you can add, remove,
# or change list elements after the list is created.'''

# # 2. List Comprehension

# ''' List comprehension is similar to the for loop; however, it allows us to create a 
# list and iterate through it in a single line. Due to its utter simplicity,
# this method is considered one of the most robust ways of iterating over Python lists.

# [You’ll notice that we’re using what looks like another for loop: for fruit in fruits.
# The key here 
# is that the command and the for..in structure are
# enclosed with the print() command in square brackets; that’s what makes it a list comprehension.]

# '''
# # Example 1
# fruits = ["Watermelon", "Grapes", "jackfruit", "Mango"]
# [print(fruit + " " +  "Juice") for fruit in fruits]
# # IMP use bracets for print with (for) / (in) 
# # i used (" ") for spaces between fruit and juice for output

# # Example 2
# Cars = ["BMW", "Ferrai", "Land Rover", "Mercedes"]
# [print(Car + " "+ "Sportscar" ) for Car in Cars]

# # Example 3
# Motorcycles_Brands = ["Heromotocorp" , "KTM" , "Royal_enfield" , "Bajaj" ]
# [print(Motorcycles_Brand + "  " + "SuperBikes" + " " + "of india") for Motorcycles_Brand in Motorcycles_Brands]

# # Example 4
# # GoalByargitinas ["34" , "43" , "45" , "345" , "23"]  # this output shows error
# # [print(GoalByargitina + "Goal" ) for GoalByargitina in GoalByargitinas]

# # Vegetables = ["Brinjal" , "Cabbage" , "okra", "Tomato"]
# # [print(Vegetable + " " + " in_Delhi") for Vegetable in Vegetables]

# # 3. A for Loop with range()

# ''' Another method for looping through a Python list is the range() function along with a for loop. 
# range() generates a sequence of integers from the provided starting and stopping indexes. 
# An index refers to the position of elements in a list. 
# The first item has an index of 0, the second list item is 1, and so on.) 
# The syntax of the range function is as follows:

# range(start, stop, step)

# The start and step arguments are optional; only the stop argument is required.
# The step determines if you skip list items; this is set as 1 by default, meaning no items are skipped.
# If you only specify one parameter (i.e. the stop index),
# the function constructs a range object containing all elements from 0 to stop-1.

# '''

# fruits = ["Apple", "Mango", "Banana", "Peach"]
 
# # Constructs range object containing elements from 0 to 3
# for i in range(len(fruits)):
#     print("The list at index", i, "contains g", fruits[i])

# Vegetables = ["Brinjal" , "Cabbage" , "okra", "Tomato"]

# # Constructs range object containing elements from 0 to 3
# for i in range(len(Vegetables)):   
#     print("The list at index ", i , "contains a", Vegetables[i])



# Shows = ["Bigboss" , "KBC", "Doremon", "Pokemon", "Beyblade"]

# # Constructs range object containing elements from 0 to 4
# for i in range(len(Shows)):
#     print("the list of index", i , "Contains a", Shows[i])


# Cricketrs = ["Sachin", "Dravid", "Virat", "Dhoni", "Rohit","Jadeja"]
# # Constructs range object containing elements from 0 to 5
# for  i  in range(len(Cricketrs)):
#     print("the lists of index", i , "Contains in a World Cup", Cricketrs[i])


# # Methods for Working with Lists

# # Method What it Does  ?

# # append() Adds an item to the end of the list.

# # clear() Removes all items from the list, leaving it empty.

# # copy() Makes a copy of a list.

# # count() Counts how many times an element appears in a list.

# # extend() Appends the items from one list to the end of another list.

# # index() Returns the index number (position) of an element within a list.

# # insert() Inserts an item into the list at a specific position.

# # pop() Removes an element from the list, and provides a copy of that item that 
# # you can store in a variable.

# # remove() Removes one item from the list.

# # reverse() Reverses the order of items in the list.

# # sort() Sorts the list in ascending order. Put reverse=True inside the 
# # parentheses to sort in descending order.


# # Seeing whether a list contains an item

# students_name = [ "Ashwin", "Rahul", "Jackei", "Manoj"]

# # is Rahul in the lists
# has_Rahul = "Rahul" in students_name # in operator used for true or false
# print(has_Rahul)

# # is Rock on the lists
# has_Rock = "Rock" in students_name # in operator used for true or false
# print(has_Rock)

# # Getting the length of a list which i previously done above so this is Explantion

# students = ["Danny", "Harry", "Kunal", "Santosh"]
# print(len(students))
# # To determine how many items are in a list, use the len() function (short for 
# # length). Put the name of the list inside the parentheses.


# # Adding an item to the end of a list

# # When you want your code to add a new item to the end of a list, use the .append()
# # method with the value you want to add inside the parentheses. You can use either 
# # a variable name or a literal value inside the quotation marks.


# Cerate a variables with list of students_name
students_name = ["Anita", "Kunalk", "Neelam", "Dainel"]

# Add usha on the list
students_name.append("usha")

# Add new student name on the list again with "usha"
new_student = "Rishi"
students_name.append("Rishi")

# now print
print(students_name)

# Cerate variables with list of numbers for units sold
Quantity = [ 56, 34 , 3456, 234, 45, 45]
Quantity.append(78)
Quantity.append(67)
Quantity.append(76)

print(Quantity)



# Inserting an item into a list

# Although the append() method allows you to add an item to the end of a list, the 
# insert() method allows you to add an item to the list in any position. The syntax 
# listname.insert(position,item)



# Replace listname with the name of the list, position with the position at which you 
# want to insert the item (for example, 0 to make it the first item, 1 to make it the 
# second item, and so forth). Replace item with the value, or the name of a variable 
# that contains the value, that you want to put into the list.


# Cerate a list of names
lsit_name = ["jacky", "harry", "Henry", "jhonny","king"]

students_name = "lailla"
lsit_name.insert(0,students_name)

print(lsit_name)

# Cerate the list of fruits 
Shopping = ["Mango", "grapes", "Banana", "Guva", "Oranges", "Jackfruit"]

fruit_name1 = "Chickoo"
Shopping.insert(2, fruit_name1)

fruit_name2 = "Dragonfruit"
Shopping.insert(0,fruit_name2)

fruit_name3 = "Cherry"
Shopping.insert(1,fruit_name3)

print(Shopping)


# Changing an item in a list

# You can change an item in a list using the = assignment operator just like you do 
# with variables. Just make sure you include the index number in square brackets of 
# the item you want to change.

# Cerate a list of names 
students_name = ["tina", "Jhonny", "Bravo", "Henry", "jocky"]
students_name [0] = "Harold"
print(students_name)

# cerate lists of numbers of float
number = [56.4 ,45.4, 45.3, 4.4, 535.3, 45.3]
number[2] = 23.4
print(number)



# Combining lists

# If you have two lists that you want to combine into a single list, use the extend()
# function with the syntax:
# original_list.extend(additional_items_list)

''' In your code, replace original_list with the name of the list to which you’ll be 
adding new list items. Replace additional_items_list with the name of the list that 
contains the items you want to add to the first list.'''

# Cerate a lists of variable name with list1 and list2

list1 = ["harry", "frank", "Gary", "Mark", "joker"]
list2 = ["Batman", "Superman", "Monkeyboy", "frenchie"]

#  Add list1 to list2 names
list1.extend(list2)

# print list1
print(list1)

# Cerate a lists of numbers  with variable list3 and list4

list3 = [56, 566 , 45, 4, 53, 11]
list4 = [34, 421, 12, 123, 23]

# Add list4 to list3
list4.extend(list3)

# print list4
print(list4)


# Removing list items

# Python offers a remove() method so you can remove any value from the list. 
# If the item is in the list multiple times, only the first occurrence is removed. For 
# example, the following code shows a list of letters with the letter C repeated a few 
# times. Then the code uses letters.remove("C") to remove the letter C from the list:

#Create a list of strings.
letters = ["A", "B", "C", "D", "C", "E", "C"]
# Remove "C" from the list.
letters.remove("C")
#Show me the new list.
print(letters)
# When you actually execute this code and then print the list, you’ll see that only the 
# first letter C has been removed:


# Cerate a lists of string .
letters2 = ["A", "B", "B", "C"]
# Remove "A" from list
letters2.remove("A")
print(letters2)


 Removeing list items useing [Pop()]

# If you want to remove an item based on its position in the list, use pop() with an 
# index number rather than remove() with a value. If you want to remove the last 
# item from the list, use pop() without an index number. For example, the following code 
# creates a list, one line removes the first item (0), and another removes 
# the last item (pop() with nothing in the parentheses). Printing the list shows 
# those two items have been removed:

letters3 = ["A", "B", "B", "C", "D"]
letters3.pop(0)
letters3.pop(2)
print(letters3)

letters4 = ["A", "B", "C", "sd", "D"]
letters4.pop(3)
print(letters4)

# When you pop() an item off the list, you can store a copy of that value in some 
# variable.

# Cerate list of string

letter0 = ["a", "A", "b", "B", "C", "c", "D", "d"]

#  Make a copy of frist list item then remove them
frist_letter_removed = letter0.pop(0)
 

# Make a copy of last list item then remove it
last_letter_removed = letter0.pop()

# Show the result
print(letter0)

# Show what is been removed
print(frist_letter_removed  +"  " + "and " + last_letter_removed + "  " + "were removed from the list")


# Removeing list item using del(delete)

# Python also offers a del (short for delete) command that deletes any item from 
# a list based on its index number (position). But again, you have to remember 
# that the first item is zero. So, let’s say you run the following code to delete item 
# number 2 from the list

# Cerate a list of strings
letters = ["A", "a", "B", "C", "D"]

# Remove item 1
del letters[1]

# Show the result
print(letters)

# Cerate a list of Second strings

letters5 = ["A", "wr", "GFS", "B", "C"]

# Remove item 1 and 2 using  del

del letters5[2]
del letters5[0]
 

# Show the results 
print(letters5)


# Clearing out a list items

# If you want to delete the contents of a list but not the list itself, use .clear(). The 
# list still exists; however, it contains no items ,In other words, it’s an empty list
# The following code shows how you could test this.

# Cerate a list of strings

letters = ["a", "sfsf", "sdf", "A"]

# Clear the list of all entries
letters.clear()

# Show the result
print(letters)  # output is [] its been cleared the list wow 



# Cerate a list of numbers
numbers = [43.34, 34 , 342 , 24]

# Clear the list of all entries 
numbers.clear()

# Show the result # wowww i luv it again the output is []
print(numbers)


# Counting how many times an item appears in a list

# You can use the Python count() method to count how many times an item appears 
# in a list. As with other list methods, the syntax is simple:
# listname.count(x)

# Replace listname with the name of your list, and x with the value you’re looking 
# for (or the name of a variable that contains that value).



# Cerate a list of string 
students_name = ["Ashwin", "Sabin", "Ashwin", "nair"]

# Count a student names
students_name  = students_name.count("Ashwin") # use = with a given variable or it will not show the count

# Show the result
print(students_name)


 


