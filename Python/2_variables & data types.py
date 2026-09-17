# This is a simple program
print("Hello Python!")

#variables and f-strings
#Variables are used to store data values. 
name = "Maria"
language = "Python"
print("My name is", name)
print(name, "is learning", language)
print(name, "wants to become", language, "expert")

#f-strings - formatted string literals is a way to embed expressions inside string literals, using curly braces {}.
first_name = "Annie"
email = "annie@gmail.com"
print(first_name)
print(f"Hello {first_name}!")
print(f"Your email is {email}.")

#Integers - whole numbers
age = 25
print(f"Your are {age} years old.")
#float - decimal numbers
gpa = 8.7
print(f"Your GPA is {gpa}.")
#Boolean - True or False
is_student = False
print(f"Are you a student?: {is_student}")
if is_student:
    print("You are a student.")
else:
    print("You are not a student.")

#Type Casting -  the process of converting a variable from one data type to another
name="Annie"
age=25
gpa=8.7
is_student=False
print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

gpa = int(gpa)
print(type(gpa)) #converts float to int
age = str(age)
print(type(age)) #converts int to str
age = float(age) #converts int to float
print(type(age))
name=bool(name) #converts str to bool
print(name) #True occurs when the string is not empty and Flse occurs when the string is empty.

# input() = A function that allows user to enter data.
#           By default, the data type of the input is string.
Qualification=input("What is your qualification?: ")
print(f"Your qualification is {Qualification}.")
age = int(input("What is your age ?:"))
age = age+1
print(f"You are going to be {age} next year.")
# TypeError: can only concatenate str (not "int") to str
# this error occurs when you try to concatenate a string with an integer. 
# To fix this, you can convert the integer to a string using the str() function before concatenation.
