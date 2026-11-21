import pygame
import random
import sys

# Pygame initialize karein
pygame.init()

# Constants 
GRID_WIDTH = 15
GRID_HEIGHT = 15
CELL_SIZE = 40  
WINDOW_WIDTH = GRID_WIDTH * CELL_SIZE
WINDOW_HEIGHT = GRID_HEIGHT * CELL_SIZE

# Colors 
BLACK = (15, 15, 15)
WHITE = (255, 255, 255)
GREEN = (46, 204, 113)
DARK_GREEN = (39, 174, 96)
RED = (231, 76, 60)
GRAY = (40, 40, 40)

# Reset Game state function
def reset_game():
    snake = [(7, 7)]
    direction = 'RIGHT'
    score = 0
    # Food ko strictly 0 se GRID_WIDTH-1 aur GRID_HEIGHT-1 ke beech me spawn karwaya hai
    food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
    while food in snake:
        food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
    return snake, direction, score, food

def main():
    # Screen setup
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Snake game with aditya")
    clock = pygame.time.Clock()
    
    # Fonts
    font_large = pygame.font.SysFont(None, 42)
    font_medium = pygame.font.SysFont(None, 24)

    # Game State Variables
    snake, direction, score, food = reset_game()
    high_score = 0
    running = True
    game_over = False
    next_direction = direction

    while running:
        # 1. Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if game_over:
                    if event.key == pygame.K_r:
                        snake, direction, score, food = reset_game()
                        next_direction = direction
                        game_over = False
                    elif event.key == pygame.K_q:
                        running = False
                else:
                    if event.key == pygame.K_UP and direction != 'DOWN':
                        next_direction = 'UP'
                    elif event.key == pygame.K_DOWN and direction != 'UP':
                        next_direction = 'DOWN'
                    elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                        next_direction = 'LEFT'
                    elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                        next_direction = 'RIGHT'

        # 2. Game Logic Updates
        if not game_over:
            direction = next_direction
            head_x, head_y = snake[0]
            
            # Coordinate movement
            if direction == 'RIGHT':
                head_x += 1
            elif direction == 'LEFT':
                head_x -= 1
            elif direction == 'UP':
                head_y -= 1  
            elif direction == 'DOWN':
                head_y += 1
            
            new_head = (head_x, head_y)

            # Detect Wall or Self Collision
            if (head_x < 0 or head_x >= GRID_WIDTH or 
                head_y < 0 or head_y >= GRID_HEIGHT or 
                new_head in snake):
                game_over = True
                if score > high_score:
                    high_score = score
            else:
                snake.insert(0, new_head)
                
                # Check Food eaten
                if new_head == food:
                    score += 10
                        
                    # Spawn new food strictly inside the 15x15 grid limits
                    while True:
                        food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
                        if food not in snake:
                            break
                else:
                    snake.pop() # Remove tail if food not eaten

        # 3. Drawing / Rendering
        screen.fill(BLACK)
        
        # Draw Grid Lines
        for x in range(GRID_WIDTH):
            for y in range(GRID_HEIGHT):
                rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(screen, GRAY, rect, 1)

        # Draw Food (Ensure it stays inside the grid cells)
        food_rect = pygame.Rect(food[0] * CELL_SIZE, food[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, RED, food_rect, border_radius=8)

        # Draw Snake
        for i, segment in enumerate(snake):
            seg_rect = pygame.Rect(segment[0] * CELL_SIZE, segment[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            if i == 0:
                pygame.draw.rect(screen, GREEN, seg_rect, border_radius=6)  # Head
            else:
                pygame.draw.rect(screen, DARK_GREEN, seg_rect, border_radius=4)  # Body

        # Draw Score HUD 
        current_fps = min(5 + (score // 30), 20)
        score_surface = font_medium.render(f"Score: {score}  |  High Score: {high_score}  |  Speed: {current_fps} FPS", True, WHITE)
        screen.blit(score_surface, (15, 12))

        # Draw Game Over Overlay Screen
        if game_over:
            overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 180))
            screen.blit(overlay, (0, 0))

            over_text = font_large.render("GAME OVER", True, RED)
            score_text = font_medium.render(f"Final Score: {score}", True, WHITE)
            restart_text = font_medium.render("Press 'R' to Restart or 'Q' to Quit", True, WHITE)

            screen.blit(over_text, over_text.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2 - 30)))
            screen.blit(score_text, score_text.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2 + 10)))
            screen.blit(restart_text, restart_text.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2 + 50)))

        pygame.display.flip()
        
        # Dynamic Game Speed
        clock.tick(current_fps) 

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
