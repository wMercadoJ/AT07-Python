def get_url(page):
    words = page.split(" ")
    for i in range(len(words)):
        if words[i].__contains__("http"):
            print words[i]



get_url("my url es: http://www.google.com test http://www.hoogle.com ")
