import sys

import pygame

from data.utils import load_image #type: ignore

from data.entities import PhysicsEntity #type: ignore


class Game:
    def __init__(self):
        
        pygame.init()

        pygame.display.set_caption("JWLC Game")

        self.screen = pygame.display.set_mode((640,480))

        self.clock = pygame.time.Clock()

        self.ing_pos = [160,260]

        self.movement = [False, False, False, False]

        self.assests= {
            'player' : load_image('entities/player.png')

        }

        self.player = PhysicsEntity(self, 'player', (50,50), (8,15))

    def run(self):
        while True:
            self.screen.fill((0,0,0))

            self.player.update((self.movement[1]-self.movement[0], 0))
            self.player.rendering(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        self.movement[0] = True
                    if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        self.movement[1] = True


                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        self.movement[0] = False
                    if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        self.movement[1] = False


            pygame.display.update()
            self.clock.tick(60)


Game().run()


