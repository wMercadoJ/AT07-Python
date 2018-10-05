import math


# Practice 05 area of circle
# author Ana Mamani
# since 10/05/2018

def area_of_circle(radio):
    if (radio >= 10):
        area = math.pi * (radio ** 2)
        print area


area_of_circle(11)
