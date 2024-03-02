#make play and quit buttons  will be added on main menu
#using multiple screens in pygame, need functions with own game loops

import pygame 
import sys 

pygame.init()
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("button")
main_font = pygame.font.SysFont("cambria", 50)
#first need button class 
class Button ():
    def __init__(self, image, x_pos, y_pos, text_input ): #initializing button
        self.image = image  #png
        self.x_pos = x_pos
        self.y_pos = 
        #^corrdinates of where want the button
        self.rect = self.image.get_rect(center=(self.x_pos,self.y_pos)) #check for input later
        self.text_input = text_input #storing text
        self.text = main_font.render(self.text_input, True, "white")
        self.text_react = self.text.get_rect(center=(self.x_pos, self.y_pos)) #check text input

    def update(self): #
        screen.blit
        screen.blit 
    
    def checkForInput(self, position)



