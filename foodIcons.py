#placing icons on middle position on screen 
#ingredients will be placed in the middle for starting point?
#for every round (win or loss) ingredients will change and in all times its randomized 
#goes to next round randomizes but after first second will move around screen

from time import sleep
import pygame
pygame.init()

gameDisplay = pygame.display.set_mode((800,600)) 

mainFood1 = pygame.image.load("pbj.png")
mainFood2 = pygame.image.load("frenchToast.png")
mainFood3 = pygame.image.load("grilledCheese.png")

ingredient1 = pygame.image.load("bread.png")
ingredient2 = pygame.image.load("pb.png")
ingredient3 = pygame.image.load("jam.png")
ingredient4 = pygame.image.load("butter.png")
ingredient5 = pygame.image.load("cheese.png")
ingredient6 = pygame.image.load("milk.jpeg")
ingredient7 = pygame.image.load("egg.jpeg")


gameDisplay.blit(mainFood1,(0,0))
pygame.display.update()
sleep(1)

gameDisplay.blit(ingredient1, (150,10))
pygame.display.update()
sleep(5)

pygame.quit()
quit()