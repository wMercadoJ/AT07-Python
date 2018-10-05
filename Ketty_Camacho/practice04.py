def identify_prime(number_min, number_max):
    cont = 0
    for i in range(number_min, number_max + 1):
        for x in range(1, i+1):
            if i % x == 0:
                cont = cont + 1
        if cont == 2:
            print("prime  " + str(i))
        else:
            print("not prime  " + str(i))
        cont = 0


identify_prime(1, 20)
