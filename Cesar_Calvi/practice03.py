# Exercise to validate if it is even or odd
if __name__ == '__main__':
    print "Enter number to see if it is even or not"
    var = float(raw_input())
    if var % 2 == 0:
        print("number pair")
    else:
        print ("number odd")


# Exercise to validate if it is a cousin or not


def is_prime(list_numbers):
    for index_i in list_numbers:
        n = 0
        for index_j in range(1, index_i + 1):
            if index_i % index_j == 0:
                n = n + 1
        if n == 2:

            print "Number ", index_i, " is prim..."


if __name__ == '__main__':
    print "Enter number MIN Y MAX: "
    number_min = int(raw_input())
    number_max = int(raw_input())
    number_list = range(number_min, number_max + 1)
    print number_list
    is_prime(number_list)
