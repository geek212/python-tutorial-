#   Sets

# Python also offers sets as a means of organizing data. The difference between a 
# set and a list is that the items in set have no specific order. Even though you may 
# define the set with the items in a certain order, none of the items get index numbers to 
# identify their positions.


# To define a set, use curly braces where you would have used square brackets for 
# a list and parentheses for a tuple. For example, here’s a set with some numbers 
# in it:



# sample_set = {1.98, 98.9, 74.95, 2.5, 1, 16.3}


# Sets are similar to lists and tuples in a few ways. You can use len() to determine 
# how many items are in a set. Use in to determine whether an item is in a set. But 
# you cannot get an item in a set based on its index number. Nor can you change an 
# item that is already in the set.




# Cerate set of names

name = {"raj,rahul,heena"}    # i have to use str " " in set { } to identify the type                               #  without
print(type(name))

# cerate set of numbers 

number = {45,23,2.34,123,445} # for number set " " is not required
print(type(number))


# Sets are similar to tuples , u cannot change the order of set


#  You can’t change the order of items in a set either. So you cannot use .sort() to 
# sort the set or .reverse() to reverse its order.

#  set has no defined order 





# Methods of sets that can use

'''
Sets can add single item by using to set 

 following syntax  :   sample_number.add(34)


We can add multiple items in the sets , But the items you’re 
adding should be defined as a list in square brackets

 following syntax   :   sample_number.update( [45, 34, 4.3 ] )


We can copy in set as its not defined order its items may not be in the same order as the original set

 following syntax    : sample_number.copy()

'''
# Lists , tuples , and dictionaries are three  of the most commonly-used Python data structures. Sets 
# don’t seem to get as much play as the other three, but it’s good to know about them. 
 





# Cerate a set named set_sample


set_sample = {34, 34.45, 67, 445, 5, 589.5, 67}

# print the set_sample
print(set_sample)                          


# print len() in set_sample
print(len(set_sample))                 


# Use in to determine 67 if set contains value
print(67 in set_sample)                                  


# Use add() to determine in set
set_sample.add(567)

# Use update() to add list in set
set_sample.update([5,6,7,8,9])


print("\nset_sample  .add() and update()")
print(set_sample)


