
# Dictionary to count the repeated words
# first options


def create_dictionary(chain):
    dictionary_string = list(chain.lower().replace(" ", ""))
    dictionary_string.sort()
    dictionary_aux = {}
    for i in dictionary_string:
        if i not in dictionary_aux.keys():
            dictionary_aux[i] = 1
        else:
            count = dictionary_aux[i]
            dictionary_aux[i] = 1 + count
    print "Result----", dictionary_aux
    return dictionary_aux


if __name__ == '__main__':
    print ("Enter chain")
    value = str(raw_input())
    create_dictionary(value)

# Second options


def create_dictionary(chain):
    dictionary_string = list(chain.lower().replace(" ", ""))
    dictionary_string.sort()
    dictionary = {}
    for i in dictionary_string:
        dictionary[i] = dictionary_string.count(i)
    print "Result----", dictionary
    return dictionary


if __name__ == '__main__':
    print ("Enter chain")
    value = str(raw_input())
    create_dictionary(value)
