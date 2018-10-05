# Suppose any line of text can contain at most one url that starts with http:// and ends at the next space in the line. Write a fragment of code to extract and print the full url if it is present.
def get_url(url):
    string_split = str(url).split(" ")
    for word_auxiliary in string_split:
        if str(word_auxiliary).__contains__("http:"):
            return word_auxiliary

url = raw_input("Enter a text with a URL included: ")

print (get_url(url))
