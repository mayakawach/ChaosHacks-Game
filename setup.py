import pygame

pygame.init()

# Set-up
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
clock = pygame.time

pygame.display.set_caption("Cooking Chaos")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# create background
bg = pygame.image.load("images/sky.jpg")
bg = pygame.transform.scale(bg, (screen.get_width(), screen.get_height()))

font = pygame.font.Font(None, 36)