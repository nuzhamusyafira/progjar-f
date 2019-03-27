import socket
import time
import threading

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 9000
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((SERVER_HOST, SERVER_PORT))
print("Server is ready\n")

def sendFile(c_addr):
    filename = ["pic1.png", "pic2.png", "pic3.png", "pic4.png"]
    for f in filename:
        sock.sendto(f.encode('ascii'), c_addr)
        fp = open(f, 'rb')
        k = fp.read(1024)
        print("Sending", f, "to", c_addr)
        while (k):
            sock.sendto(k, c_addr)
            print("Sending..")
            k = fp.read(1024)
        fp.close()
        print("Done sending", f)
        print()
        time.sleep(1)
    sock.sendto("done".encode('ascii'), c_addr)
    print("Connection", c_addr, "closed\n")

while True:
    data, addr = sock.recvfrom(1024)
    print("Got connection from", addr)
    print()
    thread = threading.Thread(target=sendFile, args=(addr, ))
    thread.start()