# Write a function area_of_circle(r) which returns the area of a circle of radius r only if the radius value is greater of 10.
import math

def area_of_circle(radio):
    return (math.pi * (radio ** 2)) if (radio > 10) else "The radius of the circle must be greater than 10"

number = int(input("Enter the radius of the circle: "))
print("The area of the radio circle "+str(number)+ " is: ", area_of_circle(number))
