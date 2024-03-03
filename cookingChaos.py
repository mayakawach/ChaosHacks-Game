from enum import Enum
import pygame
import gameLogic
import setup
import states
import buttonMenu
import dragableSquare

def draw():
    setup.bg.blit(setup.screen, (0,0))
    
    match(states.current_state):
        
        case states.State.MAIN_MENU:
            buttonMenu.mainMenu()
            
        case states.State.GAME:
            dragableSquare.game()
    
    pygame.display.update()
    
frames = pygame.time.Clock()
while states.RUNNING: 
    frames.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            states.RUNNING = False
            break
        elif event.type == gameLogic.timer.timer_event and states.current_state == states.State.GAME:
            gameLogic.timer.counter -= 1
            
            gameLogic.timer.text = gameLogic.timer.font.render(str(gameLogic.timer.counter), True, (0, 128, 0))
            if gameLogic.timer.counter == 0:
                states.RUNNING = False

        dragableSquare.handleInput(event)
    draw()

pygame.quit()
