import collections
import operator

text = "ThiS is String with Upper and lower case Letters"


def read_string(word):
    word = list(text.lower().replace(" ", ""))
    dict = collections.Counter(word)
    result = sorted(dict.items(), key=operator.itemgetter(0))
    print result


read_string(text)
