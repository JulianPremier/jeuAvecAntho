import sys
import pygame
import os
import tkinter as tk

from GameSocket import GameSocket
from Menu import Menu

class Engine:
    def __init__(self, e_sock):
        pygame.init()

        #socket config
        self.e_sock = e_sock
        e_sock.debug()
        e_sock.connect_to_server()

        #window config
        size = 500, 400
        self.window = pygame.display.set_mode(size)

        #skin config
        self.pos_x = 250
        self.pos_y = 200
        self.rect = pygame.Rect(self.pos_x, self.pos_y, 25, 20)
        self.skinColor = pygame.Color(20, 228, 214)

        #pseudo config
        pygame.font.init()
        self.myfont = pygame.font.SysFont('Arial', 15)
        self.pseudo = "Unknown"

        self.refresh()

    def refresh(self):
        """
        refresh the screen (Must be use after graphic changement)

        :return: Void
        """
        #pseudo refresh
        self.textsurface = self.myfont.render(self.pseudo, False, (255, 255, 255))
        self.window.blit(self.textsurface,(self.pos_x, self.pos_y - 20))

        #skin refresh
        pygame.draw.rect(self.window, self.skinColor, self.rect)

        #window refresh
        pygame.display.flip()

    def sendData(self):
        """
        Send skin position to the server

        :return: Void
        """
        try:
            self.e_sock.send_data(str(self.pos_x) + ', ' + str(self.pos_y))
        except ConnectionError as err:
            print('Exception raised:', err)


    def setSkinColor(self, newColor):
        """
        Change skin color

        :param newColor: string newColor
        :return: Void
        """
        self.skinColor = newColor
        self.refresh()

    def setPseudo(self, newPseudo):
        """
        Change pseudo text

        :param newPseudo: string newPseudo
        :return: Void
        """
        self.pseudo = newPseudo
        self.window.fill(pygame.Color(0, 0, 0))
        self.refresh()

    def topMove(self):
        """
        move skin at top direction

        :return: Void
        """
        self.window.fill(pygame.Color(0, 0, 0))
        self.rect = self.rect.move(0, -10)
        self.pos_y = self.pos_y - 10

    def bottomMove(self):
        """
        move skin at bottom direction

        :return: Void
        """
        self.window.fill(pygame.Color(0, 0, 0))
        self.rect = self.rect.move(0, 10)
        self.pos_y = self.pos_y + 10

    def leftMove(self):
        """
        move skin at left direction

        :return: Void
        """
        self.window.fill(pygame.Color(0, 0, 0))
        self.rect = self.rect.move(-10, 0)
        self.pos_x = self.pos_x - 10

    def rightMove(self):
        """
        move skin at right direction

        :return: Void
        """
        self.window.fill(pygame.Color(0, 0, 0))
        self.rect = self.rect.move(10, 0)
        self.pos_x = self.pos_x + 10

    def openMenu(self):
        """
        open the menu (from Menu object)

        :return: Void
        """
        root = tk.Tk()
        menu = Menu(self, master=root)
        menu.mainloop()

    def debug(self, text):
        """
        Debug more easier the text

        :return: Void
        """
        os.system("cls")
        print(text)

    def listenKeyboardEvent(self):
        """
        listen and return what key was pressed

        :return: char
        """

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
            self.sendData()
            self.refresh()