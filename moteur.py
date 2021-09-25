import sys, pygame
import os

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

    def listenKeyboardEvent(self):
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if pygame.key.get_pressed()[pygame.K_z]:
                        self.topMove()
                    elif pygame.key.get_pressed()[pygame.K_s]:
                        self.bottomMove()
                    elif pygame.key.get_pressed()[pygame.K_q]:
                        self.leftMove()
                    elif pygame.key.get_pressed()[pygame.K_d]:
                        self.rigthMove()
                    os.system("cls")
                    print("posX = ", self.pos_x, ";posY = ", self.pos_y)

engine = engine()
engine.listenKeyboardEvent()
    
#INTERESSANT
#a = pygame.key.get_pressed()[pygame.K_a]

