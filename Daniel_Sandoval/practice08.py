# Suppose any line of text can contain at most one url that starts with
#  http:// and ends at the next space in the line. Write a fragment
# of code to extract and print the full url if it is present.


def get_url(string_url):
    text = str(string_url).split(" ")
    for urls in text:
        if urls.__contains__("http://"):
            print (urls)


world = raw_input("Insert the text with a url: ")
get_url(world)
