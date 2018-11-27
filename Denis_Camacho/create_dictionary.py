
dictionary = {}


def create_dictionary(amount):
    global dictionary
    for i in range(0, amount):
        print("INTO THE HEADER PLEASE:")
        header = str(input())
        print("INTO THE DATA PLEASE:")
        data = str(input())
        dictionary[header] = data


def show_key():
    print(dictionary.keys())


def show_values():
    print(dictionary.values())


def show_dictionary():
    print(dictionary)


create_dictionary(3)
show_key()
show_values()
show_dictionary()
