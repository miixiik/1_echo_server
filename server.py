import socket

file = open('log1.txt', 'w')
sock = socket.socket()
port = 9097
while (True):
	try:
		sock.bind(('', port))
		sock.listen(0)
		break
	except:
		port +=1

print (port)
while True:
	conn, addr = sock.accept()
	file.write(str(addr[0]) + " " + str(addr[0]) + "\n")
	#print(addr)

	while True:
		data = conn.recv(1024)
		msg = data.decode()
		if not data:
			print("Client left from the chat. ")
			break
		print (msg)
		conn.send(data)
		file.write(msg + "\n")

	#if "exit" in msg:
		#break
	

conn.close()
