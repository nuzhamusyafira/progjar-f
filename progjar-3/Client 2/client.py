import socket

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 9000
FILE_FOLDER = "Files"
SAVE_FOLDER = "Downloads"
sock = socket.socket()
sock.connect((SERVER_HOST, SERVER_PORT))
connected = sock.recv(1024).decode('ascii')
if connected:
	print(connected)
	print("\nType:")
	print("1. **req " +FILE_FOLDER+ "/<filename>\n--> To request files from Server")
	print("\nOr\n")
	print("2. **send " +FILE_FOLDER+ "/<filename>\n--> To send files to Server\n")

while True:
	filename = input()
	sock.send(filename.encode('ascii'))
	if "**req" in filename: 
		filename = filename.replace("**req " +FILE_FOLDER+ "", SAVE_FOLDER, 1)
		with open(filename, 'wb') as fp:
		    print("File", filename, "created")
		    print("Receiving data...")
		    while True:
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
	elif "**send" in filename: 
		filename = filename.replace("**send ", "", 1)
		fp = open(filename, 'rb')
		k = fp.read(1024)
		print("Sending", filename, "to Server")
		print("Start sending..")
		while (k):
		    sock.send(k)
		    k = fp.read(1024)
		fp.close()
		print("Done sending", filename)
		print()
		sock.send("done".encode('ascii'))
sock.close()
print("Connection closed")