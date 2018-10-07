# According a list of values between a Min and Max range, identify if the number is prime or not.
def range_prime(num_ini, num_max):
    if num_ini > 0 and num_max > 0:
        for number_auxiliary in range(num_ini, num_max + 1):
            cont = 0
            for i in range(2, number_auxiliary):
                if number_auxiliary % i == 0: cont += 1
            print ("The number " + str(number_auxiliary) + " not is prime.") if (cont > 0) else (
                        "The number " + str(number_auxiliary) + " is prime.")
    else:
        print (
            "The value of the minimum range must be greater than the maximum range and the values must be positive integers greater than 0.")


num_ini = int(input("Enter the minimum range: "))
num_max = int(input("Enter the maximun range: "))
range_prime(num_ini, num_max)
