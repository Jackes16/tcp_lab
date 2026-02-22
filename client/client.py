import socket

HOST = '34.235.155.245'
PORT = 12345

s = socket.socket()
s.connect((HOST, PORT))
data = s.recv(1024)
print('Received:', data.decode())
s.close()
