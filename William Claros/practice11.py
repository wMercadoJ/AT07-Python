# Write a program that reads a string and returns a table of the letters of the alphabet in alphabetical
#  order which occur in the string together with the number of times each letter occurs.
import collections
import operator

def alphabetical_order_count(string):
    return sorted((collections.Counter(string.lower().replace(" ", ""))).items(), key=operator.itemgetter(0))

string = raw_input("Enter to word: ")
array = alphabetical_order_count(string)
for other in array:
    print other
