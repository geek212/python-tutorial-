# """ This function allows user to take input as a string """

# a = input("Enter your name  ")
# print(a)

# # Python input() function is used to take user input. By default,
# #  it returns the user input in form of a string

# color = input("what is the color of rose is ")
# print (color)

# user_name = input("log in this id")
# print(user_name)

# fine = input("how are you ashwin")
# print(fine)

# your = input("hello hi how are you")
# print(your)

# # i just radomly used the input function for pratice purpose

 

# n = int (input("How many roses in the garden: ?"))
# print(n)

# #  its is not possible when input defines string even with any data type with both the examples
 
# h =float(input("what are the single price of rose is ?"))
# print(h)

# # Example 1: Taking the Name and Age of the user as input and printing it

# name = input(" what is your name")
# age = input("what is your age")
# print(name , age)

# # Example 2: Taking two integers from users and adding them.

# num435 = int(input(" Please enter your number :  "))
# num56 = int(input("please enter your second number : "))

# sum_of_both_number = num435 + num56
# print("the sum of two numbers given is " , num435 + num56)

# # Their is one more exmaple for The input() function converts all
# #  the user input to a string even if that's the number.

# age = input("Enter your age")
# print (type(age))

# "What is the Python Input function? "

# # We have already seen the print function in Python, which sends data to the console 
# # Python Input function does the reverse of it. In other words, it takes user data
# # from the console so that the program can take action based on that input
# # The input function indicates the user to enter the data on the console.
# # Moreover, the program executes further only when the user has entered the data.
# # This data can then be stored in a variable and can use it in the program wherever
# # we need it.

# "What happens when you pass multiple arguments to the input() "
# "function? Will it show everything like print() function? "

# # input() -> multiple arguments #

# # num = input("Enter a number", "greater than 0 and less than 100")
# # print(num) # error will be shown

# # Why is it? The input() function takes at most one argument, but we passed two arguments to the 
# # input function. As a result, we got an error. Remember python user input() function takes only one 
# # argument. In other words, if we don't pass anything, then the input function 
# # won't show any message to the user, as seen in the first section of the tutorial.###



# # What is the Return Type of Python Input function?
# # We have mentioned that the python user input takes the information as a string type.
# # Let's check by an experiment.

# # getting input from the user
# # number = input("Enter a number:- ")
# # result = number + 2
# # print(result) # error will be shown


# # Key Takeaways #

# # input() function takes the data from the console in the form of string.
# # Moreover, we can pass a message to the input() function that will appear to the user 
# # before giving the data input. E.g. input("Enter a number:- ")
# # If we pass multiple arguments to the input() function, then we will get the error.
# # input() function returns the data in the string (str) format. Moreover, we can use the typecasting 
# # for type conversion. E.g. number = int(input("Enter a number:- "))
# # Additionally, converting one type of data into other types of data is known as typecasting.
# # We can use the functions int, str, and float for the typecasting.


ui = input("what is your name  ")
uii = input("what is your age  ")
print(ui,uii)


yu = input("hello    ")
yuu = input("how are you  ")
print(yu,yuu)


uyuy = input("how are you  ") # typcasting with input
uyuy = int(uyuy)
print(uyuy)
print(type(uyuy))


wer = input(78)   # typcasting with input 
wer = str(wer)
print(wer)
print(type(wer))