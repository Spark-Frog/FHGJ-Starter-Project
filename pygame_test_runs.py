import sys

import pygame

from data.utils import load_image

from data.entities import PhysicsEntity


class Game:
    def __init__(self):
        
        pygame.init()

        pygame.display.set_caption("JWLC Game")

        self.screen = pygame.display.set_mode((640,480))

        self.clock = pygame.time.Clock()
        '''
        self.ing = pygame.image.load("00.png")
        self.ing.set_colorkey((0,0,0))
        self.ing = pygame.transform.scale(self.ing, (60,60))
        '''
        self.ing_pos = [160,260]

        self.movement = [False, False, False, False]

        self.assests= {
            'player' : load_image('entities/player.png')

        }
        '''
        self.collison_area = pygame.Rect(50,50,300,50)
        '''
        self.player = PhysicsEntity(self, 'player', (50,50), (8,15))

    def run(self):
        while True:
            self.screen.fill((0,0,0))

            self.player.update(self.movement[1]-self.movement[0], 0)
            self.player.render(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w or event.key == pygame.K_UP:
                        self.movement[0] = True
                    if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        self.movement[1] = True
                    if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        self.movement[2] = True
                    if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        self.movement[3] = True


                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w or event.key == pygame.K_UP:
                        self.movement[0] = False
                    if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        self.movement[1] = False
                    if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        self.movement[2] = False
                    if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        self.movement[3] = False

            pygame.display.update()
            self.clock.tick(60)


Game().run()


