import pygame
import time
import food
import random

# Set-up
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
pygame.display.set_caption("Cooking Chaos")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

class NewFood:
  def __init__(food, item, name, price):
    food.item = item
    food.name = name
    food.price = price

def draw(t):
    screen.fill(("white"))
    for i in t[:] :
        pygame.draw.rect(screen, "red", i.item)
    pygame.display.update()

def main() :
    RUNNING = True

    # Foods
    random.seed(time.time())
    j = pygame.Rect(random.randint(10, 750), random.randint(10, 550), 20, 20)
    jam = NewFood(j, "jam", 2.0)

    p = pygame.Rect(random.randint(10, 750), random.randint(10, 550), 20, 20)
    peanut = NewFood(p, "peanut", 2.0)
    
    b = pygame.Rect(random.randint(10, 750), random.randint(10, 550), 20, 20)
    bread = NewFood(j, "bread", 2.0)

    frames = pygame.time.Clock()
    foods = [jam, peanut, bread]

    while RUNNING:
        frames.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False
                break
        
        draw(foods)

    pygame.quit()

if __name__ == "__main__" :  
    main()