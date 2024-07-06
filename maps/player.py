import pygame
from settings import *

class Player(pygame.sprite.Sprite):



    def __init__(self, pos, group):
        super().__init__(group)

        self.image = pygame.Surface((48, 96))
        self.image.fill("green")
        self.rect = self.image.get_rect(center = pos)
        self.z = LAYERS['main']

        #movement
        self.direction = pygame.math.Vector2()
        self.speed = 300
        self.pos = pygame.math.Vector2(self.rect.center)




    def input(self):
        keys = pygame.key.get_pressed()

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
