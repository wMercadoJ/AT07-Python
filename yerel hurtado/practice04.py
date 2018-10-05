def number_prime(number):
    divisor = 1
    count = 0
    while divisor <= number:
        if number % divisor == 0:
            count = count + 1
        divisor = divisor + 1
    if count == 2:
        return True


number_prime(0)


def array_prime(min_value, max_value):
    listPrimes = []
    for number in range(min_value, max_value):
        if number_prime(number):
            listPrimes.append(number)
    print(listPrimes)


array_prime(2, 9)
