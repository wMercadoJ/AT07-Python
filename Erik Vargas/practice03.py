number = int(input("insert number:"))


def number_even_odd(num):
    return "even" if (number % 2 == 0) else "odd"


print(number_even_odd(number))
