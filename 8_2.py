from all_colors import*
import pygame
pygame.init()
size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Рисование линии")
BACKGROUND = (0,0,0)
screen.fill(BACKGROUND)
points = []
line_color = (255,255,255)
preview_color = (192,192,192)
show_preview = True
FPS = 60
clock = pygame.time.Clock()
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1:
                points.append(event.pos)
            elif event.button ==2:
                points = []
            elif event.button ==3:
                show_preview = not show_preview





    #Основная логика
    #Отрисовка объектов
    screen.fill(BACKGROUND)
    for i in range(len(points) - 1):
        start_pos = points[i]
        end_pos = points[i+1]
        pygame.draw.line(screen,line_color,start_pos,end_pos,3)
    if len(points)>1 and show_preview:
        last_point = points[i]
        mouse_pos = pygame.mouse.get_pos()
        pygame.draw.line(screen,preview_color,mouse_pos,last_point,1)
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()