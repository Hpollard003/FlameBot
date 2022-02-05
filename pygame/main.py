import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Basic")

clock = pygame.time.Clock()
pixel_font = pygame.font.Font("font/Pixeltype.ttf", 50)

bg_surface = pygame.image.load('graphics/background.png')
ground_surface = pygame.image.load('graphics/ground.png')
text_surface = pixel_font.render("My Game", False, "cyan")

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(bg_surface, (0,0))
    screen.blit(ground_surface, (0,300)) 
    screen.blit(text_surface, (230, 10))       
    
    pygame.display.update()
    clock.tick(60)