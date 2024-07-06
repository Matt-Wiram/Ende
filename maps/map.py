import pygame, sys
import pytmx




class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,surf,groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft = pos)


pygame.init()
screen = pygame.display.set_mode((1025,1025))
tmxdata = pytmx.load_pygame('../maps/map1.tmx')
clock = pygame.time.Clock()
sprite_group = pygame.sprite.Group()

# cycle through all layers
for layer in tmxdata.visible_layers:
    # if layer.name in ('Floor', 'Plants and rocks', 'Pipes')
    if hasattr(layer,'data'):
        for x,y,surf in layer.tiles():
            # This gets tiles and distributes (0,0) to (1024, 1024) by 32
            pos = (x*96, y*96)



            Tile(pos = pos, surf = surf, groups = sprite_group)


image = tmxdata.get_layer_by_name('Floor')
# screen.blit(image, (0,0),32)
running = True
count = 0
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    sprite_group.draw(screen)
    player = pygame.draw.circle(screen, "red", player_pos, 40)
    speed = 150
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= speed * dt

    if keys[pygame.K_s]:
        player_pos.y += speed * dt

    if keys[pygame.K_a]:
        player_pos.x -= speed * dt

    if keys[pygame.K_d]:
        player_pos.x += speed * dt








    count +=1
    pygame.display.update()
    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.

    dt = clock.tick(120) / 1000
pygame.quit()

