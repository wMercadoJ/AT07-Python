url_input = "http>://www.google.com test"


def get_url(url):
    if "http://" in url:
        complete_url = url[url.find("http://"):len(url)]
        return complete_url[0:complete_url.find(" ")]


print(get_url("http://www.google.com test "))

