import socket

s = socket.socket()
host = ''
s.connect((host,9000))

while True:
	msg = input('enter msg : ')
	s.sendall(str.encode(msg))
	msg = s.recv(1024).decode()
	print (msg)
