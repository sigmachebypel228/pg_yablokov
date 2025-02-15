
import random
from pygame.constants import *
from all_colors import *
import pygame
pygame.init()

rect = pygame.Rect(0,100,200,150)
size = (1280 , 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('My game')
Background = (255,255,255)
screen.fill(Background)
FPS = 60
clock = pygame.time.Clock()
speed = 5
running  = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    rect.x += speed




    if rect.x > screen.get_width():
        rect.x = -rect.width
    screen.fill(Background)

    pygame.draw.rect(screen, blue ,rect)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()