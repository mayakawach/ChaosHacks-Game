from enum import Enum
import pygame
import gameLogic
import setup
import states

def draw():
    setup.bg.blit(setup.screen, (0,0))
    
    match(states.current_state):
        
        case states.State.MAIN_MENU:
            setup.screen.fill((0,0,0))
            text = setup.font.render("MENU", True, (255, 255, 255))
            setup.screen.blit(text, (100, 100))
            pygame.draw.rect(setup.screen, "blue", (50,50,50,50))
            
        case states.State.GAME:
            gameLogic.game()
    
    pygame.display.update()
    
frames = pygame.time.Clock()
while states.RUNNING: 
    frames.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            states.RUNNING = False
            break
        
        if event.type == pygame.KEYDOWN:
            if states.current_state == states.State.MAIN_MENU:
                states.current_state = states.State.GAME
    draw()

pygame.quit()
