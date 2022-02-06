import pygame
from sys import exit

# Initializing and window settings
pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Cyber Spirits")

# Settings
clock = pygame.time.Clock()
pixel_font = pygame.font.Font("font/Pixeltype.ttf", 50)
game_active = True

# Bg and Floor attributes
bg_surface = pygame.image.load('graphics/background.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

# Score Card
score_surf = pixel_font.render("RUN", True, (64,64,64))
score_rect = score_surf.get_rect(center = (100, 100))

# Enemy attributes
enemy_surf = pygame.image.load('graphics/enemy/enemy1.png').convert_alpha()
enemy_rect = enemy_surf.get_rect(midbottom = (600 , 310))

# Player attributes
player_surf = pygame.image.load('graphics/Player/Robot_Walk1_v1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,310))
player_gravity = 0


while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
        # User Inputs
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_rect.bottom == 310:
                player_gravity = -20
        if event.type == pygame.MOUSEBUTTONDOWN:
            if player_rect.collidepoint(event.pos) and player_rect.bottom == 310:
                player_gravity = -20
    
    # Background and Floor
    screen.blit(bg_surface, (0,0))
    screen.blit(ground_surface, (0,300)) 

    # Ememy
    enemy_rect.right -= 3
    if enemy_rect.right < -100: enemy_rect.right = 800
    screen.blit(enemy_surf, enemy_rect)   

    # Player 
    player_gravity += 1
    player_rect.y += player_gravity
    if player_rect.bottom >= 310: player_rect.bottom = 310
    screen.blit(player_surf, player_rect)
    
    # GameOver Collision
    if enemy_rect.colliderect(player_rect):
        pygame.quit()
        exit()
    
    

    pygame.display.update()
    clock.tick(60)