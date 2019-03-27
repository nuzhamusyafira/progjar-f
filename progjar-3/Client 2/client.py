import socket
from os import listdir
from os.path import isfile, join

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
	print("1. **req " +FILE_FOLDER+ "/<filename>\n--> To request files from Server\n")
	print("2. **send " +FILE_FOLDER+ "/<filename>\n--> To send files to Server\n")
	print("3. **ls <directory_path>\n--> To list all files in the directory\n")
	print("4. **q\n--> To quit\n")
	print("========================================================================\n")

while True:
	filename = input()
	if "**ls" in filename:
		path = filename.replace("**ls ", "", 1)
		files = [f for f in listdir(path) if isfile(join(path, f))]
		print("List of files in '" +path+ "':")
		for i in range(len(files)):
			print("-", files[i])
		print()
	else:
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
			    print("Successfully save the file in", filename)
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
		elif "**q" in filename:
			print("Connection closed")
			break