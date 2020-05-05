import socket
import threading

def send():
	global msg,lock
	lock.acquire()
	try:
		s = socket.socket()
		host = ''
		port = 9001
		address = (host,port)
		s.connect(address)
		s.sendall(str.encode(msg))
		s.close()
	finally:
		lock.release()



def main():
	global lock,msg
	lock = threading.Lock()
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	host = ''
	port = 9000
	address = (host,port)
	server.bind(address)
	server.listen(1)

	print ('server running at',host,':',port)

	while True:
		try:
			client,addr = server.accept()
			print ('connected to ',addr[0],':',addr[1])

			msg = client.recv(1024).decode()

			forward = threading.Thread(target=send,name="mail")
			forward.start()
			print ('get msg >> ',msg)
			

		except Exception as e:
			print (e)

if __name__ == '__main__':
	main()
