def funtion_1():
    size_list = int(input("into the size the list"))
    list=[]
    for i in range(0, size_list):
        data_intput = str(input("into the value"))
        list.append(data_intput)
    funtion_2(list)


def funtion_2(list):
    for var in list:
        print var


funtion_1()
