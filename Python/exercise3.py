import math
#Circumference of a circle
radius =float(input("Enter the Radius of a circle:"))
circumference = 2 * math.pi * radius
print(f"The circumference of a Circle is: {round(circumference, 2)}")

#Area of a circle
radius = float(input("Enter the Radius of a circle:"))
area = math.pi * radius ** 2
print(f"The Area of a Circle is: {round(area, 2)}")

#Hypotenuse of a right triangle
base = float(input("Enter the base of a right triangle:"))
height = float(input("Enter the height of a right triangle:"))
hypotenuse = math.sqrt(base ** 2 + height ** 2)
print(f"Hypotenuse of a right triangle: {round(hypotenuse, 2)}")