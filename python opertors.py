#### Python’s Arithmetic Operators #####


# + Addition 1 + 1 = 2
# - Subtraction 10 - 1 = 9
# * Multiplication 3 * 5 = 15
# / Division 10 / 5 = 2
# % Modulus (remainder after division) 11 % 5 = 1
# ** Exponent 3**2 = 9
# // Floor division 11 // 5 = 

# The first four items in the table are the same as you learned in elementary school. 
# The last three are a little more advanced so we’ll explain them here:
# » The modulus is the remainder after division. So, for example, 11 % 5 is 1 
# because if you divide 11 by 2 you get 5 remainder 1. That 1 is the modulus 
# (sometimes called the modulo).

# » The exponent is ** because you can’t type a small raised number in code. But 
# it just means “raised to the power of” in the sense that 3**2 is 32 or 3 squared, 
# which is 3*3 or 9. And of course 3**4 would be 3*3*3*3 or 81.
# » Floor division, indicated by //, is integer division in that anything after the 
# decimal point is truncated (ignored). The term truncated in this sense means 
# “cut off,” without any rounding. For example, in regular division 9/5 is 1.8. 
# But 9//5 is just 1 because the .8 is just chopped off, it doesn’t even round 
# up the 1 to a 2



# Python Comparison Operators #

# Operator Meaning

# < Less than
# <= Less than or equal to
# > Greater than
# >= Greater than or equal to
# == Equal to
# != Not equal to
# is Object identity
# is not Negated object identity


 
# examples how to use Arthemtic operators

a = 90 + 8
b = 9898 * 90
c = 78 - 56

print("the value of 90+8", 90+8)
print("the value of 9898*90",9898*90)
print("the value of 78-56",78-56)





# Python also offers three logical operators, also called Boolean operators that can 
# allow you assess multiple comparisons before making a final decision. Those 
# operators use the English word for, well, basically what they mean



""" Python Logical Operators
Operator Meaning """

# and  both are true
# or one or the other is true
# not is not true


# Python Bitwise Operators

# Bitwise operators are used to compare (binary) numbers:

# Operator	Name	Description
# & 	AND	Sets each bit to 1 if both bits are 1
# |	OR	Sets each bit to 1 if one of two bits is 1
#  ^	XOR	Sets each bit to 1 if only one of two bits is 1
# ~ 	NOT	Inverts all the bits
# <<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off
# >>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off


# Python Assignment Operators

# Assignment operators are used to assign values to variables:

# Operator	Example	Same As	Try it
# =	x = 5	x = 5	
# +=	x += 3	 x = x + 3	
# -=	x -= 3	 x = x - 3	
# *=	x *= 3	 x = x * 3	
# /=	x /= 3	 x = x / 3	
# %=	x %= 3	 x = x % 3	
# //=	x //= 3	 x = x // 3	
# **=	x **= 3  x = x ** 3	
# &=	x &= 3	 x = x & 3	
# |=	x |= 3	 x = x | 3	
# ^=	x ^= 3	 x = x ^ 3	
# >>=	x >>= 3	 x = x >> 3	
# <<=	x <<= 3	 x = x << 3	


# Summary

# operator	
# Description

# Syntax
# =

# Assign value of right side of expression to left side operand	x = y + z 
# +=

# Add and Assign: Add right side operand with left side operand and then assign to left operand	a += b   
# -=

# Subtract AND: Subtract right operand from left operand and then assign to left operand: True if both operands are equal	a -= b  
# *=

# Multiply AND: Multiply right operand with left operand and then assign to left operand	a *= b     
# /=

# Divide AND: Divide left operand with right operand and then assign to left operand	a /= b
# %=

# Modulus AND: Takes modulus using left and right operands and assign result to left operand	a %= b  
# //=

# Divide(floor) AND: Divide left operand with right operand and then assign the value(floor) to left operand	a //= b   
# **=

# Exponent AND: Calculate exponent(raise power) value using operands and assign value to left operand	a **= b     
# &=

# Performs Bitwise AND on operands and assign value to left operand	a &= b   
# |=

# Performs Bitwise OR on operands and assign value to left operand	a |= b    
# ^=

