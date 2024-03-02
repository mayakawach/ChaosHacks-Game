from enum import Enum
import pygame

pygame.init()

class State(Enum):
    MAIN_MENU = 0
    GAME = 1
    
current_state = State.MAIN_MENU
RUNNING = True

clock = pygame.time
# Set-up
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

pygame.display.set_caption("Cooking Chaos")

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
bg = pygame.image.load("sky.jpg")
font = pygame.font.Font(None, 36)