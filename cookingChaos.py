import pygame
import time

pygame.init()

# Set-up
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 300
pygame.display.set_caption("Cooking Chaos")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
bg = pygame.image.load("sky.jpg")


class Food:
  def __init__(food, item, name, price):
    food.item = item
    food.name = name
    food.price = price

# Initializing Vegtable List
tomato = pygame.Rect(100, 150, 20, 20)
veg = [tomato]
t = Food(tomato,)
t = Food(tomato, "tomato", 1.00)

def drawFood(veg) :
    for i in veg :
        pygame.draw.rect(screen, "red", i)
    pygame.display.update()

def draw():
    # screen.fill(("red"))
    bg.blit(screen, (0,0))
    drawFood(veg)
    pygame.display.update()


RUNNING = True

frames = pygame.time.Clock()
while RUNNING: 
    frames.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False

        # mouse_click = pygame.mouse.get_pressed()
        # if mouse_click[pygame.MOUSEBUTTONUP]:
        #     print(mouse_click)

        #     tomato.x += 5
    
        
    
    draw()

pygame.quit()