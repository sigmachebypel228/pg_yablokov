import pygame
from all_colors import*
pygame.init()
size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Моя игра")
BACKGROUND = (255, 255, 255)

rect1 = pygame.Rect(100,100,200,150)
rect2 = pygame.Rect(250,150,200,150)
rect3 = pygame.Rect(500,100,200,150)
rect4 = pygame.Rect(600,300,200,150)
width = 5
screen.fill(BACKGROUND)
def collision(rect, other_rect):
    if rect.colliderect(other_rect):
        pygame.draw.rect(screen, red,rect,width)
        pygame.draw.rect(screen, red, other_rect, width)
    else:
        pygame.draw.rect(screen, blue, rect, width)
        pygame.draw.rect(screen, blue, other_rect, width)
collision(rect1, rect2)
collision(rect3, rect4)
FPS = 60
clock = pygame.time.Clock()
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #Основная логика
    #Отрисовка объектов

    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()