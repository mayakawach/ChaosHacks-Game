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
        self.y_pos = y_pos
        #^corrdinates of where want the button
        self.rect = self.image.get_rect(center=(self.x_pos,self.y_pos)) #check for input later
        self.text_input = text_input #storing text
        self.text = main_font.render(self.text_input, True, "white")
        self.text_react = self.text.get_rect(center=(self.x_pos, self.y_pos)) #check text input

    def update(self): 
        screen.blit(self.image, self.react)
        screen.blit(self.text,self.text_react)
    
    def checkForInput(self, position):
        if position[0] in range (self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            print ("button press!")                                            
    def changeColor(self,position):
        if position[0] in range (self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text= main_font.render(self.text_input, True, "green")
        else:
            self.text = main_font.render(self.text_input, True, "white")

button_surface = pygame.image.load("button.png")
button_surface = pygame. transformers.scale(button_surface, (400,150))

button = Button(button_surface, 400, 300, "click me")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            button.checkForInput(pygame.mouse.get_pos())

    screen.fill("white")
    
    button.update()
    button.changeColor(pygame.mouse.get_pos())

    pygame.display.update()
         
    #in main menu now, can make seperate buttons using the class above 

    #play_button = Button()
    #quit_button = Button()
