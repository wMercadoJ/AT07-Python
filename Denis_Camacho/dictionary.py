def words(words):
    data = {}
    for word in words:
        data[word] = words.count(word)
    return data


word = list("ThiS is String with Upper and lower case Letters".lower().replace(" ", ""))
word.sort()
print(words(word))
