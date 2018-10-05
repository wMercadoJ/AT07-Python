def function_01():
    leng = int(input("introduce # element "))
    list = []
    for i in range(leng):
        value = int(input("add value-->"))
        list.append(value)
    return list


def function_02(content_list):
    for i in range(len(content_list)):
        print content_list[i]


content_list = function_01()
function_02(content_list)
