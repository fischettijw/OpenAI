import pygame

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Template")

# Set up game loop
game_running = True
while game_running:
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    # Update

    # Draw
    screen.fill((255, 255, 255))  # Fill screen with white color
    pygame.display.update()

# Quit Pygame
pygame.quit()
