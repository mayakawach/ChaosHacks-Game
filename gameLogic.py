import pygame
import food
import setup
import timer

totalMoney = 0
totalString = ""

dragging = False
offset_x, offset_y = 0, 0

num_vegetables = 50
vegetables = []

for i in range(num_vegetables):
    new_vegetable = food.create_vegetable(i)
    vegetables.append(new_vegetable)

sky_image = pygame.image.load("images/sky.jpg")
sky_image = pygame.transform.scale(sky_image, (setup.SCREEN_WIDTH, setup.SCREEN_HEIGHT))

def game():
    setup.screen.blit(sky_image, (0, 0))  # Draw the sky image
    drawTimer()
    drawGameTitle()
    drawFood(vegetables)
    basket()
    pygame.display.update()
    
def drawGameTitle():
    text = setup.font.render("COOKING CHAOS", True, (0, 0, 0))
    setup.screen.blit(text, (290, 25))

def drawTimer() :
    text_rect = timer.text.get_rect(center = setup.screen.get_rect().center)
    setup.screen.blit(timer.text, text_rect)

def drawFood(veg):
    for i in veg:
        background_circle_radius = max(i.shape.width, i.shape.height) // 2 + 5
        background_circle_color = (0, 0, 0, 10)
        background_circle_center = i.shape.center
        pygame.draw.circle(setup.screen, background_circle_color, background_circle_center, background_circle_radius, 0)
        
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
