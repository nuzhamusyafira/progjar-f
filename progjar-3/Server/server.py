import socket
import time
import threading

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 9000
sock = socket.socket()
sock.bind((SERVER_HOST, SERVER_PORT))
sock.listen(5)
print("Server listening...\n")

def sendFile(client):
    filename = ["Files/pic1.png", "Files/pic2.png", "Files/pic3.png", "Files/pic4.png"]
    for f in filename:
        client.send(f.encode('ascii'))
        fp = open(f, 'rb')
        k = fp.read(1024)
        print("Sending", f)
        while (k):
            client.send(k)
            print("Sending..")
            k = fp.read(1024)
        fp.close()
        print("Done sending", f)
        print()
        time.sleep(1)
    print("Connection", addr, "closed\n")
    client.close()
while True:
    conn, addr = sock.accept()
    print("Got connection from", addr)
    print()
    thread = threading.Thread(target=sendFile, args=(conn,))
    thread.start()