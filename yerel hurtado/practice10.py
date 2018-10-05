def times_letter(text):
    text = text.lower()
    words = text.replace(" ", "")
    dic = {}
    for i in words:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    print(sorted(dic.items()))


times_letter("Esto Es Un Texto")
