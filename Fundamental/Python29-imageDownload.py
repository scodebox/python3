import random
import urllib.request

def getImage(url):
    name = random.randrange(1,100)
    fullname = str(name) + '.jpg'

    urllib.request.urlretrieve(url,fullname)


getImage(input('Enter url : '))
