import sys, pygame
import os

class moteur:
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

moteur.run()
    
#INTERESSANT
#a = pygame.key.get_pressed()[pygame.K_a]

