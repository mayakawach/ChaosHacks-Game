import pygame
import food
import setup

import random

totalMoney = 0
totalString = ""

dragging = False
offset_x, offset_y = 0, 0

num_vegetables = 5
vegetables = []

for i in range(num_vegetables):
    new_vegetable = food.create_vegetable(i)
    vegetables.append(new_vegetable)

def game():
    drawGameTitle()
    drawFood(vegetables)
    basket()
    pygame.display.update()

def drawFood(veg):
    for i in veg:
        pygame.draw.rect(setup.screen, "red", i.shape)
    
def drawGameTitle():
    setup.screen.fill((0,0,0))
    text = setup.font.render("COOKING CHAOS", True, (255, 255, 255))
    setup.screen.blit(text, (290, 25))

def handleInput(event):
    global dragging, offset_x, offset_y, dragged_vegetable

    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:  # Left mouse button
            for veg_item in vegetables:
                if veg_item.shape.collidepoint(event.pos):
                    dragging = True
                    dragged_vegetable = veg_item
                    # Calculate offset from the top-left corner of the vegetable
                    offset_x = dragged_vegetable.shape.x - event.pos[0]
                    offset_y = dragged_vegetable.shape.y - event.pos[1]
    elif event.type == pygame.MOUSEMOTION:
        if dragging:
            dragged_vegetable.shape.x = event.pos[0] + offset_x
            dragged_vegetable.shape.y = event.pos[1] + offset_y
    elif event.type == pygame.MOUSEBUTTONUP:
        if event.button == 1:
            dragging = False
            dragged_vegetable = None
            
def basket() :
    global totalMoney, totalString
    
    foodBasket = pygame.Rect(700, 510, 150, 150)
    
    tomatoes_to_remove = []
    for veg in vegetables[:]:
        if veg.shape.x + 20 >= foodBasket.x and veg.shape.colliderect(foodBasket):
            totalMoney += veg.price
            totalString = str(totalMoney)
            tomatoes_to_remove.append(veg)

    for veg in tomatoes_to_remove:
        vegetables.remove(veg)

    draw(foodBasket, totalString)
    
def draw(basket, totalString):
    pygame.draw.rect(setup.screen, "brown", basket)
    drawText(totalString)
    
def drawText(totalString) :
    text = setup.font.render(totalString, True, (255, 255, 255))
    setup.screen.blit(text, (735, 550))