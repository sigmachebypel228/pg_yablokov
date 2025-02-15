import pygame
import random
from pygame.constants import *
from all_colors import*
pygame.init()

size = (1280 , 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('My game')
Background = (255,255,255)
screen.fill(Background)
FPS = 60
clock = pygame.time.Clock()
red = (255,0,0)
x,y = 50,50
width,height = 100,100
speed = 5
running  = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys= pygame.key.get_pressed()
    if keys[K_LEFT]:
        x -= speed
    if keys[K_RIGHT]:
        x += speed
    if keys[K_UP]:
        y -= speed
    if keys[K_DOWN]:
        y+= speed
    if y<0:
        y=0
        color = random.choice(colors)
        continue
    if y<720 - height:
        y = 720 - height
        color = random.choice(colors)
        continue
    if x<0:
        x=0
        color = random.choice(colors)
        continue
    if x< 1280+width:

        x = 1280 + width
        color = random.choice(colors)
        continue





    screen.fill(Background)
    pygame.draw.rect(screen,red,(x,y,width,height))
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()