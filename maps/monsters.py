import pygame
from settings import *



class Monster(pygame.sprite.Sprite):



    def __init__(self, pos, group, player):
        super().__init__(group)

        self.image = pygame.Surface((48, 96))
        self.image.fill("red")
        self.rect = self.image.get_rect(center = pos)
        self.z = LAYERS['main']
        self.attackable = 1

        self.player = player

        #movement
        self.direction = pygame.math.Vector2()
        self.speed = 200
        self.pos = pygame.math.Vector2(self.rect.center)




    def target(self):
        if self.player == None:
            self.direction = pygame.math.Vector2()
        else:
            pass

        # vertical axis
        if self.player.pos.y < self.pos.y:
            self.direction.y = -1
        elif self.player.pos.y > self.pos.y:
            self.direction.y = 1
        else:
            self.direction.y = 0

            # horizantal axis
        if self.player.pos.x < self.pos.x:
            self.direction.x = -1
        elif self.player.pos.x > self.pos.x:
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
        self.target()
        self.move(dt)
