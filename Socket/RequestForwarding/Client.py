import socket

server = socket.socket()

host = '192.168.1.16'
port = 9001
address = (host,port)
server.connect(address)

msg = input ('Enter msg : ')

server.sendall(str.encode(msg))
server.close()
