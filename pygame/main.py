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

enemy_surface = pygame.image.load('graphics/enemy/enemy1.png')
enemy_x_pos = 600

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(bg_surface, (0,0))
    screen.blit(ground_surface, (0,300)) 
    screen.blit(text_surface, (230, 10))    
    enemy_x_pos -= 4
    if enemy_x_pos < -100: enemy_x_pos = 800
    screen.blit(enemy_surface, (enemy_x_pos, 250))   
    
    pygame.display.update()
    clock.tick(60)