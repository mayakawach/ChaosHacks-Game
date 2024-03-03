import pygame
import food
import setup
import timer

# create background
win = pygame.display.set_mode((800, 600))
bg = pygame.transform.scale(pygame.image.load("sky.jpg"), (0,0))

# Initializing Vegtable List
tomato = pygame.Rect(100, 150, 20, 20)
veg = [tomato]
t = food.Food(tomato, "tomato", 1.00)

def game():
    drawGameTitle()
    drawBG()
    drawTimer()
    drawFood(veg)
    

def drawFood(veg):
    for i in veg:
        pygame.draw.rect(setup.screen, "red", i)

def drawGameTitle():
    setup.screen.fill((0,0,0))
    text = setup.font.render("COOKING CHAOS", True, (255, 255, 255))
    setup.screen.blit(text, (290, 25))

def drawTimer() :
    text_rect = timer.text.get_rect(center = setup.screen.get_rect().center)
    setup.screen.blit(timer.text, text_rect)


