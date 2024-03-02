import pygame
from enum import Enum
import time
import gameLogic
import setup

class State(Enum):
    MAIN_MENU = 0
    GAME = 1
    
current_state = State.MAIN_MENU
RUNNING = True

def draw():
    setup.bg.blit(setup.screen, (0,0))
    
    match(current_state):
        case State.MAIN_MENU:
            pygame.draw.rect(setup.screen, "blue", (50,50,50,50))
        case State.GAME:
            gameLogic.drawFood(gameLogic.veg)
    
    pygame.display.update()
    
frames = pygame.time.Clock()
while RUNNING: 
    frames.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
            break
        
        if event.type == pygame.KEYDOWN:
            current_state = State.GAME
    draw()

pygame.quit()
