
# Fill a list by keyboard


def create_array(num):
    array_aux = []
    for i in range(num):
        print ("Enter ", i + 1, "Element")
        value = str(raw_input())
        array_aux.append(value)
    return array_aux


def show_array(arr):
    print ("array result", arr)


if __name__ == '__main__':
    print ("Enter value from the array")
    value_array = int(raw_input())
    result_create = create_array(value_array)
    show_array(result_create)



