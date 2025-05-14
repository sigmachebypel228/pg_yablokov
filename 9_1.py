import pygame
from all_colors import *

# Инициализация Pygame
pygame.init()

# Настройки экрана
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Рисование")
clock = pygame.time.Clock()

# Настройки кисти
BACKGROUND = (255, 255, 255)
brush_color = (0, 0, 0)
brush_width = 5
canvas = pygame.Surface(screen.get_size())
canvas.fill(BACKGROUND)

# Настройки палитры
dragging_pallete = False
border_color = (0, 0, 0)
cur_index = 0
color_size = 50
pallete_rect = pygame.Rect(10, 10, color_size * 12, color_size)
pallete = pygame.Surface(pallete_rect.size)

# Настройки прямоугольников
drawing_rect = False
start_pos = None
rect_color = red
fill_rect = False
current_rects = []  # Список для хранения нарисованных прямоугольников


def draw_pallete():
    pallete.fill(BACKGROUND)
    for i in range(12):
        color_rect = pygame.Rect(i * color_size, 0, color_size, color_size)
        pygame.draw.rect(pallete, colors[i], color_rect)
    border_rect = pygame.Rect(cur_index * color_size, 0, color_size, color_size)
    pygame.draw.rect(pallete, border_color, border_rect, width=3)
    screen.blit(pallete, pallete_rect.topleft)


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Обработка палитры цветов и рисования
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:  # Правая кнопка мыши - начало рисования прямоугольника
                drawing_rect = True
                start_pos = event.pos
            elif event.button == 1:  # Левая кнопка мыши - рисование кистью или выбор цвета
                if pallete_rect.collidepoint(event.pos):
                    selected_color_index = ((event.pos[0] - pallete_rect.left) // color_size)
                    cur_index = selected_color_index
                    brush_color = colors[cur_index]
                    rect_color = colors[cur_index]
                else:
                    # Запоминаем начальную позицию для рисования кистью
                    last_mouse_pos = event.pos

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 3 and drawing_rect:  # Правая кнопка мыши - завершение прямоугольника
                drawing_rect = False
                end_pos = event.pos
                rect_width = end_pos[0] - start_pos[0]
                rect_height = end_pos[1] - start_pos[1]
                if rect_width != 0 and rect_height != 0:  # Не добавляем нулевые прямоугольники
                    rect = pygame.Rect(start_pos[0], start_pos[1], rect_width, rect_height)
                    current_rects.append((rect, rect_color, fill_rect))
            elif event.button == 1:  # Левая кнопка мыши - перемещение палитры
                dragging_pallete = False

        elif event.type == pygame.MOUSEMOTION:
            if pygame.mouse.get_pressed()[2]:  # Движение с зажатой ПКМ - рисование прямоугольника
                pass  # Обрабатывается в основном цикле
            elif pygame.mouse.get_pressed()[0]:  # Движение с зажатой ЛКМ - рисование кистью
                if not pallete_rect.collidepoint(event.pos):
                    pygame.draw.circle(canvas, brush_color, event.pos, brush_width)
            elif dragging_pallete:  # Перемещение палитры
                pallete_rect.x = event.pos[0] - pallete_rect.width / 2
                pallete_rect.y = event.pos[1] - pallete_rect.height / 2

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                fill_rect = not fill_rect
            elif event.key == pygame.K_c:
                canvas.fill(BACKGROUND)  # Очистка холста
                current_rects = []  # Очистка списка прямоугольников

    # Отрисовка
    screen.blit(canvas, (0, 0))

    # Отрисовка всех сохраненных прямоугольников
    for rect, color, fill in current_rects:
        pygame.draw.rect(screen, color, rect, width=0 if fill else 1)

    # Отрисовка текущего прямоугольника (если рисуем)
    if drawing_rect:
        current_pos = pygame.mouse.get_pos()
        rect_width = current_pos[0] - start_pos[0]
        rect_height = current_pos[1] - start_pos[1]
        rect = pygame.Rect(start_pos[0], start_pos[1], rect_width, rect_height)
        pygame.draw.rect(screen, rect_color, rect, width=0 if fill_rect else 1)

    draw_pallete()

    # Отображение информации
    font = pygame.font.SysFont(None, 24)
    fill_text = font.render(f"Заливка: {'Вкл (SPACE)' if fill_rect else 'Выкл (SPACE)'}", True, (0, 0, 0))
    clear_text = font.render("Очистить: C", True, (0, 0, 0))
    help_text = font.render("ЛКМ: рисовать кистью | ПКМ: рисовать прямоугольник", True, (0, 0, 0))
    screen.blit(fill_text, (SCREEN_WIDTH - 250, 10))
    screen.blit(clear_text, (SCREEN_WIDTH - 250, 40))
    screen.blit(help_text, (10, SCREEN_HEIGHT - 30))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()