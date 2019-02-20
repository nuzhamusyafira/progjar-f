import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = 'localhost'
port = 10000
server_address = (ip, port)
print("starting up on %s port %s" %server_address)
sock.bind(server_address)
sock.listen(1)
while True:
	print("waiting for a connection")
	connection, client_address = sock.accept()
	print("connection from", client_address)
	while True:
		data = connection.recv(1024).decode('ascii')
		print("received", data)
		if data:
			print("sending data back to the client")
			data = "--> " + data
			connection.sendall(data.encode('ascii'))
		else:
			print("no more data from", client_address)
			break
	connection.close()