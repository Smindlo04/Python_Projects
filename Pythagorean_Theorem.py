# Import from math
import math

# Ask the user to input the lengths of the three sides of a triangle
value1=float(input("Please input the length of the longest side: "))
value2=float(input("Please input the length of the second side: "))
value3=float(input("Please input the length of the third side: "))

# Indication that is a right triangle or not
if round(value1==math.sqrt(value2**2+value3**2),2) :
 print("It's a right triangle")
else:
 print("It is not a right triangle")
