# No arguments defined
# Should ask to the user the number of elements in the list
# According the value inserted ask for each value of the array and push it in a new array
# Return the array


def create_list_of_string(number):
    empty_list = []
    for i in range(number):
        insert_teclado = int(input("Insert the " + str(i + 1) + " numbers: "))
        empty_list.append(insert_teclado)
    return empty_list


# Should receive 1 argument (the array returned in method 1)
# should print the array

def show_item(number):
    print "------- Show the list -------"
    for i in range(number.__len__()):
        print "The "+str(i+1)+" number is "+str(number[i])


insert_number = int(input("Enter quantity of elements to use: "))
list_number = create_list_of_string(insert_number)
show_item(list_number)
