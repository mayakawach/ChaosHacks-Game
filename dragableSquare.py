import pygame
import food
import setup

dragging = False
offset_x, offset_y = 0, 0

# Initializing Vegtable List
tomato = pygame.Rect(100, 150, 200, 200)
veg = [tomato]
t = food.Food(tomato, "tomato", 1.00)

def game():
    drawGameTitle()
    drawFood(veg)

def drawFood(veg):
    for i in veg:
        pygame.draw.rect(setup.screen, "red", i)
    pygame.display.update()
    
def drawGameTitle():
    setup.screen.fill((0,0,0))
    text = setup.font.render("COOKING CHAOS", True, (255, 255, 255))
    setup.screen.blit(text, (290, 25))
    
def handleInput(event):
    global dragging, offset_x, offset_y

    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:  # Left mouse button
            if tomato.collidepoint(event.pos):
                dragging = True
                # Calculate offset from the top-left corner of the vegetable
                offset_x = tomato.x - event.pos[0]
                offset_y = tomato.y - event.pos[1]
    elif event.type == pygame.MOUSEMOTION:
        if dragging:
            tomato.x = event.pos[0] + offset_x
            tomato.y = event.pos[1] + offset_y
    elif event.type == pygame.MOUSEBUTTONUP:
        if event.button == 1:
            dragging = False