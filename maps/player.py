import math

import pygame
from settings import *

class Player(pygame.sprite.Sprite):



    def __init__(self, pos, group):
        super().__init__(group)

        self.image = pygame.Surface((48, 96))
        self.image.fill("green")
        self.rect = self.image.get_rect(center = pos)
        self.z = LAYERS['main']
        self.attackable = 1


        #movement
        self.direction = pygame.math.Vector2()
        self.speed = 300
        self.pos = pygame.math.Vector2(self.rect.center)





    def input(self):
        #keyboard controls
        keys = pygame.key.get_pressed()


 # mouse controls
        click = pygame.event.get(1025)

        if len(click) > 0:
            #Grabbing the x and y from coords becuase they are different from player pos
            x = click[0].pos[0]
            y = click[0].pos[1]
            self.target(x, y)





#keyboard controls
    # vertical axis
        if keys[pygame.K_w]:
            self.direction.y = -1
        elif keys[pygame.K_s]:
            self.direction.y = 1
        else:
    # horizantal axis
            self.direction.y = 0
        if keys[pygame.K_a]:
            self.direction.x = -1
        elif keys[pygame.K_d]:
            self.direction.x = 1
        else:
            self.direction.x = 0




    def target(self, x, y):
        print(x, y)
        #Figuring out the direction the click is facing
        x = x - SCREEN_WIDTH / 2
        y = y - SCREEN_HEIGHT / 2
        print(x, y)
        #Grabbing the distance from the player, all items in direction and distance of 150 can be changed to be dynamic
        distance = math.sqrt(x ** 2 + y ** 2)
        print(self.pos)
        print(distance)


    # Was working on this for direction of sprite player
        # if abs(x) > abs(y):
        #     direction =
        # elif abs(y) > abs(y):
        #     direction =
        # else:
        #     direction =





    def move(self, dt):
        #normalizing vector
        if self.direction.magnitude() > 0:

            self.direction = self.direction.normalize()
        #horizantal movement
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.centerx = self.pos.x

        #vertical movement
        self.pos.y += self.direction.y * self.speed * dt
        self.rect.centery = self.pos.y



    def update(self, dt):
        self.input()
        self.move(dt)
