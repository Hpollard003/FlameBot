import pygame, sys
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Basic")

clock = pygame.time.Clock()

bg_surface = pygame.image.load('graphics/background.png')
ground_surface = pygame.image.load('graphics/ground.png')


while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(bg_surface, (0,0))
    screen.blit(ground_surface, (0,300))        
    
    pygame.display.update()
    clock.tick(60)