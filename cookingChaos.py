from enum import Enum
import pygame
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
            setup.screen.fill((0,0,0))
            text = setup.font.render("MENU", True, (255, 255, 255))
            setup.screen.blit(text, (100, 100))
            pygame.draw.rect(setup.screen, "blue", (50,50,50,50))
            
        case State.GAME:
            setup.screen.fill((0,0,0))
            text = setup.font.render("GAME", True, (255, 255, 255))
            setup.screen.blit(text, (100, 100))
            gameLogic.game()
    
    pygame.display.update()
    
frames = pygame.time.Clock()
while RUNNING: 
    frames.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
            break
        
        if event.type == pygame.KEYDOWN:
            if current_state == State.MAIN_MENU:
                current_state = State.GAME
            else:
                current_state = State.MAIN_MENU
    draw()

pygame.quit()
