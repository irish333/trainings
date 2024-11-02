import pygame
import random

# Initialize pygame
pygame.init()

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
blue = (50, 153, 213)
yellow = (255, 255, 102)

# Set display dimensions
display_width = 800
display_height = 600

# Set bird size and egg size
bird_width = 50
bird_height = 50
egg_size = 20

# Set display
game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Bird Laying Eggs Game")

# Set clock for FPS
clock = pygame.time.Clock()

# Load bird image
bird_image = pygame.image.load("bird.webp")  # Use a bird image or replace with a shape
bird_image = pygame.transform.scale(bird_image, (bird_width, bird_height))

# Function to display the bird
def display_bird(x, y):
    game_display.blit(bird_image, (x, y))

# Function to draw eggs
def draw_eggs(eggs_list):
    for egg in eggs_list:
        pygame.draw.circle(game_display, yellow, (egg[0], egg[1]), egg_size)

# Main game loop
def game_loop():
    game_over = False

    # Bird's initial position
    bird_x = 100
    bird_y = display_height / 2
    bird_y_change = 0

    # List to hold eggs (position of eggs)
    eggs = []

    # Bird movement speed and gravity
    bird_speed = 10
    gravity = 3

    # Egg laying delay
    egg_delay = 20
    egg_timer = 0

    while not game_over:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            # Bird controls
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    bird_y_change = -bird_speed
                if event.key == pygame.K_DOWN:
                    bird_y_change = bird_speed
                if event.key == pygame.K_SPACE:  # Lay an egg
                    eggs.append([bird_x + bird_width, bird_y + bird_height // 2])

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    bird_y_change = 0

        # Update bird's position
        bird_y += bird_y_change

        # Apply gravity (bird falls down when not moving)
        bird_y += gravity

        # Boundary conditions (bird stays on screen)
        if bird_y < 0:
            bird_y = 0
        if bird_y > display_height - bird_height:
            bird_y = display_height - bird_height

        # Fill the display background
        game_display.fill(blue)

        # Display bird
        display_bird(bird_x, bird_y)

        # Update eggs
        if egg_timer >= egg_delay:
            eggs.append([bird_x + bird_width, bird_y + bird_height // 2])
            egg_timer = 0
        egg_timer += 1

        # Move eggs to the left and remove them when out of bounds
        eggs = [[egg[0] - 5, egg[1]] for egg in eggs if egg[0] > 0]

        # Draw eggs
        draw_eggs(eggs)

        # Update display
        pygame.display.update()

        # Set FPS
        clock.tick(30)

    pygame.quit()
    quit()

# Run the game
game_loop()
