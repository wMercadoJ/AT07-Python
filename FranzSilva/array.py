
def create_array():
    array = []
    length = int(input('Insert the length of array:'))
    for i in range(length):
        value = input('Insert the values:')
        array.append(value)
    return array


def print_array(array):
    print(array)


print_array(create_array())