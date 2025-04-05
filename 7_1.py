from all_colors import *
import pygame
pygame.init()
def move_towards(pos1, pos2, speed):
    x1 ,y1 = pos1
    x2,y2 = pos2
    dx = x2-x1
    dy = y2-y1
    if abs(dx) > speed:
        if dx > 0 :
            x1 += speed
        else:
            x1-= speed
    else:
        x1 = x2
    if abs(dy) > speed:
        if dy > 0 :
            y1 += speed
        else:
            y1-= speed
    else:
        y1 = y2
    return (x1,y1)
size = (640, 480)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Моя игра")

BACKGROUND = black
circle_color = white
circle_radius = 20
circle_pos = (320,240)
speed = 30
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