import pygame
import sys
import random
import subprocess

pygame.init()

vec = pygame.math.Vector2

HEIGHT = 450
WIDTH = 400
ACC = 0.5
FRIC = -0.12
FPS = 60

FramePerSec = pygame.time.Clock()

displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")

x = 50
y = 50
length = 200
width = 200
run = True

while run:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            run =False

    pygame.draw.rect(displaysurface, (255,210,0), (x,y,length,width))
    pygame.display.update()

pygame.quit()