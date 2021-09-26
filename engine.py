import sys, pygame
import os
from tkinter import *
from tkinter import ttk

class engine:
    def __init__(self):
        pygame.init()

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

    def rigthMove(self):
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

engine = engine()
engine.run()