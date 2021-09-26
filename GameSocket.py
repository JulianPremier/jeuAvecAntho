import socket


class GameSocket:
    host = ''
    port = 4977
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn = None
    addr = None

    def __init__(self, new_port=None):
        if new_port is not None:
            self.port = new_port

    def debug(self):
        """
        Used for debugging purpose only
        :return: Void
        """
        print(f'My port is {self.port}')

    def connect_to_server(self):
        """
        Connect to local server a.k.a. localhost / 127.0.0.1
        :return: Void
        """
        try:
            self.host = 'localhost'
            self.sock.connect((self.host, self.port))
            print('Connected to server.')
        except ConnectionRefusedError or ConnectionError:
            print('weird')

    def send_data(self, data):
        """
        Send data to server in UTF-8 encoding

        :param data: string data
        :return: Void
        """
        data = data.encode('utf8')
        self.sock.sendall(data)

    def close_socket(self):
        self.sock.close()