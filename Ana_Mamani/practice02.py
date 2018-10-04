# Practice 02 function that receive 3 arguments
# author Ana Mamani
# since 10/04/2018

def perform_operation(x, a, b):
    a = int(a)
    b = int(b)
    if x == "+":
        result = a + b
    if x == "-":
        result = a - b
    if x == "*":
        result = a * b
    if x == "/":
        result = a / b
    return result


print perform_operation("%", "6", "7")
