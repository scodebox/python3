import socket
import threading

def connection(client,address):
	with client:
		print ('connected by ', address)
		while True:
			msg = client.recv(1024).decode()
			if not msg:
				break
			print (msg)
			client.sendall(str.encode(msg))


s = socket.socket()
host = ''
s.bind((host,9000))
s.listen(5)

while True:
	client,address = s.accept()
	t = threading.Thread(target=connection, args=(client,address))
	t.start()
