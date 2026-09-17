# Arithmeic Operators
# Augmented arithmetic operators are used to perform arithmetic operations on variables and update their values in a single step.
a = 237.56
a += 10 # equivalent to a = a + 10
a -= 10
a *= 10
a /= 10 #Division always returns a float value, even if the result is a whole number.
a **= 3 #Exponentiation operator raises the value of a to the power of 3.
a //= 10 #Floor Division gives the whole number part of the division result, discarding any decimal portion.
a %= 3 #Modulus operator returns the remainder of the division operation.
print(a)

#Built-in math functions
x = 3.14
y = -4
z = 5
round = round(x) #rounds the value of x to the nearest integer.
absolute = abs(y) #returns the absolute value of y.
power = pow(z, 2) #raises z to the power of 2.
maximum= max(x, y, z) #returns the maximum value among x, y, and z.
minimum= min(x, y, z) #returns the minimum value among x, y, and z.
print(round)
print(absolute)
print(power)
print(maximum)
print(minimum)

#the math module provides access to mathematical functions and constants.
import math 
print(math.pi)
print(math.e)
print(math.sqrt(16)) 
print(math.ceil(3.14)) #returns the smallest integer greater than or equal to 3.14.
print(math.floor(3.54)) #returns the largest integer less than or equal to 3.54.
print(math.factorial(5)) #returns the factorial of 5, which is 5! = 5 * 4 * 3 * 2 * 1 = 120.
