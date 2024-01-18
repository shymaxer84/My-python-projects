import pyshorteners

url = input('Enter the URL :')


def shortenURL(url):
    s = pyshorteners.Shortener()
    print(s.tinyurl.short(url))


shortenURL(url)
