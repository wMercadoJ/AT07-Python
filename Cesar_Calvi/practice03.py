# Exercise to validate if it is even or odd
if __name__ == '__main__':
    print "Enter number to see if it is even or not"
    var = float(raw_input())
    if var % 2 == 0:
        print("number pair")
    else:
        print ("number odd")


# Exercise to validate if it is a cousin or not


def is_prime(lst):
    for i in lst:
        n = 0
        for j in range(1, i + 1):
            if i % j == 0:
                n = n + 1
        if n == 2:
            print "Number ", i, " is prim..."


if __name__ == '__main__':
    print "Enter number MIN Y MAX: "
    minNum = int(raw_input())
    maxNum = int(raw_input())
    lst = range(minNum, maxNum + 1)
    print lst
    is_prime(lst)
