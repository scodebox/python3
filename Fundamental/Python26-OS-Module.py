import os

current = os.getcwd()
print (current)

os.mkdir('newDir')
os.rename('newDir','newDir2')
os.rmdir('newDir2')
