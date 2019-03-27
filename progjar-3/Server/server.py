import socket
import time
import threading

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 9000
FILE_FOLDER = "Files"
SAVE_FOLDER = "Downloads"
sock = socket.socket()
sock.bind((SERVER_HOST, SERVER_PORT))
sock.listen(5)
print("Server listening...\n")

def sendFile(client, ad):
    filename = client.recv(1024).decode('ascii')
    while filename:
        if "req" in filename:
            filename = filename.replace("req ", "", 1)
            fp = open(filename, 'rb')
            k = fp.read(1024)
            print("Sending", filename, "to", ad)
            print("Start sending..")
            while (k):
                client.send(k)
                k = fp.read(1024)
            fp.close()
            print("Done sending", filename)
            print()
            client.send("done".encode('ascii'))
        elif "send" in filename:
            filename = filename.replace("send " +FILE_FOLDER+ "", SAVE_FOLDER, 1)
            with open(filename, 'wb') as fp:
                print("File", filename, "from", ad, "created")
                print("Receiving data...")
                while True:
                    data = client.recv(1024)
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
        filename = client.recv(1024).decode('ascii')

while True:
    conn, addr = sock.accept()
    print("Got connection from", addr)
    conn.send("Connected to the Server".encode('ascii'))
    print()
    thread = threading.Thread(target=sendFile, args=(conn, addr, ))
    thread.start()