import socket

host, port = ('', 4977)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    s.listen(5)
    conn, addr = s.accept()
    with conn:
        print('Client connected', addr)
        while True:
            data = conn.recv(1024)
            data = data.decode('utf8')
            print(data)
        if not data:
            conn.close()
            s.close()






