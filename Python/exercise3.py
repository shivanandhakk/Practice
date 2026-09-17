# Python Calculator
operator = input("Enter an operator (+, -, *, /): ")
num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))
if operator == '+':
    result = num1 + num2
    print(result)
elif operator == '-':
    result = num1 - num2
    print(result)
elif operator == '*':
    result = num1 * num2
    print(result)
elif operator == '/':
    result = num1 / num2
    print(result)
else:
    print(f"{operator} is not a valid operator.")

#Temperature Conversion Program
temp = float(input("Enter the temperature: "))
unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ")
if unit == 'C':
    fahrenheit = (temp * 9/5) + 32
    print(f"The temperature in Fahrenheit is: {fahrenheit}F")
elif unit == 'F':
    celsius = (temp - 32) * 5/9
    print(f"The temperature in Celsius is: {celsius}C")
else:
    print("Invalid unit. Please enter 'C' or 'F'.")