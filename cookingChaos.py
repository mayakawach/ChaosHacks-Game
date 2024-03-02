from enum import Enum
import pygame
import gameLogic
import setup

def draw():
    setup.bg.blit(setup.screen, (0,0))
    
    match(setup.current_state):
        
        case setup.State.MAIN_MENU:
            setup.screen.fill((0,0,0))
            text = setup.font.render("MENU", True, (255, 255, 255))
            setup.screen.blit(text, (100, 100))
            pygame.draw.rect(setup.screen, "blue", (50,50,50,50))
            
        case setup.State.GAME:
            gameLogic.game()
    
    pygame.display.update()
    
frames = pygame.time.Clock()
while setup.RUNNING: 
    frames.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            setup.RUNNING = False
            break
        
        if event.type == pygame.KEYDOWN:
            if setup.current_state == setup.State.MAIN_MENU:
                setup.current_state = setup.State.GAME
    draw()

pygame.quit()
