import pygame
import time
import random

# Set-up
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
pygame.display.set_caption("Cooking Chaos")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# constants
BASKET_HEIGHT = 30
BASKET_WIDTH = 50

class NewFood:
  def __init__(food, item, name, price):
    food.item = item
    food.name = name
    food.price = price

def draw(basket):
    screen.fill(("white"))
    pygame.draw.rect(screen, "brown", basket)
    pygame.display.update()

def main() :
    RUNNING = True
    frames = pygame.time.Clock()
    foodBasket = pygame.Rect(SCREEN_WIDTH - BASKET_WIDTH, SCREEN_HEIGHT - BASKET_HEIGHT, BASKET_WIDTH, BASKET_HEIGHT)
    tomato = pygame.Rect(100, SCREEN_HEIGHT - 20, 20,)
    t = NewFood()
    while RUNNING: 
        frames.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False
                break
        draw(foodBasket)
    pygame.quit()

if __name__ == "__main__" :
    main()