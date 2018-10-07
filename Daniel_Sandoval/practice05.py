# Write a function area_of_circle(r) which returns the area of a circle of radius
# r only if the radius value is greater of 10.

import math


def area_of_circle(value_radio):
    value_pi = math.pi
    return "The area of a circle is: " + str(value_pi * math.pow(value_radio, 2))\
        if value_radio > 10 else "Radius is minor"


enter_radio = int(input("Enter the radius value of the circle: "))

print area_of_circle(enter_radio)