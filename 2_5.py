from all_colors import *
import pygame
pygame.init()


size = (1280 , 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('My game')
Background = (255,255,255)
screen.fill(Background)
FPS = 60
clock = pygame.time.Clock()
x = 0
y = 0
rect2_size = 100
rect_size = 200
color = [red,green,blue,black]
running  = True
# rect1 = pygame.Rect(x,y,rect_size,rect_size)
# rect1.center = (screen.get_width() //2,screen.get_height() //2)
# pygame.draw.rect(screen,black,rect1)
# rect2 = pygame.Rect(x,y,rect2_size,rect2_size)
# rect2.center = (screen.get_width() //2,screen.get_height( )//2)
# pygame.draw.rect(screen,red,rect2)

for i in range(4):
    rect1 = pygame.Rect(x,y,rect_size,rect_size)
    rect1.center = (screen.get_width() //2,screen.get_height() //2)
    pygame.draw.rect(screen,color[i],rect1)
    rect2 = pygame.Rect(x,y,rect2_size,rect2_size)
    rect2.center = (screen.get_width() //2,screen.get_height() // 2)
    pygame.draw.rect(screen,red,rect2)
    x += 100
    y += 100
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()