def table_letters(sentence):
    join_letter = list(sentence.replace(" ", "").lower())
    join_letter.sort()
    dic = {}
    for i in join_letter:
        dic[i] = join_letter.count(i)
    return dic


print table_letters("ThiS is String with Upper and lower case Letters")
