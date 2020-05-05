import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = ''
port = 8081
address = (host,port)

server.bind(address)
server.listen(1)
print ('Server running Addrss : ',host,":",port)
flag = 0

while True:
	try:
		if flag!=1:
			client,addr = server.accept()
			print ('Connected to ',addr[0],':',addr[1])
			flag = 1

		name = client.recv(1024).decode()
		
		f = open(name,'rb')
		l = f.read(2048)

		while (l):
			client.send(l)
			l=f.read(2048)
		f.close()
		client.close()

		flag=0
		print ('done')
	except Exception as e:
		print ('Exception')
		flag=0
