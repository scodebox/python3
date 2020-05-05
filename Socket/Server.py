import socket
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = "localhost"
port = 1234
address = (host,port)

server.bind(address)
server.listen(1)
print ('Server running Addrss : ',host,":",port)
flag = 0

client,addr = server.accept()
print ('Connected to ',addr[0],':',addr[1])

req = client.recv(1024)  
print (req.decode('UTF-8'))
reply = "working"
client.sendall(str.encode(reply));
