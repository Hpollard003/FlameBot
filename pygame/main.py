import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Cyber Spirits")

clock = pygame.time.Clock()
pixel_font = pygame.font.Font("font/Pixeltype.ttf", 50)

bg_surface = pygame.image.load('graphics/background.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
text_surface = pixel_font.render("RUN", False, "cyan")

enemy_surf = pygame.image.load('graphics/enemy/enemy1.png').convert_alpha()
enemy_rect = enemy_surf.get_rect(midbottom = (600 , 310))

player_surf = pygame.image.load('graphics/Player/Robot_Walk1_v1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,310))

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(bg_surface, (0,0))
    screen.blit(ground_surface, (0,300)) 
    screen.blit(text_surface, (230, 10))    
    enemy_rect.right -= 3
    if enemy_rect.right < -100: enemy_rect.right = 800
    screen.blit(enemy_surf, enemy_rect)   
    player_rect.left += 3
    if player_rect.left > 800: player_rect.left = -100
    screen.blit(player_surf, player_rect)
    
    pygame.display.update()
    clock.tick(60)