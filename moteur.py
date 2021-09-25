import sys, pygame
import socket
import os


class Moteur:
    @staticmethod
    def run():
        pygame.init()

        size = 500, 400
        window = pygame.display.set_mode(size)

        rect_pos = pos_x, pos_y = 250, 200
        rect = pygame.Rect(pos_x, pos_y, 25, 20)
        pygame.draw.rect(window, (20, 228, 214), rect)
        pygame.display.flip()

        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if pygame.key.get_pressed()[pygame.K_z]:
                        window.fill(pygame.Color(0, 0, 0))
                        rect = rect.move(0, -10)
                        pos_y = pos_y - 10
                        pygame.draw.rect(window, (20, 228, 214), rect)
                        pygame.display.flip()
                    elif pygame.key.get_pressed()[pygame.K_s]:
                        window.fill(pygame.Color(0, 0, 0))
                        rect = rect.move(0, 10)
                        pos_y = pos_y + 10
                        pygame.draw.rect(window, (20, 228, 214), rect)
                        pygame.display.flip()
                    elif pygame.key.get_pressed()[pygame.K_q]:
                        window.fill(pygame.Color(0, 0, 0))
                        rect = rect.move(-10, 0)
                        pos_x = pos_x - 10
                        pygame.draw.rect(window, (20, 228, 214), rect)
                        pygame.display.flip()
                    elif pygame.key.get_pressed()[pygame.K_d]:
                        window.fill(pygame.Color(0, 0, 0))
                        rect = rect.move(10, 0)
                        pos_x = pos_x + 10
                        pygame.draw.rect(window, (20, 228, 214), rect)
                        pygame.display.flip()
                    os.system("cls")
                    print("posX = ", pos_x, ";posY = ", pos_y)


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
        finally:
            self.sock.close()


if __name__ == '__main__':
    socket = GameSocket()
    socket.debug()
    socket.connect_to_server()
    Moteur.run()

# INTERESSANT
# a = pygame.key.get_pressed()[pygame.K_a]
