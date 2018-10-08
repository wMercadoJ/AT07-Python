
def create_array():
    array = []
    length = int(input('Insert the length of array:'))
    for index in range(length):
        value = input('Insert the values:')
        array.append(value)
    return array


print(create_array())
