import pygame
import sys

pygame.init()

WIDTH = 800
HEIGHT = 600

WHITE = (255, 255, 255)
BLUE = (0, 191, 255)

SPEED = 5

ball_speed_x = 4
ball_speed_y = 4

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Ping Pong Game')

player1_rect = pygame.Rect(50, HEIGHT // 2 - 50, 20, 100)
player2_rect = pygame.Rect(WIDTH - 70, HEIGHT // 2 - 50, 20, 100)
ball_rect = pygame.Rect(385, 285, 30, 30)

player1_score = 0
player2_score = 0

font = pygame.font.Font(None, 74)
winner_font = pygame.font.Font(None, 100)

clock = pygame.time.Clock()

def display_score():
    player1_score_text = font.render(str(player1_score), True, WHITE)
    player2_score_text = font.render(str(player2_score), True, WHITE)
    screen.blit(player1_score_text, (200, 10))
    screen.blit(player2_score_text, (600, 10))

def display_winner(winner_text):
    text = winner_font.render(winner_text, True, WHITE)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text, text_rect)
    pygame.display.flip()
    pygame.time.delay(3000)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_w] and player1_rect.top > 0:
        player1_rect.y -= SPEED
    if keys[pygame.K_s] and player1_rect.bottom < HEIGHT:
        player1_rect.y += SPEED

    if keys[pygame.K_UP] and player2_rect.top > 0:
        player2_rect.y -= SPEED
    if keys[pygame.K_DOWN] and player2_rect.bottom < HEIGHT:
        player2_rect.y += SPEED
    
    ball_rect.x += ball_speed_x
    ball_rect.y += ball_speed_y

    if ball_rect.top <= 0 or ball_rect.bottom >= HEIGHT:
        ball_speed_y = -ball_speed_y

    if ball_rect.colliderect(player1_rect) or ball_rect.colliderect(player2_rect):
        ball_speed_x = -ball_speed_x

    
    if ball_rect.left <= 0:
        player2_score += 1
        ball_rect.center = (WIDTH // 2, HEIGHT // 2)
        ball_speed_x = -ball_speed_x
    if ball_rect.right >= WIDTH:
        player1_score += 1
        ball_rect.center = (WIDTH // 2, HEIGHT // 2)
        ball_speed_x = -ball_speed_x

    if player1_score >= 10:
        display_winner("Player 1 Wins!")
        running = False
    if player2_score >= 10:
        display_winner("Player 2 Wins!")
        running = False

    screen.fill(BLUE)

    pygame.draw.rect(screen, WHITE, player1_rect)
    pygame.draw.rect(screen, WHITE, player2_rect)
    pygame.draw.ellipse(screen, WHITE, ball_rect)
    
    display_score()

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()