import socket

s=socket.socket()
hostname=socket.gethostname()
port=9999
s.connect((hostname, port))
print(s.recv(1024).decode('utf-8'))
s.send(b"Hello, server!")
s.close()
print("Connection closed")
