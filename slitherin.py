import pygame
import time
import random

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


# Game Over function
def game_over():
    my_font = pygame.font.SysFont('times new roman', 35)

    # Creating a text surface on which text will be drawn
    game_over_surface = my_font.render('Your Score is:' + str(score), True, red)

    # Creating a rectangular object for text surface object
    game_over_rect = game_over_surface.get_rect()

    # Setting position of the text
    game_over_rect.midtop = (x_window/2, y_window/4)

    # Using blit to draw text on the screen
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()

    # Waiting a few seconds before quitting the game.
    time.sleep(3)

    # Quitting the game
    pygame.quit()
    quit()

# Slitherin Snake Main Function
while True:

    # Handling controller(key) events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
    
    # If two keys are pressed at the same time
    if change_to == 'UP' and direction != 'DOWN':
        direcion = 'UP'
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
    
    # Game end conditions
    if slither_position[0] < 0 or slither_position[0] > x_window-10:
        game_over()
    if slither_position[1] < 0 or slither_position[1] > y_window-10:
        game_over()
    
    # If the snake touches itself
    for block in slither_body[1:]:
        if slither_position[0] == block[0] and slither_position[1] == block[1]:
            game_over()
    
    # Continuously dispalying score
    score_show(1, white, 'times new roman', 20)

    # Refresh game screen
    pygame.display.update()

    # Frame Per Second /Refresh Rate
    fps.tick(slither_speed)

        











