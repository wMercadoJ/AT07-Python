import math

rad = int(input("insert radio:"))


def area_circle(radio):
    if radio > 10:
        print(math.pi * (radio ** 2))
    else:
        print("radio minor a 10")


area_circle(rad)
