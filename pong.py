#Controls:
# Left paddle: W/S
# Right paddle: Up/Down

import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
BALL_SIZE = 10
PADDLE_SPEED = 5
BALL_SPEED_X = 4
BALL_SPEED_Y = 4

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Paddle positions
left_paddle = pygame.Rect(10, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
right_paddle = pygame.Rect(WIDTH - 20, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

# Ball
ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, BALL_SIZE, BALL_SIZE)
ball_dx = BALL_SPEED_X
ball_dy = BALL_SPEED_Y

# Scores
left_score = 0
right_score = 0
font = pygame.font.Font(None, 74)

clock = pygame.time.Clock()

# Game state
running = True
game_started = False  # wait for click to begin

# Pre-render start message
start_font = pygame.font.Font(None, 50)
start_text = start_font.render("Click to Start", True, WHITE)
start_rect = start_text.get_rect(center=(WIDTH//2, HEIGHT//2))

# Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # start the game on mouse click
        if not game_started and event.type == pygame.MOUSEBUTTONDOWN:
            game_started = True
            ball_dx = BALL_SPEED_X
            ball_dy = BALL_SPEED_Y
    
    # Keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and left_paddle.top > 0:
        left_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_s] and left_paddle.bottom < HEIGHT:
        left_paddle.y += PADDLE_SPEED
    if keys[pygame.K_UP] and right_paddle.top > 0:
        right_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and right_paddle.bottom < HEIGHT:
        right_paddle.y += PADDLE_SPEED

    if game_started:
        # Move ball
        ball.x += ball_dx
        ball.y += ball_dy

        # Collisions with top/bottom
        if ball.top <= 0 or ball.bottom >= HEIGHT:
            ball_dy = -ball_dy

        # Paddle collisions
        if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
            ball_dx = -ball_dx

        # Scoring
        if ball.left <= 0:
            right_score += 1
            ball.center = (WIDTH // 2, HEIGHT // 2)
            ball_dx = -BALL_SPEED_X
        if ball.right >= WIDTH:
            left_score += 1
            ball.center = (WIDTH // 2, HEIGHT // 2)
            ball_dx = BALL_SPEED_X

    # Draw everything
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, left_paddle)
    pygame.draw.rect(screen, WHITE, right_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    left_text = font.render(str(left_score), True, WHITE)
    right_text = font.render(str(right_score), True, WHITE)
    screen.blit(left_text, (WIDTH // 4, 20))
    screen.blit(right_text, (WIDTH * 3 // 4, 20))

    # display start text if game not started
    if not game_started:
        screen.blit(start_text, start_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
