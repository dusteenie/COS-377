import socket
PORT = 4001
IP = '127.0.0.1'
BUF_SIZE = 1024
# create a socket object name 'k'
sock = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
sock.bind((IP, PORT))
sock.listen(2)
con, addr = sock.accept()
print ('Connection Address is: ' , addr)

data = con.recv(BUF_SIZE)

while data:
	print ("Received data: ", data)
	data = con.recv(BUF_SIZE)

#con.send(data)
con.close()