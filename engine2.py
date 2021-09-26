import sys
import pygame
import socket
import os


class Engine:
    def __init__(self, e_sock):
        pygame.init()
        self.e_sock = e_sock
        e_sock.debug()
        e_sock.connect_to_server()

        size = 500, 400
        self.window = pygame.display.set_mode(size)

        self.pos_x = 250
        self.pos_y = 200
        self.rect = pygame.Rect(self.pos_x, self.pos_y, 25, 20)

        pygame.draw.rect(self.window, (20, 228, 214), self.rect)
        pygame.display.flip()

    def refresh(self):
        pygame.draw.rect(self.window, (20, 228, 214), self.rect)
        pygame.display.flip()
        self.e_sock.send_data(str(self.pos_x) + ', ' + str(self.pos_y))

    def topMove(self):
        self.window.fill(pygame.Color(0, 0, 0))
        self.rect = self.rect.move(0, -10)
        self.pos_y = self.pos_y - 10
        self.refresh()

    def bottomMove(self):
        self.window.fill(pygame.Color(0, 0, 0))
        self.rect = self.rect.move(0, 10)
        self.pos_y = self.pos_y + 10
        self.refresh()

    def leftMove(self):
        self.window.fill(pygame.Color(0, 0, 0))
        self.rect = self.rect.move(-10, 0)
        self.pos_x = self.pos_x - 10
        self.refresh()

    def rightMove(self):
        self.window.fill(pygame.Color(0, 0, 0))
        self.rect = self.rect.move(10, 0)
        self.pos_x = self.pos_x + 10
        self.refresh()

    def openMenu(self):
        self.debug("open menu")

    def debug(self, text):
        os.system("cls")
        print(text)

    def listenKeyboardEvent(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_z]:
                    key = 'z'
                elif pygame.key.get_pressed()[pygame.K_s]:
                    key = 's'
                elif pygame.key.get_pressed()[pygame.K_q]:
                    key = 'q'
                elif pygame.key.get_pressed()[pygame.K_d]:
                    key = 'd'
                elif pygame.key.get_pressed()[pygame.K_v]:
                    key = 'v'
                display = "posX = ", self.pos_x, ";posY = ", self.pos_y
                self.debug(display)
                return key

     def run(self):
        while 1:
            key = self.listenKeyboardEvent()
            if key == 'z':
                self.topMove()
            elif key == 's':
                self.bottomMove()
            elif key == 'q':
                self.leftMove()
            elif key == 'd':
                self.rigthMove()
            elif key == 'v':
                self.openMenu()
            key = ''


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
        print(f'My port is {self.port}')

    def connect_to_server(self):
        try:
            self.host = 'localhost'
            self.sock.connect((self.host, self.port))
            print('Connected to server.')
        except ConnectionRefusedError or ConnectionError:
            print('weird')

    def send_data(self, data):
        data = data.encode('utf8')
        print(data)
        self.sock.sendall(data)

    def close_socket(self):
        self.sock.close()


if __name__ == '__main__':
    socket = GameSocket()
    engine = Engine(socket)
    engine.run()

# INTERESSANT
# a = pygame.key.get_pressed()[pygame.K_a]
