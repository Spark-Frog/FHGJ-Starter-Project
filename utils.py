import pygame


BASE_IMG_PATH = '/Users/carterlandstrom/Downloads/data/images/' 
#For the BASE_IMG_PATH you will need to change it so it correctly directs to the files.
#Most likely using vs or vscode just put /data/images/ but since Macs are dumb I need the 
#extra stuff/
def load_image(path):
    img = pygame.image.load(BASE_IMG_PATH + path).convert()
    img.set_colorkey((0,0,0))
    return img
