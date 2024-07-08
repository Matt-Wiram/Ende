import math
import random

import pygame
from settings import *
from player import Player
from sprites import Generic
from sprites import Furniture
from pytmx.util_pygame import load_pygame
from monsters import Monster

class Level:

    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        self.all_sprites = CameraGroup()
        # self.monster_sprites = MonsterGroup()
        self.setup()




    # for setting up map and tiles along with objects and walls
    def setup(self):
    # This is where you change map
        tmx_data = load_pygame('map1.tmx')

        for layer in ['ground']:
            for x, y, surf in tmx_data.get_layer_by_name(layer).tiles():

                #This is where im making floor tiles and objects like chests




                Generic((x * TILE_SIZE, y * TILE_SIZE), surf, self.all_sprites, LAYERS[layer])
                 #####



        for obj in tmx_data.objects:
            print(obj)
            print(obj.template)
            print(obj.image)
            print(dir(obj.image))


            # Furniture((obj.x +130, obj.y +130), obj.image, self.all_sprites, LAYERS[item])


        self.player = Player((SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2), self.all_sprites)

     # #Monster set up and spawn and probably add to all.sprites and camera group
        # ran = random.randint(0, 1000)
        # if ran > 998:
        #     pass
        # else:
        #     monster = Monster((ran // 10, ran // 10), self.monster_sprites, self.player)

    def run(self, dt):
        self.display_surface.fill("black")


        #Display player sprite and background
        self.all_sprites.customize_draw(self.player)

        # #display monsters and background
        # self.monster_sprites.customize_draw(self)
        #
        #
        self.all_sprites.update(dt)
        # self.monster_sprites.update(dt)



# class MonsterGroup(pygame.sprite.Group):
# # Radius of 4 * 96 to draw and set up as a boolean
#
#     def __init__(self):
#         super().__init__()
#         self.display_surface = pygame.display.get_surface()
#         self.rectangle = pygame.display.get_surface().get_rect()
#
#
#     def customize_draw(self, monster):
#         # Radius of 4 * 96 to draw and set up as a boolean
#
#         for layer in LAYERS.values():
#
#             for sprite in self.sprites():
#                 pos = sprite.rect.center
#                 vicinity = math.sqrt((monster.player.pos.x - pos[0]) ** 2 + (monster.player.pos.y - pos[1]) ** 2) < SCREEN_HEIGHT / 2
#                 if vicinity:
#                     sprite.z = LAYERS['main']
#                     self.display_surface.blit(sprite.image, self.rectangle)
#
#                 else:
#                     sprite.z = LAYERS['water']
#


class CameraGroup(pygame.sprite.Group):

    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()

    def customize_draw(self, player):
        self.offset.x = player.rect.centerx - SCREEN_WIDTH / 2
        self.offset.y = player.rect.centery - SCREEN_HEIGHT / 2

        for layer in LAYERS.values():

            for sprite in self.sprites():
                if sprite.z == layer:
                    offset_rect = sprite.rect.copy()
                    offset_rect.center -= self.offset
                    self.display_surface.blit(sprite.image, offset_rect)

