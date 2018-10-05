# According a list of values between a Min and Max range,
# identify if the number is prime or not.


def number_is_cousin(num):
    for ini in num:
        accountant = 0
        for j in range(1, ini + 1):
            if ini % j == 0:
                accountant = accountant + 1
        if accountant == 2:
            print "The number ", ini, " is cousin..."
        else:
            print "The number ", ini, " is not cousin..."


number_1 = int(input("Insert the first positive integer value greater than the zero: "))
number_2 = int(input("Insert the second positive integer value greater than the first value: "))
num = range(number_1, number_2)

print number_is_cousin(num)