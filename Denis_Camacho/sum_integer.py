number = int(input("into the number"))


def sum_to(number):
    number = number if number < 35 else 35
    sum = 0
    for i in range(0, number + 1):
        sum += i
    return sum


print(sum_to(number))
