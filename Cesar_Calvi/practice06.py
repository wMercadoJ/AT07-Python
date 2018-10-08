
# Suppose any line of text can contain at most one url that starts with “http://” and ends at the next space in the
# line. Write a fragment of code to extract and print the full url if it is present.


def show_present_url(chain_input):
    list = chain_input.split("\n")
    print "list", list
    for item in list:
        all = item.split(" ")
        for article in all:
            if article.startswith("https://"):
                print "url", article


if __name__ == '__main__':
    print "enter chain"
    chain = str(raw_input())
    show_present_url(chain)
