def words(word):
    data = {}
    for i in word:
        data[i] = word.count(i)
    return data


word = list("ThiS is String with Upper and lower case Letters".lower().replace(" ", ""))
word.sort()
print words(word)
