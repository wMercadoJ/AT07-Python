def get_url_page(text):
    text_array = text.split(" ")
    for word in text_array:
        if word.find("http") == 0:
            print(word)


get_url_page("la pagina web http://www.google.com.bo se encuentra")
