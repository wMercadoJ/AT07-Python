import operator


def operation(operator_math, operator_one, operator_two):
    operation_math = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}
    if operator_math == "+" or operator_math == "*" or operator_math == "-" or operator_math == "+":
        print(operation_math[operator_math](float(operator_one), float(operator_two)))


operation("+", "3", "4")
operation("-", "3", "4")
operation("*", "3", "4")
operation("/", "4", "3")
operation("(", "4", "5")