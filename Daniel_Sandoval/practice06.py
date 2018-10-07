# Write a function sum_to(n) that returns the sum of all integer numbers up to and
# including only until any value lower than 35. So sum_to(10)wouldbe1+2+3...+10
# which would return the value 55, but if n=40 only until sum to 35 need to be returned.


def sum_to(number):
    add_digits = 0
    for ini in range(1, number + 1):
        add_digits += ini
        if ini == 35 and number >= 35:
            print add_digits
            break
    print add_digits


number = int(input("Insert a number integer: "))

sum_to(number)