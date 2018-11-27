number1 = int(input("into the first range"))
number2 = int(input("into the second range"))


def number_prime(num1, num2):
    if num1 > 0 & num2 > 0:
        num1 = min(num1, num2)
        num2 = max(num1, num2)
    while num1 <= num2:
        print prime(num1)
        num1 += 1


def prime(number_prime):
    status = True
    for i in range(2, number_prime / 2 + 1):
        if (number_prime % i) == 0: status = False

    return "the number :" + str(number_prime) + " is prime" if status else "the number :" + str(
        number_prime) + " not is prime"


number_prime(number1, number2)
