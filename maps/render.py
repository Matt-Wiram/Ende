import pygame, sys
import pytmx
from settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, surf, group):
        super().__init__(group)
        self.image = surf
        slef.rect = self.image.get_rect(top_left = pos)
        self.z = LAYERS['ground']
