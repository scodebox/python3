import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = ''
port = 9001
address = (host,port)
server.bind(address)
server.listen(1)

print ('server running at',host,':',port)

while True:
	try:
		client,addr = server.accept()
		print ('connected to ',addr[0],':',addr[1])

		msg = client.recv(1024)
		print ('get msg : ')
		print (msg.decode('UTF-8'))

	except Exception as e:
		print ('Problem')


