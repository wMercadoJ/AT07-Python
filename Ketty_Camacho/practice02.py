def perform_operation(a, b, c):
    b = int(b)
    c = int(c)
    if (a == '-'):
        print b - c
    if (a == '+'):
        print c + b
    if (a == '*'):
        print b * c
    if (a == '**'):
        print b ** c
    elif (a == '/' and b > c):
        print b / c
    else:
        print c / b



perform_operation('/', '8', '1')
