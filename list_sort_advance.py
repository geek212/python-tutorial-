# This is a sort () advance method 

# Dates are a little trickier because you can’t just type them in as strings, like 
# "12/31/2020". They have to be the date data type to sort correctly. This means 
# using the datetime module and the date() method to define each date. You can 
# add the dates to the list as you would any other list. For example, in the following 
# line, the code creates a list of four dates, and the code is perfectly fine.
# dates = [dt.date(2020,12,31), dt.date(2019,1,31), dt.date(2018,2,28), 
# dt.date(2020,1,1)]
# The computer certainly won’t mind if you create the list this way. But if you want 
# to make the code more readable to yourself or other developers, you may want 
# to create and append each date, one at a time, so just so it’s a little easier to see 
# what’s going on and so you don’t have to deal with so many commas in one line 
# of code. Figure 3-10 shows an example where we created an empty list named 
# datelist:
# datelist = []
# Then we appended one date at a time to the list using the dt.date(year,month,day)
# syntax


# need this modules for date
import datetime as dt

# Cerate a list of dates , empty starters
datelist = []

# Append one code at a time so it can easier to read
datelist.append(dt.date(2023,12,13))
datelist.append(dt.date(2021,1,13))
datelist.append(dt.date(2022,1,10))

# Sort the dates earliest to latest
datelist.sort()
for date in datelist :
    print(f"{date:%d%m%y}") 


# Not the easiest list to read. So, rather than print the whole list with one print()
# statement, we looped through each date in the list,
# and printed each one formatted with the f-string %m/%d/%Y.




# If you want to sort items in reverse order, put reverse=True inside the sort() 
# parentheses (and don’t forget to make the first letter uppercase)

# Example 2 : need this modules for date

import datetime as dt

# Cerate a list of strings
names = ["Ashwin", "Sabin", "hshwin", "nair"]

# Cerate a list of int
numbers = [1,3,4,5,2,6,9,7,8,10]


# Cerate list of appends for empty sraters cozzz code is long 
datelist = []

datelist.append(dt.date(2023,2,22))
datelist.append(dt.date(2022,12,21))
datelist.append(dt.date(2012,12,21))
datelist.append(dt.date(1999,12,12))


# Sort the string in reverse order (Z to A)
names.sort(reverse=True)
print(names)


# Sort the int in reverse order from(longest to smallest)
numbers.sort(reverse=True)
print(numbers)


# Sort the dates in reverse order from (latest to earliest)
datelist.sort(reverse=True)
for date in datelist :
    print(f"{date:%y/%d/%m}") 

