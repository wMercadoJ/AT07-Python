num1 = int(input("insert number min:"))
num2 = int(input("insert number max:"))


def range_primes(minimum, maximo):
    if minimum > 0 and maximo > 0:
        while minimum <= maximo:
            aux = 0
            for i in range(1, minimum):
                if minimum % i == 0:
                    aux += 1
            print("is prime:", minimum) if aux < 2 else ("not is prime:", minimum)
            minimum += 1


range_primes(num1, num2)
