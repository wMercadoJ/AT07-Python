# Create a function that receive 3 arguments :
# 	2 numbers
# 	1 operations
# According the operation defined the expected result need to be printed.
# For example :  operator '*' , numbers: 5 y 6
# perform_operation('*',5,6) => 30

def perform_operation(operator, num1, num2):
    return {
        '+': int(num1) + int(num2),
        '-': int(num1) - int(num2),
        '*': int(num1) * int(num2),
        '/': int(num1) / int(num2),
        '**': int(num1) ** int(num2),
        '//': int(num1) // int(num2),
    }.get(operator,"Option no valid")


print (perform_operation('*', 5, 6))