# Performs Bitwise xOR on operands and assign value to left operand	a ^= b    
# >>=

# Performs Bitwise right shift on operands and assign value to left operand	a >>= b     
# <<=

# Performs Bitwise left shift on operands and assign value to left operand	a <<= b 


# Now Let’s see each Assignment Operator one by one.

# 1) Assign: This operator is used to assign the value of the right side of
#  the expression to the left side operand.

# Syntax:

# x = y + z
# Example:


# Assigning values using 
# Assignment Operator
  
a = 3
b = 5
  
c = a + b
  
# Output
print(c)
# Output:

# 8
# 2) Add and Assign: This operator is used to add the right side 
# operand with the left side operand and then assigning the result to the left operand.

# Syntax: 

# x += y
# Example:


a = 3
b = 5
  
# a = a + b
a += b
  
# Output
print(a)
# Output:

# 8
# 3) Subtract and Assign: This operator is used to subtract the right 
# operand from the left operand and then assigning the result to the left operand.

# Syntax:

# x -= y
# Example –


a = 3
b = 5
  
# a = a - b
a -= b
  
# Output
print(a)
# Output:

# -2
#  4) Multiply and Assign: This operator is used to multiply 
#  the right operand with the left operand and then assigning the result to the left operand.

# Syntax:

# x *= y
# Example:


a = 3
b = 5
  
# a = a * b
a *= b
  
# Output
print(a)
# Output:

# 15
#  5) Divide and Assign: This operator is used to divide the left operand 
#  with the right operand and then assigning the result to the left operand.

# Syntax: 

# x /= y
# Example:


a = 3
b = 5
  
# a = a / b
a /= b
  
# Output
print(a)
# Output:

# 0.6
#  6) Modulus and Assign: This operator is used to take the modulus 
#  using the left and the right operands and then assigning the result to the left operand.

# Syntax:

# x %= y
# Example:


a = 3
b = 5
  
# a = a % b
a %= b
  
# Output
print(a)
# Output:

# 3
# 7) Divide (floor) and Assign: This operator is used to divide the 
# left operand with the right operand and then assigning the result(floor) to the left operand.

# Syntax:

# x //= y
# Example:


a = 3
b = 5
  
# a = a // b
a //= b
  
# Output
print(a)
# Output:

# 0
#  8) Exponent and Assign: This operator is used to calculate the 
#  exponent(raise power) value using operands and then assigning the result to the left operand.

# Syntax:

# x **= y
# Example:


a = 3
b = 5
  
# a = a ** b
a **= b
  
# Output
print(a)
# Output:

# 243
# 9) Bitwise AND and Assign: This operator is used to perform 
# Bitwise AND on both operands and then assigning the result to the left operand.

# Syntax:

# x &= y
# Example:


a = 3
b = 5
  
# a = a & b
a &= b
  
# Output
print(a)
# Output:

# 1
# 10) Bitwise OR and Assign: This operator is used to perform Bitwise 
# OR on the operands and then assigning result to the left operand.

# Syntax:

# x |= y
# Example:


a = 3
b = 5
  
# a = a | b
a |= b
  
# Output
print(a)
# Output:

# 7
# 11) Bitwise XOR and Assign: This operator is used to perform Bitwise 
# XOR on the operands and then assigning result to the left operand.


# Syntax:

# x ^= y
# Example:


a = 3
b = 5
  
# a = a ^ b
a ^= b
  
# Output
print(a)

# 12) Bitwise Right Shift and Assign: This operator is 
# used to perform Bitwise right shift on the operands and then assigning result to the left operand.

# Syntax:

# x >>= y
# Example:


a = 3
b = 5
  
# a = a >> b
a >>= b
  
# Output
print(a)
# Output:

0
# 13) Bitwise Left Shift and Assign: This operator is used 
# to perform Bitwise left shift on the operands and then assigning result to the left operand.

# Syntax:

# x <<= y
# Example:


a = 3
b = 5
  
# a = a << b
a <<= b
  
# Output
print(a)




# Underscores in Numbers

# When you’re writing long numbers, you can group digits using underscores 
# to make large numbers more readable

number = 23_4_3435_90
print(number)
# python ignores underscore when reading digits
