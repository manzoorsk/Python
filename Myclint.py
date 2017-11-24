import socket

socket=socket.socket()
socket_address='localhost'
#host=socket.gethostname()
port=12345

socket.connect((socket_address,port))

print(socket.recv(1024))

socket.close()
