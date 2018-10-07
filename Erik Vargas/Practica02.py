operators = str(input("insert number first:"))
number1 = input("insert number first:")
number2 = input("insert number second:")


def perform_operation(operator, num1, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        try:
            return num1 / num2
        except ZeroDivisionError:
            return "No is possible divide for Zero"
    elif operator == "%":
        return num1 % num2
    elif operator == "//":
        return num1 // num2
    else:
        return "no exist operator"


print (perform_operation(operators, number1, number2))
