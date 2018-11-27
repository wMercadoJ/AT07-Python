def sum_total(number):
    sum_result = 0
    for i in range(number + 1):
        if (i <= 35):
            sum_result += i
        else:
            break
    print(sum_result)


sum_total(40)
