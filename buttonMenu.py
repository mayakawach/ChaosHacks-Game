#make play and quit buttons  will be added on main menu
#using multiple screens in pygame, need functions with own game loops

import pygame 
import sys 
import states
import setup

#first need button class 
class Button ():
    def __init__(self, image, x_pos, y_pos, text_input ): #initializing button
        self.image = image  #png
        self.x_pos = x_pos
        self.y_pos = y_pos
        #^corrdinates of where want the button
        self.rect = self.image.get_rect(center=(self.x_pos,self.y_pos)) #check for input later, it is set to size of button
        self.text_input = text_input #storing text
        self.text = setup.font.render(self.text_input, True, "white")
        self.text_react = self.text.get_rect(center=(self.x_pos, self.y_pos)) #check text input

    def update(self): #blit puts image on screen
        setup.screen.blit(self.image, self.rect) 
        setup.screen.blit(self.text,self.text_react)
    
    def checkForInput(self, position): #check is where mouse position is 
        if position[0] in range (self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            states.current_state = states.State.GAME                                           
    def changeColor(self,position):
        if position[0] in range (self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text= setup.font.render(self.text_input, True, "green") #if hovering over 
        else:
            self.text = setup.font.render(self.text_input, True, "white")

button_surface = pygame.image.load("button.png")
button_surface = pygame. transform.scale(button_surface, (400,150))

button = Button(button_surface, 400, 300, "Start Game")

def mainMenu():
    drawGameTitle()
    button.update()
    button.changeColor(pygame.mouse.get_pos())
    
    handleMenuInput()
            
def handleMenuInput():
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            button.checkForInput(pygame.mouse.get_pos())

def drawGameTitle() :
    setup.screen.fill((0,0,0))
    text = setup.font.render("COOKING CHAOS", True, (255, 255, 255))
    setup.screen.blit(text, (290, 25))
         
    #in main menu now, can make seperate buttons using the class above 

    #PLAY_BUTTON = Button(image=pygame.image.load("assests/Play Rect.png"), pos=(640,250)
    #QUIT_BUTTON = Button(image=pygame.image.load("assests/Quit Rect.png"), pos=(640,400)

    #quit something else

    #play function 
    '''def play ():
        pygame.display.set_caption("play")
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")

        PLAY_TEXT
        PLAY_RECT
        SCREEN.blitt'''