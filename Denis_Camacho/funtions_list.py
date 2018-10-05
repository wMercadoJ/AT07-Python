def first_function():
    size_list = int(input("into the size the list"))
    elements_list = []
    for i in range(0, size_list):
        data_input = str(input("into the value"))
        elements_list.append(data_input)
        second_function(elements_list)


def second_function(element_list):
    for var in element_list:
        print var


first_function()
