import hashlib
m = input('Enter : ')
print(hashlib.md5(m.encode('utf-8')).hexdigest())
