import math

# Write a function area_of_circle(r) which returns the area of a circle of radius r only if the radius value is
# greater of 10


def area_of_circle(r):
    area = math.pi * r ** 2
    if area > 10:
        print (area, "mayor a 10")
        return area
    else:
        print ("minor a  10")


if __name__ == '__main__':
    print "Input radio"
    r = float(raw_input())
    area_of_circle(r)

# Write a function sum_to(n) that returns the sum of all integer numbers up to and including only until any value
# lower than 35.


def sum_to_n(number):
    maxim = 35
    res = 0.0
    if number < 35.0:
        maxim = int(number)
    for i in range(1, maxim + 1):
        res = res + float(i)
    print "Result: ", res


if __name__ == '__main__':
    print "INGRESS Number:"
    a = int(raw_input())
    sum_to_n(a)
