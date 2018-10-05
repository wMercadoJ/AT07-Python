import math

ratio = int(input("into the ratio"))


def area_of_circle(ratio):
    area = 2 * math.pow(math.pi, 2)
    return area if ratio > 10 else ""


print area_of_circle(ratio)
