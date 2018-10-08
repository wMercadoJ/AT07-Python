
def set_array():
    size = int(input("set size of array"))
    list_array = []
    for number in range(size):
        list_array.append(input("new number in array"))
    return list_array


def print_array(array_list):
    print(array_list)


array = set_array()
print_array(array)

