import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 10000)
print("connecting to %s port %s" %server_address)
sock.connect(server_address)

try:
    message = "INI ADALAH DATA YANG DIKIRIM ABCDEFGHIJKLMNOPQ"
    print("sending \"%s\"" %message)
    sock.sendall(message.encode('ascii'))
    amount_received = 0
    amount_expected = len(message)
    while amount_received < amount_expected:
        data = sock.recv(1024).decode('ascii')
        amount_received += len(data)
        print("received \"%s\"" %data)
finally:
    print("closing socket")
sock.close()