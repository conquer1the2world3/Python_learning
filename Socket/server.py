import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostname = socket.gethostname()
port = 9999
s.bind((hostname, port))
s.listen(1)

print(f"Server is running on {hostname}:{port}")

while True:
    c, addr = s.accept()
    print(f"Got a connection from {addr}")
    c.send(b"Thank you for connecting to the server")
    c.close()
