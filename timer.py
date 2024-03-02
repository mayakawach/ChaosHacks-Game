import pygame 

pygame.init()
font = pygame.font.SysFont(None, 800)
counter = 60
text = font.render(str(counter), True, ("red"))

timer_event = pygame.USEREVENT+1
pygame.time.set_timer(timer_event, 1000)
