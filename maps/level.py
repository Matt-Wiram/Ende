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

        for layer in ['floor']:
            for x, y, surf in tmx_data.get_layer_by_name(layer).tiles():

                #This is where im making floor tiles and objects like chests




                Generic((x * TILE_SIZE, y * TILE_SIZE), surf, self.all_sprites, LAYERS[layer])
                 #####



        for obj in tmx_data.objects:
            layers = LAYERS['items']



            # print(obj.visible)
            # # <TiledObject[11]: "wood_chest_unopened">
            #
            # print(obj.type)
            # # furniture
            #
            # print(obj.image)
            # # <Surface(150x140x32 SW)>
            #
            # print(dir(obj.image))
            # # ['__class__', '__copy__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_pixels_address', 'blit', 'blits', 'convert', 'convert_alpha', 'copy', 'fill', 'get_abs_offset', 'get_abs_parent', 'get_alpha', 'get_at', 'get_at_mapped', 'get_bitsize', 'get_blendmode', 'get_bounding_rect', 'get_buffer', 'get_bytesize', 'get_clip', 'get_colorkey', 'get_flags', 'get_height', 'get_locked', 'get_locks', 'get_losses', 'get_masks', 'get_offset', 'get_palette', 'get_palette_at', 'get_parent', 'get_pitch', 'get_rect', 'get_shifts', 'get_size', 'get_view', 'get_width', 'lock', 'map_rgb', 'mustlock', 'premul_alpha', 'scroll', 'set_alpha', 'set_at', 'set_clip', 'set_colorkey', 'set_masks', 'set_palette', 'set_palette_at', 'set_shifts', 'subsurface', 'unlock', 'unmap_rgb']


            if not obj.visible:
                layers = LAYERS['invisible']
                print("Halp")

            if obj.type == 'furniture':
                Furniture((obj.x, obj.y), obj.image, self.all_sprites, layers)


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

