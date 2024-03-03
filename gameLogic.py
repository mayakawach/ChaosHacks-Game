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
sky_image2 = pygame.image.load("images/sky2.jpg")
sky_image2 = pygame.transform.scale(sky_image2, (setup.SCREEN_WIDTH, setup.SCREEN_HEIGHT))

def game():
    if timer.counter > 10:
        setup.screen.blit(sky_image, (0, 0))  # Draw the sky image
    else:
        setup.screen.blit(sky_image2, (0, 0))  # Draw the sky image
    
    drawTimer()
    drawGameTitle()
    drawFood(vegetables)
    basket()
    pygame.display.update()
    
def drawGameTitle():
    if timer.counter > 10:
        text = setup.font.render("COOKING CHAOS", True, (0, 0, 0))
    else:
        text = setup.font.render("COOKING CHAOS", True, (255, 255, 255))
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

    foodBasket = pygame.Rect(650, 460, 150, 150)

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
    # Load the basket image
    basket_image = pygame.image.load("images/basket.png")
    
    # Resize the basket image to match the dimensions of the basket rect
    basket_image = pygame.transform.scale(basket_image, (basket.width, basket.height))
    
    # Blit the basket image onto the screen at the position of the basket rect
    setup.screen.blit(basket_image, (basket.x, basket.y))
    
    # Draw the total string
    text = setup.font.render(totalString, True, (255, 255, 255))
    setup.screen.blit(text, (710, 540))

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
