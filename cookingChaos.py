import pygame

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 200

pygame.display.set_caption

screen = pygame.display.set_mode((CONST_WIDTH, CONST_HEIGHT))
running = True

def draw():
    screen.fill(("red"))
    pygame.display.update()

while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw()

pygame.quit()