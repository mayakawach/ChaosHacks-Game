import pygame

pygame.init()

clock = pygame.time
# Set-up
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500

pygame.display.set_caption("Cooking Chaos")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
bg = pygame.image.load("sky.jpg")

Running = True

RUNNING = True
frames = pygame.time.Clock()
while RUNNING: 
    frames.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
            break
        
        if event.type == pygame.KEYDOWN:
            RUNNING = False
    draw()
pygame.quit()