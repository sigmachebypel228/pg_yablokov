import pygame
from all_colors import*
pygame.init()
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Моя игра")
BACKGROUND = (255, 255, 255)
brush_color = (0,0,0)
brush_width = 5
dragging_pallete = False
border_color = (0,0,0)
cur_index = 0
canvas = pygame.Surface(screen.get_size())
canvas.fill(BACKGROUND)
size = 50
pallete_rect = pygame.Rect(10,10,size*12,size)
pallete = pygame.Surface(pallete_rect.size)
def draw_pallete():

    pallete.fill(BACKGROUND)
    for i in range(12):
        color_rect = pygame.Rect(i*size,0,size,size)
        pygame.draw.rect(pallete,colors[i],color_rect)
    border_rect = pygame.Rect(cur_index * size,0,size,size)
    pygame.draw.rect(pallete,border_color,border_rect,width = 3)
    screen.blit(pallete,pallete_rect.topleft)
FPS = 60
clock = pygame.time.Clock()
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            if pallete_rect.collidepoint(event.pos):

                print(' потащили ')
                dragging_pallete = True
                offset = (event.pos[0] - pallete_rect.left,event.pos[1] - pallete_rect.top)
            else:
                print('не тащим')
                dragging_pallete = False

        elif event.type == pygame.MOUSEBUTTONUP and event.button == 3:
            print ('не тащим')
            dragging_pallete = False


    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()
    if mouse_pressed[0]:
        if pallete_rect.collidepoint(mouse_pos):
            selected_color_index = ((mouse_pos[0] - pallete_rect.left) // size)
            cur_index = selected_color_index
            brush_color = colors[cur_index]
        else:
            pygame.draw.circle(canvas,brush_color,mouse_pos,brush_width)
    if dragging_pallete:
        new_pos = (mouse_pos[0] - offset[0],mouse_pos[1] - offset[1])
        d


    #Отрисовка объектов

    screen.blit(canvas, (0,0))
    draw_pallete()
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()