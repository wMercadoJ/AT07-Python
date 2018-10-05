number = int(input("into the number"))


def odd_ever(number_test):
    return "The number is even" if number_test % 2 == 0 else "The number is odd"


print odd_ever(number)
