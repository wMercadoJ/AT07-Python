def times_letter(text):
    text = text.lower()
    words = text.replace(" ", "")
    dic = {}
    for word in words:
        if word in dic:
            dic[word] += 1
        else:
            dic[word] = 1
    print(sorted(dic.items()))


times_letter("Esto Es Un Texto")
