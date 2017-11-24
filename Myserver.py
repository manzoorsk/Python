import socket

socket=socket.socket()
socket_name='localhost'
#host=''
port=12345

socket.bind((socket_name,port))
socket.listen(10)
while True:
    conn,address=socket.accept()
    print('i just got connection from the server',address)
    conn.send('send the server')
    conn.close()

