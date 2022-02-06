import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Cyber Spirits")

clock = pygame.time.Clock()
pixel_font = pygame.font.Font("font/Pixeltype.ttf", 50)

bg_surface = pygame.image.load('graphics/background.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

score_surf = pixel_font.render("RUN", True, (64,64,64))
score_rect = score_surf.get_rect(center = (100, 100))

enemy_surf = pygame.image.load('graphics/enemy/enemy1.png').convert_alpha()
enemy_rect = enemy_surf.get_rect(midbottom = (600 , 310))

player_surf = pygame.image.load('graphics/Player/Robot_Walk1_v1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,310))
player_gravity = 0


while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if player_rect.bottom == 310:
                    player_gravity = -20
        if event.type == pygame.MOUSEBUTTONDOWN:
            if player_rect.collidepoint(event.pos):
                if player_rect.bottom == 310:
                    player_gravity = -20
    
    screen.blit(bg_surface, (0,0))
    screen.blit(ground_surface, (0,300)) 
    # pygame.draw.rect(screen, 'Blue3', score_rect, width=200)
    # # pygame.draw.line(screen,'cyan',(0,10), pygame.mouse.get_pos())
    # # pygame.draw.circle(screen, '#c0e3ec', score_rect.center, 33)
    # screen.blit(score_surf, score_rect)    
    
    
    enemy_rect.right -= 3
    if enemy_rect.right < -100: enemy_rect.right = 800
    screen.blit(enemy_surf, enemy_rect)   


    # Player 
    player_gravity += 1
    player_rect.y += player_gravity
    if player_rect.bottom >= 310: player_rect.bottom = 310
    screen.blit(player_surf, player_rect)

    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_SPACE]:
    #     print('jump')
    # if player_rect.colliderect(enemy_rect):
    #     print("Ouch")
    # mouse_pos = pygame.mouse.get_pos()
    # if player_rect.collidepoint(mouse_pos):
    #     print(pygame.mouse.get_pressed())
    
    pygame.display.update()
    clock.tick(60)