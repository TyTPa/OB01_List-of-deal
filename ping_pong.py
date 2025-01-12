
#"Пинг-Понг":

import pygame
import sys

# Константы
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
BALL_SIZE = 15
PADDLE_SPEED = 10
BALL_SPEED_X, BALL_SPEED_Y = 5, 5

class Paddle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, PADDLE_WIDTH, PADDLE_HEIGHT)

    def move(self, direction):
        if direction == 'up' and self.rect.top > 0:
            self.rect.y -= PADDLE_SPEED
        if direction == 'down' and self.rect.bottom < HEIGHT:
            self.rect.y += PADDLE_SPEED

    def draw(self, surface):
        pygame.draw.rect(surface, WHITE, self.rect)

class Ball:
    def __init__(self):
        self.rect = pygame.Rect(WIDTH // 2, HEIGHT // 2, BALL_SIZE, BALL_SIZE)
        self.speed_x = BALL_SPEED_X
        self.speed_y = BALL_SPEED_Y

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.speed_y = -self.speed_y

    def reset(self):
        self.rect.x = WIDTH // 2
        self.rect.y = HEIGHT // 2
        self.speed_x = BALL_SPEED_X * (-1 if self.speed_x > 0 else 1)

    def draw(self, surface):
        pygame.draw.ellipse(surface, WHITE, self.rect)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Пинг-Понг")
    clock = pygame.time.Clock()

    left_paddle = Paddle(30, HEIGHT // 2 - PADDLE_HEIGHT // 2)
    right_paddle = Paddle(WIDTH - 40, HEIGHT // 2 - PADDLE_HEIGHT // 2)
    ball = Ball()

    # Счет
    left_score = 0
    right_score = 0
    font = pygame.font.Font(None, 74)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            left_paddle.move('up')
        if keys[pygame.K_s]:
            left_paddle.move('down')
        if keys[pygame.K_UP]:
            right_paddle.move('up')
        if keys[pygame.K_DOWN]:
            right_paddle.move('down')

        ball.move()

        # Проверка столкновений с ракетками
        if ball.rect.colliderect(left_paddle.rect) or ball.rect.colliderect(right_paddle.rect):
            ball.speed_x = -ball.speed_x

        # Проверка выхода за границы
        if ball.rect.left <= 0:
            right_score += 1  # Правый игрок получает очко
            ball.reset()
        if ball.rect.right >= WIDTH:
            left_score += 1  # Левый игрок получает очко
            ball.reset()

        screen.fill(BLACK)
        left_paddle.draw(screen)
        right_paddle.draw(screen)
        ball.draw(screen)

        # Отображение счета
        score_text = font.render(f"{left_score} : {right_score}", True, WHITE)
        screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 20))

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
        main()
### Как играть:
#- Игрок слева управляет ракеткой с помощью клавиш W (вверх) и S (вниз).
#- Игрок справа управляет ракеткой с помощью стрелок вверх и вниз.

