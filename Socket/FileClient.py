import socket

server = socket.socket()
host = ''
port = 8081

address = (host,port)

server.connect(address)

name = input('File Name : ')
server.send(str.encode(name))

with open(name,'wb') as f:
	print ('file open')

	while True:
		print ('fetching file...')
		data = server.recv(2048)
		print('data=%s', (data))
		if not data:
			break
		f.write(data)
f.close()
server.close()
