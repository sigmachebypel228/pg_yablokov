from all_colors import *
import random
import pygame
import time

pygame.init()

size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('My game')
background_color = (255, 255, 255)
screen.fill(background_color)
fps = 60
clock = pygame.time.Clock()

width = screen.get_width() // 2
height = screen.get_height() // 2
colors = [red, green, blue, black]
running = True

# Оставляем исходный код без изменений
rect_size = 200


last_time = time.time()  # Время последнего обновления цветов

while running:
    current_time = time.time()
    if current_time - last_time >= 0.01:  # Каждые 0.01 секунду
        last_time = current_time

        # Обновление цветов для всех уже созданных квадратов
        rect_size = 200
        for i in range(30):
            rect = pygame.Rect(0, 0, rect_size, rect_size)
            rect.center = (width, height)
            pygame.draw.rect(screen, random.choice(colors), rect)
            rect_size -= 10

    pygame.display.flip()
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()