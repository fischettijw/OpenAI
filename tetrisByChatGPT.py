import pygame
import random

# Initialize the game
pygame.init()

# Set up the window
window = pygame.display.set_mode((300, 500))

# Define colors
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Define the block size and rows and columns
block_size = 25
cols = 10
rows = 20

# Define the shapes of the tetrominoes
tetrominoes = [
    [[1, 1, 1, 1]],

    [[2, 2, 2],
     [0, 2, 0]],

    [[3, 3, 3],
     [0, 0, 3]],

    [[4, 4],
     [4, 4]],

    [[0, 5, 5],
     [5, 5, 0]],

    [[6, 6, 0],
     [0, 6, 6]],

    [[0, 7, 0],
     [7, 7, 7]]
]

# Initialize a blank grid
grid = [[0 for x in range(cols)] for y in range(rows)]

# Initialize the current tetromino and its position
current_tetromino = random.choice(tetrominoes)
current_x = cols // 2 - len(current_tetromino[0]) // 2
current_y = 0

# Set up the clock
clock = pygame.time.Clock()

# Start the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the window
    window.fill(black)

    # Draw the grid
    for y in range(rows):
        for x in range(cols):
            if grid[y][x] > 0:
                pygame.draw.rect(window, (red, green, blue)[grid[y][x] - 1], (x * block_size, y * block_size, block_size, block_size))

    # Draw the current tetromino
    for y, row in enumerate(current_tetromino):
        for x, val in enumerate(row):
            if val > 0:
                pygame.draw.rect(window, (red, green, blue)[val - 1], ((current_x + x) * block_size, (current_y + y) * block_size, block_size, block_size))

    # Update the display
    pygame.display.update()

    # Limit the framerate
    clock.tick(60)

# Quit the game
pygame.quit()
