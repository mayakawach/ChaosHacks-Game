import pygame

pygame.init()

clock = pygame.time
# Set-up
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# create background
win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
bg = pygame.transform.scale(pygame.image.load("sky.jpg"), (0,0))

pygame.display.set_caption("Cooking Chaos")

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
bg = pygame.image.load("sky.jpg")
font = pygame.font.Font(None, 36)