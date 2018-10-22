import urllib.request


def wordCount(url, word):
    fp = urllib.request.urlopen(url)
    mybytes = fp.read()
    mystr = mybytes.decode("utf8")
    fp.close()
    wordlower = word.lower()
    count = 0
    line = mystr.split()
    for each in line:
        wordline = each.lower()
        wordline = wordline.strip("!@#$%¨&*()_-+=?/.,<>:;{}[]")
        if wordlower == wordline:
            count += 1
    return count
