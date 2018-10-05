# Practice 07
# author Ana Mamani Zenteno
# since 10/05/2018

def insert():
    read_key = int(input('ingrese the tam'))
    arreglo = []
    for i in range(read_key):
        insert_key = int(input("inserte value"))
        arreglo.append(insert_key)
    return arreglo


def get_value(value_arreglo):
    for i in range(len(value_arreglo)):
        print value_arreglo[i]


arreglo = insert()
get_value(arreglo)
