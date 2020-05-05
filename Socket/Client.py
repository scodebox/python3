import socket

server = socket.socket()
host = "localhost"
port = 1234

address = (host,port)

server.connect(address)

req = input('Enter data : ')

if req == 'c':
    server.sendall(str.encode(req))
    print (server.recv(1024).decode('UTF-8'))
    server.close()
