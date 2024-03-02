from enum import Enum
import pygame

class State(Enum):
    MAIN_MENU = 0
    GAME = 1
    
current_state = State.MAIN_MENU
RUNNING = True