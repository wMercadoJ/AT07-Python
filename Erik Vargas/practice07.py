def add_to_list():
    tam = int(input("insert tam:"))
    list = []
    for x in xrange(0, tam):
        date = int(input("insert date:"))
        list.append(date)

    get_list(list)


def get_list(list):
    for x in list:
        print x


add_to_list()
