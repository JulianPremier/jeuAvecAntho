import socket

host, port = ('', 4977)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))

while True:
    sock.listen(5)
    conn, addr = sock.accept()
    print('Client connected')

conn.close()
sock.close()


