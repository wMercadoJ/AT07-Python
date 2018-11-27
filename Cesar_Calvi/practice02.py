
def doProcess(number_one, number_two, operator):
    if operator == "+":
        print "SUMA: "
        print number_one + number_two

    if operator == "-":
        print "RESTA: "
        print number_one - number_two

    if operator == "*":
        print "MULTIPLICACION: "
        print number_one * number_two

    if operator == "/":
        print "DIVISION: "
        print number_one / number_two


if __name__ == "__main__":
    print ("First number")
    number_one = float(raw_input())
    print ("Second number")
    number_two = float(raw_input())
    print ("Operator")
    operator = str(raw_input())
    doProcess(number_one, number_two, operator)
