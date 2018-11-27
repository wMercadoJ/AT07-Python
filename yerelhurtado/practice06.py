def sum_to(number):
    content = 1
    result = 0
    while content <= number:
        result += content
        content = content + 1
        if content > 35:
            break

    print(result)


sum_to(40)
