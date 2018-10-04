
def doProcess(a, b, c):
    if c == "+":
        print "SUMA: "
        print a + b

    if c == "-":
        print "RESTA: "
        print a - b

    if c == "*":
        print "MULTIPLICACION: "
        print a * b

    if c == "/":
        print "DIVISION: "
        print a / b


if __name__ == "__main__":
    print ("First number")
    a = float(raw_input())
    print ("Second number")
    b = float(raw_input())
    print ("Operator")
    c = str(raw_input())
    doProcess(a, b, c)
