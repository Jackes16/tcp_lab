import socket

HOST = '0.0.0.0'
PORT = 12345

s = socket.socket()
s.bind((HOST, PORT))
s.listen(1)
print("TCP server waiting for connection...")
conn, addr = s.accept()
print(f"Connected to {addr}")
conn.send(b"Hello from Dockerized EC2 server!")
conn.close()
