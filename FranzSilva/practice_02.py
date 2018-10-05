class Aritmetics:

    def aritmetic_functions(elf, operator, number_1, number_2):
        if operator == "+":
            result = number_1 + number_2

        elif operator == "-":
            result = number_1 - number_2

        elif operator == "*":
            result = number_1 * number_2

        elif operator == "/":
            result = number_1 / number_2
        else:
            result = 'Error: invalid operator'
        print("Result: ", result)