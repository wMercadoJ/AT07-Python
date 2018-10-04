#Create a function that receive 3 arguments :
#	2 numbers
#	1 operations
print ("----- Create function -----")
def format_operation(operator, value1, value2):
    if operator == "+":
        print (value1 + value2)
    else:
        if operator == "-":
            print (value1 - value2)
        else:
            if operator == "*":
                print (value1 * value2)
            else:
                print (value1 / value2)

first_value = int(input("Enter the first value: "))
second_value = int(input("Enter the second value: "))
value_aritmethics = raw_input("Enter the arithmetic operator: ")

format_operation(value_aritmethics,first_value,second_value)
#format_operation("*",8,5)
