import pygame
import os

BASE_IMG_PATH = '/Users/carterlandstrom/Downloads/data/images/'

def load_image(path):
    img = pygame.image.load(BASE_IMG_PATH + path).convert()
    img.set_colorkey((0,0,0))
    return img

def load_images(path):
    images = []
    for ing_name in sorted(os.listdir(BASE_IMG_PATH + path)):
        images.append(load_image(path + '/'+ ing_name))
    return images
