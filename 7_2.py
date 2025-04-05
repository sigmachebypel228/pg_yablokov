from all_colors import *
import math
import pygame
pygame.init()
def distance(pos1,pos2):
    return math.sqrt((pos2[0] -pos1[0])**2 +(pos2[1] -pos1[1])**2 )
def move_towards(pos1, pos2, min_speed = 1, max_speed = 10):
    x1 ,y1 = pos1
    x2,y2 = pos2
    dx = x2-x1
    dy = y2-y1
    dist = distance(pos1,pos2)
    if dist < min_speed:
        return pos2
    if dist == 0:
        return pos1
    speed = max(min_speed, min(dist/5,max_speed))
    dx/=dist
    dy/=dist
    print(dx,dy)
    x1 +=dx * speed
    y1 += dy*speed
    return (x1,y1)
size = (640, 480)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Моя игра")

BACKGROUND = black
circle_color = white
circle_radius = 20
circle_pos = (320,240)
speed = 3
screen.fill(BACKGROUND)
FPS = 60
clock = pygame.time.Clock()
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    mouse_pos = pygame.mouse.get_pos()

    circle_pos = move_towards(circle_pos, mouse_pos, speed)

    #Отрисовка объектов
    screen.fill(BACKGROUND)
    pygame.draw.circle(screen, circle_color,(int(circle_pos[0]) ,int(circle_pos [1])),circle_radius)
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()