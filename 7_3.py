import pygame
import random
import time

# Инициализируем Pygame
pygame.init()

# Размеры окна
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pac-Man')

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 215, 0)
RED = (255, 0, 0)

# Загрузка изображений Pac-Man'а
PACMAN_IMAGES = {
    'up': pygame.image.load('resurse/pacman_up.png'),
    'down': pygame.image.load('resurse/pacman_down.png'),
    'left': pygame.image.load('resurse/pacman_left.png'),
    'right': pygame.image.load('resurse/pacman_right.png'),
    'up_left': pygame.image.load('resurse/pacman_up_left.png'),
    'up_right': pygame.image.load('resurse/pacman_up_right.png'),
    'down_left': pygame.image.load('resurse/pacman_down_left.png'),
    'down_right': pygame.image.load('resurse/pacman_down_right.png')
}

# Класс Dot (точка)
class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 5
        self.color = YELLOW
        self.rect = pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.radius)

# Класс Pac-Man
class PacMan:
    def __init__(self):
        self.x, self.y = WIDTH // 2, HEIGHT // 2
        self.speed = 4
        self.direction = 'right'
        self.image = PACMAN_IMAGES[self.direction]
        self.rect = pygame.Rect(self.x - 16, self.y - 16, 32, 32)  # Хитбокс Пак-Мэна

    def update(self, mouse_pos):
        self.direction = self.get_direction(mouse_pos)
        self.move_towards(mouse_pos)
        self.image = PACMAN_IMAGES[self.direction]
        self.rect = pygame.Rect(self.x - 16, self.y - 16, 32, 32)  # Обновляем хитбокс

    def draw(self, surface):
        surface.blit(self.image, (self.x - 16, self.y - 16))  # Центрирование изображения

    def get_direction(self, target_pos):
        dx = target_pos[0] - self.x
        dy = target_pos[1] - self.y

        if abs(dx) > abs(dy):
            return 'right' if dx > 0 else 'left'
        else:
            return 'down' if dy > 0 else 'up'

    def move_towards(self, target_pos):
        x1, y1 = self.x, self.y
        x2, y2 = target_pos
        dx = x2 - x1
        dy = y2 - y1

        if abs(dx) > self.speed:
            self.x += self.speed if dx > 0 else -self.speed
        elif abs(dx) <= self.speed:
            self.x = x2

        if abs(dy) > self.speed:
            self.y += self.speed if dy > 0 else -self.speed
        elif abs(dy) <= self.speed:
            self.y = y2

# Основная функция игры
def main():
    global SCREEN, WIDTH, HEIGHT
    clock = pygame.time.Clock()
    fps = 60

    # Создаем Pac-Man
    pac_man = PacMan()

    # Список точек
    dots = []
    for _ in range(20):
        x = random.randint(50, WIDTH - 50)
        y = random.randint(50, HEIGHT - 50)
        dots.append(Dot(x, y))

    # Таймер и счетчик очков
    score = 0
    timer = 10  # Время до следующей точки
    start_time = time.time()

    running = True
    game_over = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Обновляем положение Pac-Man'а
        mouse_pos = pygame.mouse.get_pos()
        pac_man.update(mouse_pos)

        # Проверяем столкновения с точками
        for dot in dots[:]:
            if pac_man.rect.colliderect(dot.rect):
                dots.remove(dot)
                score += 1
                timer -= 1  # Уменьшаем таймер на 1 секунду
                break  # Едим одну точку за раз

        # Если время вышло, показываем экран поражения
        current_time = time.time()
        elapsed_time = current_time - start_time
        if elapsed_time >= timer:
            game_over = True
            running = False

        # Рисуем фон и объекты
        SCREEN.fill(BLACK)
        for dot in dots:
            dot.draw(SCREEN)
        pac_man.draw(SCREEN)

        # Показываем счетчик очков
        font = pygame.font.SysFont(None, 48)
        text = font.render(f'Score: {score}', True, WHITE)
        SCREEN.blit(text, (10, 10))

        # Отображаем таймер
        timer_text = font.render(f'Timer: {timer:.2f}', True, WHITE)
        SCREEN.blit(timer_text, (WIDTH - 150, 10))

        # Обновление экрана
        pygame.display.flip()
        clock.tick(fps)

    # Экран поражения
    if game_over:
        SCREEN.fill(BLACK)
        font = pygame.font.SysFont(None, 72)
        game_over_text = font.render('Game Over', True, RED)
        score_text = font.render(f'You scored: {score}', True, WHITE)
        SCREEN.blit(game_over_text, (WIDTH//2 - game_over_text.get_width()//2, HEIGHT//2 - 100))
        SCREEN.blit(score_text, (WIDTH//2 - score_text.get_width()//2, HEIGHT//2))
        pygame.display.flip()
        pygame.time.wait(5000)  # Ждем 5 секунд перед выходом

    pygame.quit()

# Запуск игры
main()