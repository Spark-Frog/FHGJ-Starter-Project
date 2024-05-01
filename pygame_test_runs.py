import sys

import pygame

from data.utils import load_image, load_images #type: ignore
from data.entities import PhysicsEntity #type: ignore
from data.tilemap import Tilemap #type: ignore
from data.clouds import Clouds #type: ignore

class Game:
    def __init__(self):
        
        pygame.init()

        pygame.display.set_caption("fghj")

        self.screen = pygame.display.set_mode((640,480))

        self.display = pygame.Surface((320,240))

        self.clock = pygame.time.Clock()

        self.ing_pos = [160,260]

        self.movement = [False, False]

        self.assests= {
            'decor' : load_images('tiles/decor'),
            'grass' : load_images('tiles/grass'),
            'large_decor' : load_images('tiles/large_decor'),
            'stone' : load_images('tiles/stone'),
            'player' : load_image('entities/player.png'),
            'background' : load_image('background.png'),
            'clouds' : load_images('clouds'),

        }

        #print(self.assests) Use to check assests
        self.clouds = Clouds(self.assests['clouds'], count = 16)

        self.player = PhysicsEntity(self, 'player', (50,50), (8,15))

        self.tilemap = Tilemap(self, tile_size=16)


        self.scroll = [0, 0]

    def run(self):
        while True:
            self.display.blit(self.assests['background'], (0,0))

            self.scroll[0] += (self.player.rect().centerx - self.display.get_width()/2- self.scroll[0]) / 10
            self.scroll[1] += (self.player.rect().centery - self.display.get_height()/2- self.scroll[1]) / 20
            render_scroll = (int(self.scroll[0]), int(self.scroll[1]))


            self.clouds.update()
            self.clouds.render(self.display , offset =render_scroll)

            self.tilemap.render(self.display, offset = render_scroll)

            self.player.update(self.tilemap, (self.movement[1]-self.movement[0], 0))
            self.player.rendering(self.display, offset = render_scroll)


            #print(self.tilemap.physics_rects_around(self.player.pos))


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        self.movement[0] = True
                    if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        self.movement[1] = True
                    if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                        self.player.velocity[1] = -3


                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        self.movement[0] = False
                    if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        self.movement[1] = False


            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()),(0,0))
            pygame.display.update()
            self.clock.tick(60)


Game().run()
