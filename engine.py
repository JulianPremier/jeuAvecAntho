import sys
import pygame
import os
import tkinter as tk

from GameSocket import GameSocket
from Menu import Menu


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

        self.skinColor = pygame.Color(20, 228, 214)
        pygame.draw.rect(self.window, self.skinColor, self.rect)
        pygame.display.flip()

    def refresh(self):
        pygame.draw.rect(self.window, self.skinColor, self.rect)
        pygame.display.flip()
        try:
            self.e_sock.send_data(str(self.pos_x) + ', ' + str(self.pos_y))
        except ConnectionError as err:
            print('Exception raised:', err)

    def setSkinColor(self, newColor):
        self.skinColor = newColor
        self.refresh()

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
        root = tk.Tk()
        menu = Menu(master=root)
        menu.mainloop()

    def debug(self, text):
        os.system("cls")
        print(text)

    def listenKeyboardEvent(self):
        key = ''
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
                self.rightMove()
            elif key == 'v':
                self.openMenu()


if __name__ == '__main__':
    socket = GameSocket()
    engine = Engine(socket)
    engine.run()

# INTERESSANT
# a = pygame.key.get_pressed()[pygame.K_a]
