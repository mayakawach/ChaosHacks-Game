import pygame 

pygame.init()

font = pygame.font.SysFont(None, 800)
counter = 30
text = font.render(str(counter), True, (255, 255, 255))

timer_event = pygame.USEREVENT+1
pygame.time.set_timer(timer_event, 1000)