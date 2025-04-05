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
pacman_pos = (400,300)
speed = 3
pacman_images = {'up': pygame.image.load('resurse/pacman_up.png'),
                'down': pygame.image.load('resurse/pacman_down.png'),
                'left': pygame.image.load('resurse/pacman_left.png'),
                'right': pygame.image.load('resurse/pacman_right.png'),
                'up_left': pygame.image.load('resurse/pacman_up_left.png'),
                'up_right': pygame.image.load('resurse/pacman_up_right.png'),
                'down_left': pygame.image.load('resurse/pacman_down_left.png'),
                'down_right': pygame.image.load('resurse/pacman_down_right.png')}
def get_direction(pos1,pos2):
    dx = pos2[0] - pos1[0]
    dy = pos2[1] - pos1[1]
    direction = 'right'
    if dy <0:
        if dx<0:
            direction = 'up_left'
        elif dx>0:
            direction = 'up_right'
        else:
            direction = 'up'
    elif dy >0:
        if dx<0:
            direction = 'down_left'
        elif dx>0:
            direction = 'down_right'
        else:
            direction = 'down'
    else:

        if dx<0:
            direction = 'left'
        elif dx>0:
            direction = 'right'
    return direction



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
    direction = get_direction(pacman_pos,mouse_pos)
    pacman_pos = move_towards(pacman_pos, mouse_pos)

    #Отрисовка объектов
    screen.fill(BACKGROUND)
    pacman_image = pacman_images[direction]
    screen.blit(pacman_image , pacman_pos)
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()