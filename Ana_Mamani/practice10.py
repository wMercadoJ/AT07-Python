# Practice 10
# author Ana Mamani Zenteno
# since 10/05/2018

def reads_a_string(cadena):
    variable_cadena = cadena.replace(" ", "")
    value_data = dict()
    for i in variable_cadena.lower():
        if i in value_data:
            value_data[i] += 1
        else:
            value_data[i] = 1
    print sorted(value_data.items())


reads_a_string("ThiS is String with Upper and lower case Letters")
