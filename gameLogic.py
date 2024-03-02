import pygame
import food
import setup

def drawFood(veg) :
    for i in veg :
        pygame.draw.rect(setup.screen, "red", i)
    pygame.display.update()
    
# Initializing Vegtable List
tomato = pygame.Rect(100, 150, 20, 20)
veg = [tomato]
t = food.Food(tomato, "tomato", 1.00)