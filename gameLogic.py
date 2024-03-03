import pygame
import food
import setup
import timer

totalMoney = 0
totalString = ""

dragging = False
offset_x, offset_y = 0, 0

num_vegetables = 20
vegetables = []

for i in range(num_vegetables):
    new_vegetable = food.create_vegetable(i)
    vegetables.append(new_vegetable)

def game():
    setup.screen.fill((0,0,0))
    drawTimer()
    drawGameTitle()
    drawFood(vegetables)
    basket()
    pygame.display.update()
    
<<<<<<< HEAD
=======
def drawGameTitle():
    text = setup.font.render("COOKING CHAOS", True, (255, 255, 255))
    setup.screen.blit(text, (290, 25))
>>>>>>> 2304893db4a2e7d03818cdc48467d695687112a2

def drawTimer() :
    text_rect = timer.text.get_rect(center = setup.screen.get_rect().center)
    setup.screen.blit(timer.text, text_rect)

def drawFood(veg):
    for i in veg:
        setup.screen.blit(i.image, i.shape.topleft)

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

    drawBasket(foodBasket, totalString)

def drawBasket(basket, totalString):
    pygame.draw.rect(setup.screen, "brown", basket)
    text = setup.font.render(totalString, True, (255, 255, 255))
    setup.screen.blit(text, (735, 550))

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