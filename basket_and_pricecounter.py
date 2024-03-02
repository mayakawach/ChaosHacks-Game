import pygame
import time
import random
import setup

# Set-up
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
pygame.display.set_caption("Cooking Chaos")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# constants
BASKET_HEIGHT = 30
BASKET_WIDTH = 50
font = pygame.font.Font(None, 36)


class NewFood:
  def __init__(food, item, name, price):
    food.item = item
    food.name = name
    food.price = price

def drawA(basket, t):
    screen.fill(("white"))
    pygame.draw.rect(screen, "brown", basket)
    for i in t :
        pygame.draw.rect(screen, "red", i.item)
    pygame.display.update()

def draw(basket):
    screen.fill(("white"))
    pygame.draw.rect(screen, "brown", basket)
    pygame.display.update()

def drawText(total) :
    text = font.render(total, True, (0, 0, 0))
    screen.blit(text, (100, 100))
    pygame.display.update()

def main() :
    RUNNING = True
    frames = pygame.time.Clock()
    foodBasket = pygame.Rect(SCREEN_WIDTH - BASKET_WIDTH, SCREEN_HEIGHT - BASKET_HEIGHT, BASKET_WIDTH, BASKET_HEIGHT)
    tomato = pygame.Rect(100, SCREEN_HEIGHT - 20, 20, 20)
    tomato1 = pygame.Rect(100, SCREEN_HEIGHT - 20, 20, 20)
    tomato2 = pygame.Rect(100, SCREEN_HEIGHT - 20, 20, 20)

    t = NewFood(tomato, "tomato", 1.00)
    t1 = NewFood(tomato1, "tomato", 1.00)
    t2 = NewFood(tomato2, "tomato", 1.00)

    l = [t]

    total = "0.0"
    totalInt = 0
    # while RUNNING: 
    #     frames.tick(60)
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             RUNNING = False
    #             break

    #     keys = pygame.key.get_pressed()

    #     if not l :
    #         continue
    #     elif keys[pygame.K_d] and t.item.x + 20 <= SCREEN_WIDTH :
    #         t.item.x += 5
    #     elif keys[pygame.K_a] and SCREEN_WIDTH - t.item.x >= 0:
    #         t.item.x -= 5

    #     tomatoes_to_remove = []
    #     for t in l[:] :
    #         if t.item.x + 20 >= foodBasket.x and t.item.colliderect(foodBasket):
    #             totalInt += t.price
    #             total = str(totalInt)
    #             tomatoes_to_remove.append(t)

    #     draw(total)

    #     for i in tomatoes_to_remove :
    #         remove(i);
            
    #     if not l :
    #         draw(foodBasket)
    #     else :
    #         drawA(foodBasket, tomato)
    # pygame.quit()

    total = "0.0"
    totalInt = 0

    while RUNNING:
        frames.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False
                break

        keys = pygame.key.get_pressed()

        if not l:
            continue
        elif keys[pygame.K_d] and t.item.x + 20 <= SCREEN_WIDTH:
            t.item.x += 5
        elif keys[pygame.K_a] and SCREEN_WIDTH - t.item.x >= 0:
            t.item.x -= 5

        tomatoes_to_remove = []
        for t_item in l[:]:
            if t_item.item.x + 20 >= foodBasket.x and t_item.item.colliderect(foodBasket):
                totalInt += t_item.price
                total = str(totalInt)
                tomatoes_to_remove.append(t_item)

        for t_item in tomatoes_to_remove:
            l.remove(t_item)

        if not l:
            draw(foodBasket)
        else:
            drawA(foodBasket, l)

        drawText(total)

    pygame.quit()

if __name__ == "__main__" :
    
    main()