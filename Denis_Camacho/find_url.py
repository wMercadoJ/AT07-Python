def find_url(url):
    http = "http://"
    urls = url.split(" ")
    for var in urls:
        if var.__contains__(http):
            return var


print find_url("My url is : http://www.google.com test")
