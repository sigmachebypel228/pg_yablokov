from all_colors import*
import random
import pygame
pygame.init()

size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Моя игра")
BACKGROUND = (135,206,235)
screen.fill(BACKGROUND)

snowflakes = []

for i in range(100):
    snowflake = pygame.Surface((50,50))
    snowflake.set_colorkey((0,0,0))
    pygame.draw.circle(snowflake, (255,255,255),(25,25),10)
    pygame.draw.line(snowflake, (255,255,255),(25,5),(25,45),5)
    pygame.draw.line(snowflake, (255,255,255),(5,25),(45,25),5)
    pygame.draw.line(snowflake, (255,255,255),(10,10),(40,40),5)
    pygame.draw.line(snowflake, (255,255,255),(10,40),(40,10),5)
    pos = [random.randint(0,800),random.randint(0,600)]
    screen.blit(snowflake, pos)
    snowflakes.append(pos)
print(snowflakes)

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
    screen.fill(BACKGROUND)
    for pos in snowflakes:
        pos[1]+=1
        if pos[1]> 600:
            pos[0] = random.randint(0,800)
            pos[1] = 0
        screen.blit(snowflake,pos)
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()