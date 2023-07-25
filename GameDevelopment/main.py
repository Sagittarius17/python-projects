import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 1366
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pygame Game')

# Set up the clock
clock = pygame.time.Clock()

# Set up the player
player_x = 320
player_y = 400
player_speed = 5
player_image = pygame.image.load('Game Development/black.png').convert_alpha()

# Set up the enemy
enemy_x = random.randint(0, screen_width - 50)
enemy_y = 0
enemy_speed = 3
enemy_image = pygame.image.load('Game Development/red.png').convert_alpha()

# Set up the game loop
running = True
while running:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    elif keys[pygame.K_RIGHT]:
        player_x += player_speed

    # Move the enemy
    enemy_y += enemy_speed
    if enemy_y > screen_height:
        enemy_x = random.randint(0, screen_width - 50)
        enemy_y = 0

    # Check for collisions
    player_rect = pygame.Rect(player_x, player_y, 50, 50)
    enemy_rect = pygame.Rect(enemy_x, enemy_y, 50, 50)
    if player_rect.colliderect(enemy_rect):
        print('Game Over')
        running = False

    # Draw the game objects
    screen.fill((255, 255, 255))
    screen.blit(player_image, (player_x, player_y))
    screen.blit(enemy_image, (enemy_x, enemy_y))
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
