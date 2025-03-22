#добавить звуки            2    при отскоке от ракетки увеличиваеться скорость    3  ограничить скороость     добавить табло скоорости          т  выход
from all_colors import *
import pygame
import sys
pygame.init()

SCR_WIDTH = 1280
SCR_HEIGHT = 720
screen = pygame.display.set_mode([SCR_WIDTH, SCR_HEIGHT])
pygame.display.set_caption("Пинг-понг")



PADDLE_WIDTH = 25
PADDLE_HEIGHT = 100
PADDLE_SPEED = 10

BALL_SIZE = 20
BALL_SPEED_X = 5
BALL_SPEED_Y = 5


paddle_1_rect = pygame.Rect(0, SCR_HEIGHT//2 - PADDLE_HEIGHT//2,
                            PADDLE_WIDTH, PADDLE_HEIGHT)

paddle_2_rect = pygame.Rect(SCR_WIDTH - PADDLE_WIDTH,
                            SCR_HEIGHT//2 - PADDLE_HEIGHT//2,
                            PADDLE_WIDTH, PADDLE_HEIGHT)

ball_rect = pygame.Rect(SCR_WIDTH//2 - BALL_SIZE//2,
                            SCR_HEIGHT//2 - BALL_SIZE//2, BALL_SIZE, BALL_SIZE)

score_1 = 0
score_2 = 0
font = pygame.font.SysFont(None, 32)
ai_mode = True
if len(sys.argv) >1:
    if sys.argv[1] == '--human':
        ai_mode = False
def update_ai():
    if ball_rect.x > SCR_WIDTH // 2:
        if ball_rect.centery < paddle_2_rect.centery:
            paddle_2_rect.y -= PADDLE_SPEED
        elif ball_rect.centery > paddle_2_rect.centery:
            paddle_2_rect.y += PADDLE_SPEED
        if paddle_2_rect.top < 0:
            paddle_2_rect.top = 0
        if paddle_2_rect.bottom > SCR_HEIGHT:
            paddle_2_rect.top = SCR_HEIGHT
    else:

        paddle_2_rect.centery += (SCR_HEIGHT // 2 - paddle_2_rect.centery) / PADDLE_SPEED


BACKGROUND = black
screen.fill(BACKGROUND)
FPS = 60
clock = pygame.time.Clock()
running = True
ai_mode = True





while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddle_1_rect.y -= PADDLE_SPEED
        if paddle_1_rect.top <=0:
            paddle_1_rect.top = 0
    if keys[pygame.K_s]:
        paddle_1_rect.y += PADDLE_SPEED
        if paddle_1_rect.bottom >= SCR_HEIGHT:
            paddle_1_rect.bottom = SCR_HEIGHT
    if keys[pygame.K_UP]:
        paddle_2_rect.y -= PADDLE_SPEED
        if paddle_2_rect.top <=0:
            paddle_2_rect.top = 0
    if keys[pygame.K_DOWN]:
        paddle_2_rect.y += PADDLE_SPEED
        if paddle_2_rect.bottom >= SCR_HEIGHT:
            paddle_2_rect.bottom = SCR_HEIGHT
    ball_rect.x += BALL_SPEED_X
    ball_rect.y += BALL_SPEED_Y
    if ball_rect.top <=0 or ball_rect.bottom >= SCR_HEIGHT:
        BALL_SPEED_Y *=-1



#если поверхность мяча столкуналась с поверхностью первой ракетки или поверхность мяча столкнулась с поверхностью второй ракетки : скорость мяча по оси икс умножить  на -1

    if ball_rect.colliderect(paddle_1_rect) or ball_rect.colliderect(paddle_2_rect):
        BALL_SPEED_X *=-1
    if ball_rect.left <=0:
        ball_rect = pygame.Rect(SCR_WIDTH // 2 - BALL_SIZE // 2,
                                SCR_HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
        score_2 +=1
    if ball_rect.right >=SCR_WIDTH:
        ball_rect = pygame.Rect(SCR_WIDTH // 2 - BALL_SIZE // 2,
                                SCR_HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
        score_1 +=1
    if ai_mode ==True:
        update_ai()

    #Основная логика
    #Отрисовка объектов
    screen.fill(BACKGROUND)

    pygame.draw.rect(screen, white, paddle_1_rect)
    pygame.draw.rect(screen, white, paddle_2_rect)
    pygame.draw.ellipse(screen, white, ball_rect)
    pygame.draw.line(screen, white, (SCR_WIDTH//2, 0), (SCR_WIDTH//2, SCR_HEIGHT), 5)
    score_text = font.render(f'{score_1} : {score_2}', True , white)
    screen.blit(score_text,( SCR_WIDTH // 2 - score_text.get_width()// 2,10))
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()