select_operator = str(input("inset the operator"))
number1 = input("num1")
number2 = input("num2")


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
            return "Oops!  That was no valid number.  Try again..."

    else:
        return "no fount the operator ........"


operators = ["*", "+", "-", "/", "g"]
for i in operators:
    print (perform_operation(i, 5, 10))

print (select_operator, number1, number2)
print (perform_operation(select_operator, number1, number2))
