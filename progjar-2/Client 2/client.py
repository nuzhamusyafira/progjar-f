import socket

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 9000
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto("connected".encode('ascii'), (SERVER_HOST, SERVER_PORT))
filename, addr = sock.recvfrom(1024)
filename = filename.decode('ascii')
while True:
	if filename == "done":
		break
	with open(filename, 'wb') as fp:
	    print("File", filename, "created")
	    while True:
	        print("Receiving data...")
	        data, addr = sock.recvfrom(1024)
	        try:
	        	data = data.decode('ascii')
	        	break
	        except:
	        	if not data:
	        		break
	        	fp.write(data)
	    fp.close()
	    print("Successfully get the file", filename)
	    print()
	filename = data
print("Connection closed")