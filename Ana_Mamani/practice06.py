# Practice 06 sum of all integer numbers up to and including only until any value lower than 35
# author Ana Mamani
# since 10/05/2018

def sum_to(number):
    sum = 0
    for val in range(number + 1):
        if (val <= 35):
            sum += val
        else:
            break
    print sum


sum_to(10)
