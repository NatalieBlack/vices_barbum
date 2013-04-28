from pygame import *
import pygame
import sys
class GameObject(object):
    def __init__(self, image, height, hspeed, vspeed):
        self.hor_speed = hspeed
        self.ver_speed = vspeed
        self.image = image
        self.pos = image.get_rect().move(0, height)
    def set_speed(self, x, y):
        self.hor_speed = x
        self.ver_speed = y
    def move(self):
        self.pos = self.pos.move(self.hor_speed, self.ver_speed)

class BackgroundSprite(pygame.sprite.Sprite):
    def __init__(self, img, xposition):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(img)

        self.rect = (xposition,0)

screen = pygame.display.set_mode((896, 480))
player = pygame.image.load('guitar_small.png')
tegan = BackgroundSprite('tegan.jpg', 0)
sara = BackgroundSprite('sara.jpg', 396)
backgrounds = pygame.sprite.Group(tegan, sara)
backgrounds.draw(screen)
o = GameObject(player, 40, 0, 0)
while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key  == pygame.K_j:
                o.set_speed(o.hor_speed, 20)
            if event.key  == pygame.K_k:
                o.set_speed(o.hor_speed,-20)
            if event.key  == pygame.K_h:
                o.set_speed(-20,o.ver_speed)
            if event.key  == pygame.K_l:
                o.set_speed(20,o.ver_speed)
        if event.type == pygame.KEYUP:
            o.set_speed(0,0)
    #screen.blit(tegan, o.pos, o.pos)
    o.move()
    screen.blit(o.image, o.pos)
    pygame.display.update()
    pygame.time.delay(100)
