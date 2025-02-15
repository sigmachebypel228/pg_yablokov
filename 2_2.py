import pygame
pygame.init()

size = (1280 , 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('My game')
Background = (255,255,255)
screen.fill(Background)
FPS = 60
clock = pygame.time.Clock()
red = (255,0,0)
x,y = 50,50
width,height = 100,100
speed = 5
running  = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print('НАжато вперед')
                y-= speed
                if y<0:
                    y = 0
            elif event.key == pygame.K_DOWN:
                print('нажато назад')
                y+= speed
                if y>720-height:
                    y = 720-height
            elif event.key == pygame.K_LEFT:
                print('нажато влево')
                x-= speed
                if x>0:
                    x = 0
            elif event.key == pygame.K_RIGHT:
                print('нажато вправо')
                x+= speed
                if x>1280-width:
                    x = 1280-width
            else:
                print(f'Нажали клавишу{event.key}')




    screen.fill(Background)
    pygame.draw.rect(screen,red,(x,y,width,height))
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()