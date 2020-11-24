from pygame.locals import *
import pygame 
import time
import sys
pygame.init() 
FPS=30
fpsClock=pygame.time.Clock()

white = (255, 255, 255) 

X = 700
Y = 500

gameIcon = pygame.image.load('Game Icon.ico')

pygame.display.set_icon(gameIcon)
display_surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)


pygame.display.set_caption('Flat minecraft') 
 
image = pygame.image.load(r'loading.png') 
display_surface.fill(white) 
display_surface.blit(image, (-350, -200))
pygame.display.update()
time.sleep(2)
UP='up'
LEFT='left'
RIGHT='right'
DOWN='down'

sprite=pygame.image.load('Steve left.jpg')
spritex=200
spritey=389
direction=LEFT
background=pygame.image.load('bg.png')
while True:
    display_surface.blit(background,(0,-200))

    display_surface.blit(sprite,(spritex,spritey))

    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if (event.key == pygame.K_LEFT):
                sprite=pygame.image.load('Steve left.jpg')
            elif (event.key == pygame.K_RIGHT):
                sprite=pygame.image.load('Steve right.jpg')
    keys_pressed = pygame.key.get_pressed()

    if keys_pressed[pygame.K_LEFT]:
        spritex -= 5

    if keys_pressed[pygame.K_RIGHT]:
        spritex += 5


    pygame.display.update()
    fpsClock.tick(FPS)

