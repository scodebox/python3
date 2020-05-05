import socket
import sys
from _thread import *


def send(msg):
	try:
		print (msg)
	finally:
		print("done")


def handleClient(client):
	msg = client.recv(1024).decode()
	start_new_thread(send,(msg,) )
	client.close()


host = ''
port = 9000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
	server.bind((host,port))
	print ('server running at',host,':',port)
except socket.error as e:
	print (str(e))

server.listen(5)

while True:

	client,addr = server.accept()
	print ('connected to ',addr[0],':',addr[1])

	start_new_thread(handleClient,(client,) )