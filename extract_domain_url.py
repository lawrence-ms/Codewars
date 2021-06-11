# https://www.codewars.com/kata/514a024011ea4fb54200004b

def domain_name(url):
    if url.partition("www.")[1] == "":
        if url.partition("://")[1] == "":
            return url.partition(".")[0]
        return url.partition("://")[2].partition(".")[0]
    return url.partition("www.")[2].partition(".")[0]
