import socket

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 9000
sock = socket.socket()
sock.connect((SERVER_HOST, SERVER_PORT))
filename = sock.recv(1024).decode('ascii')
while filename:
	with open(filename, 'wb') as fp:
	    print("File", filename, "created")
	    while True:
	        print("Receiving data...")
	        data = sock.recv(1024)
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
sock.close()
print("Connection closed")