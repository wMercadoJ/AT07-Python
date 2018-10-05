url = "My url is : http://www.google.com test".split(" ")
find_word = list(filter(lambda http: http.__contains__("http://"), url))

print find_word
