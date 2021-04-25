import socket

PORT = 4001
IP = '127.0.0.1'
BUF_SIZE = 1024

s = 'wut'

sock = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
sock.connect((IP, PORT))
#sock.send(s)
sock.send(bytes(s, 'utf-8'))
data = sock.recv(BUF_SIZE)

sock.close()