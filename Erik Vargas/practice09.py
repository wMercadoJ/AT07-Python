number = int(input("insert number:"))


def sum_int(num):
    plus = 0
    for i in range(1, num + 1):
        if i <= 35:
            plus += i
    print plus


sum_int(number)
