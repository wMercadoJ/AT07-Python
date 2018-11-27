import math


def area_of_circle(radius):
    if radius > 10:
        area = math.pi * (radius ** 2)
        print(area)


area_of_circle(11)