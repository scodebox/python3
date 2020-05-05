import urllib.request

x = urllib.request.urlopen('http://www.google.com')
print (x.read())
    
