def perform_operation(operators, number_01, number_02):
    number_01 = int(number_01)
    number_02 = int(number_02)
    if (operators == '-'):
        print number_01 - number_02
    if (operators == '+'):
        print number_02 + number_01
    if (operators == '*'):
        print number_01 * number_02
    if (operators == '**'):
        print number_01 ** number_02
    elif (operators == '/' and number_01 > number_02):
        print number_01 / number_02
    else:
        print number_02 / number_01



perform_operation('/', '8', '2')
