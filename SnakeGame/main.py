import pygame
import random

# Initialize pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Game dimensions
WIDTH, HEIGHT = 640, 480
CELL_SIZE = 15

# Loading bar for super food
LOADING_BAR_WIDTH = 100  # Initial width for full lifespan
LOADING_BAR_HEIGHT = 2  # Height of the loading bar
LOADING_BAR_COLOR = WHITE  # White color

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

pygame.font.init()
font = pygame.font.SysFont(None, 35)

# Directions
LEFT = (-1, 0)
RIGHT = (1, 0)
UP = (0, -1)
DOWN = (0, 1)

class Snake:
    def __init__(self):
        self.body = [(5, 5), (4, 5), (3, 5)]
        self.direction = RIGHT

    def move(self):
        head_x, head_y = self.body[0]
        new_dir_x, new_dir_y = self.direction
        new_head = ((head_x + new_dir_x) % (WIDTH // CELL_SIZE), (head_y + new_dir_y) % (HEIGHT // CELL_SIZE))
        self.body = [new_head] + self.body[:-1]

    def grow(self):
        head_x, head_y = self.body[0]
        new_dir_x, new_dir_y = self.direction
        new_head = ((head_x + new_dir_x) % (WIDTH // CELL_SIZE), (head_y + new_dir_y) % (HEIGHT // CELL_SIZE))
        self.body = [new_head] + self.body

    def collide(self):
        return self.body[0] in self.body[1:]

def draw_snake(snake):
    for segment in snake.body:
        pygame.draw.rect(screen, GREEN, (segment[0] * CELL_SIZE, segment[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        
def display_score(score):
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

def main():
    score = 0
    snake = Snake()
    food = (random.randint(0, (WIDTH // CELL_SIZE) - 1), random.randint(0, (HEIGHT // CELL_SIZE) - 1))
    super_food = None  # Initially, no super food
    super_food_timer = 0
    clock = pygame.time.Clock()
    running = True

    while running:
        screen.fill(BLACK)
        
        # score = len(snake.body) - 3  # initial snake length is 3
        display_score(score)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and snake.direction != RIGHT:
                    snake.direction = LEFT
                if event.key == pygame.K_RIGHT and snake.direction != LEFT:
                    snake.direction = RIGHT
                if event.key == pygame.K_UP and snake.direction != DOWN:
                    snake.direction = UP
                if event.key == pygame.K_DOWN and snake.direction != UP:
                    snake.direction = DOWN

        snake.move()

        # Check if snake ate the food
        if snake.body[0] == food:
            snake.grow()
            score += 1
            food = (random.randint(0, (WIDTH // CELL_SIZE) - 1), random.randint(0, (HEIGHT // CELL_SIZE) - 1))
            
        # Handle super food
        if super_food and snake.body[0] == super_food:
            score += super_food_timer
            snake.grow()
            super_food = None

        # Randomly spawn super food
        if not super_food and random.random() < 0.02:  # 2% chance to spawn super food each frame
            super_food = (random.randint(0, (WIDTH // CELL_SIZE) - 1), random.randint(0, (HEIGHT // CELL_SIZE) - 1))
            super_food_timer = 100  # Super food will stay for 100 frames

        if super_food:
            pygame.draw.rect(screen, BLUE, (super_food[0] * CELL_SIZE, super_food[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            
            # Draw the loading bar
            pygame.draw.rect(screen, LOADING_BAR_COLOR, (super_food[0] * CELL_SIZE, (super_food[1] - 1) * CELL_SIZE, LOADING_BAR_WIDTH * (super_food_timer / 100), LOADING_BAR_HEIGHT))
            
            if snake.body[0] == super_food:
                score += super_food_timer  # Add points according to the loading bar's value
                super_food = None  # Remove super food
            else:
                super_food_timer -= 1
                if super_food_timer <= 0:  # Remove super food after time runs out
                    super_food = None



        # Check collision with itself
        if snake.collide():
            running = False

        draw_snake(snake)
        pygame.draw.rect(screen, RED, (food[0] * CELL_SIZE, food[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        pygame.display.flip()
        clock.tick(10)

    pygame.quit()

if __name__ == "__main__":
    main()
