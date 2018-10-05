# Practice 07
# author Ana Mamani
# since 10/05/2018

def most_one_url(text):
    words = text.split()
    for url in words:
        if url.find("http") == 0:
            print url


most_one_url("Mi url es: http://www.google.com test ")
