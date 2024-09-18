import math

# 1. Circumference of a circle
# radius = float(input('Enter the radius of a circle: '))
#
# circumference = 2 * math.pi * radius
#
# print(f"The circumference is : {round(circumference,2)}cm")

# 2. Area :
# radius = float(input('Enter the radius of a circle: '))
#
# area = math.pi * pow(radius,2)
# print(f"The area of the circle is : {round(area,2)}")

# Hypotenuse of Right angle triangle

a = float(input("Side A = "))
b = float(input("Side B = "))

c = math.sqrt(pow(a,2) + pow(b,2))
print(f"Hypotenuse = {c}")