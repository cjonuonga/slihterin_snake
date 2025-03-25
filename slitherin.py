import pygame
import time
import random
import sys

# Snake speed
slither_speed = 15

# Window size
x_window = 720
y_window = 480

# Defining Colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Game states - Define these OUTSIDE the main loop
PLAYING = 1
GAME_OVER = 0
game_state = PLAYING

# Game Initialization
pygame.init()

# Game window initalization
pygame.display.set_caption('Slitherin Snake')
game_window = pygame.display.set_mode((x_window, y_window))

# Frames per second controller
fps = pygame.time.Clock()

# Snake default position
slither_position = [100, 50]

# First 4 blocks of snake body
slither_body = [[100, 50], 
                [90, 50], 
                [80, 50], 
                [70, 50]]

# Apple position
apple_position = [random.randrange(1, (x_window//10)) * 10, 
                  random.randrange(1, (y_window//10)) * 10]
apple_spawn = True

# Setting default snake direction -> right
direction = 'RIGHT'
change_to = direction

# Setting initial score
score = 0

# Displaying Score function
def score_show(choice, color, font, size):
    # Creating font object font_score
    font_score = pygame.font.SysFont(font, size)

    # Creating the display surface object
    # surface_score
    surface_score = font_score.render('Score: ' + str(score), True, color)

    # Creating rectangluar object for the text surface object
    score_rect = surface_score.get_rect()

    # Displaying text
    game_window.blit(surface_score, score_rect)

# Game over check function
def is_game_over():
    # If the Slitherin snake hits the wall
    if slither_position[0] > x_window-10 or slither_position[0] < 0 or slither_position[1] > y_window-10 or slither_position[1] < 0:
        return True

    # If the Slitherin snake hits itself
    for block in slither_body[1:]:
        if slither_position[0] == block[0] and slither_position[1] == block[1]:
            return True
    return False

# Display Game Over function
def show_game_over():
    game_window.fill(black)

    # Game over message
    font = pygame.font.SysFont('times new roman', 30)
    game_over_text = font.render('Game Over! Your Score is: ' + str(score), True, white)
    game_over_rect = game_over_text.get_rect()
    game_over_rect.midtop = (x_window/2, y_window/4)
    game_window.blit(game_over_text, game_over_rect)

    # Final Score
    font = pygame.font.SysFont('times new roman', 20)
    final_score_text = font.render("Final Score: " + str(score), True, white)
    final_score_rect = final_score_text.get_rect()
    final_score_rect.midtop = (x_window/2, y_window/2)
    game_window.blit(final_score_text, final_score_rect)

    # Restart Intrsuctions
    font = pygame.font.SysFont('times new roman', 20)
    restart_text = font.render("To play again press R", True, white)
    restart_rect = restart_text.get_rect()
    restart_rect.midtop = (x_window/2, y_window/1.5)
    game_window.blit(restart_text, restart_rect)

    pygame.display.flip()

# Restart game functionality
def restart_game():
    # Default start game settings
    global slither_position, slither_body, apple_position, apple_spawn, direction, change_to, score, game_state
    slither_position = [100, 50]
    slither_body = [[100, 50], [90, 50], [80, 50], [70, 50]]
    apple_position = [random.randrange(1, (x_window//10)) * 10, 
                      random.randrange(1, (y_window//10)) * 10]
    apple_spawn = True
    direction = 'RIGHT'
    change_to = direction
    score = 0
    game_state = PLAYING

# Slitherin Snake Main Function
while True:
    # Handling controller(key) events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
            
            # Handling game restart - Fixed by checking for the key value
            if game_state == GAME_OVER and event.key == pygame.K_r:
                restart_game()
    
    if game_state == PLAYING:
        # If two keys are pressed at the same time - Fixed typo in "direction"
        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'  
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

        # Moving the slihterin snake
        if direction == 'UP':
            slither_position[1] -= 10
        if direction == 'DOWN':
            slither_position[1] += 10
        if direction == 'LEFT':
            slither_position[0] -= 10
        if direction == 'RIGHT':
            slither_position[0] += 10
        
        # Growing slitherin snake functionality
        slither_body.insert(0, list(slither_position))
        if slither_position[0] == apple_position[0] and slither_position[1] == apple_position[1]:
            score += 1
            apple_spawn = False
        else:
            slither_body.pop()

        if not apple_spawn:
            apple_position = [random.randrange(1, (x_window//10)) * 10, 
                            random.randrange(1, (y_window//10)) * 10]
        apple_spawn = True

        # Background
        game_window.fill(black)

        # Drawing the slitherin snake and apple
        for pos in slither_body:
            pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))
        pygame.draw.rect(game_window, red, pygame.Rect(apple_position[0], apple_position[1], 10, 10))
        
        # Continuously dispalying score
        score_show(1, white, 'times new roman', 20)

        # Check for game over
        if is_game_over():
            game_state = GAME_OVER

    # If game over, show the game over screen
    if game_state == GAME_OVER:
        show_game_over()
    
    # Update display and control frame rate    
    pygame.display.update()
    fps.tick(slither_speed)