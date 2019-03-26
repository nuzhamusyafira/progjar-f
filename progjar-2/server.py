import socket
import time

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 9000
sock = socket.socket()
sock.bind((SERVER_HOST, SERVER_PORT))
sock.listen(5)
print("Server listening...\n")
while True:
    conn, addr = sock.accept()
    print("Got connection from", addr)
    print()
    filename = ["pic1.png", "pic2.png", "pic3.png", "pic4.png"]
    for f in filename:
        conn.send(f.encode('ascii'))
        fp = open(f, 'rb')
        k = fp.read(1024)
        print("Sending", f)
        while (k):
            conn.send(k)
            print("Sending..")
            k = fp.read(1024)
        fp.close()
        print("Done sending", f)
        print()
        time.sleep(1)
    print("Connection", addr, "closed\n")
    conn.close()