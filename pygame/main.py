import pygame
from sys import exit


# Score Card
def display_score():
    current_time = int((pygame.time.get_ticks() - start_time) / 1000)
    score_surf = pixel_font.render(f'Score: {current_time}', False, 'Cyan')
    score_rect = score_surf.get_rect(center = (400, 100))
    screen.blit(score_surf,score_rect)
    return current_time

# Initializing and window settings
pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Cyber Spirits")

# Settings
clock = pygame.time.Clock()
pixel_font = pygame.font.Font("font/Pixeltype.ttf", 50)
game_active = False
start_time = 0
score = 0

# Bg and Floor attributes
bg_surface = pygame.image.load('graphics/background.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

# Enemy attributes
enemy_surf = pygame.image.load('graphics/enemy/enemy1.png').convert_alpha()
enemy_rect = enemy_surf.get_rect(midbottom = (600 , 310))

# Player attributes
player_idle = pygame.image.load('graphics/player/player.png')
player_idle_rect = player_idle.get_rect(midbottom = (80, 310))
player_surf = pygame.image.load('graphics/Player/Robot_Walk1_v1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,310))
player_gravity = 0

# Intro Robot
player_stand = pygame.image.load('graphics/Player/player.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand,0,3)
player_stand_rect = player_stand.get_rect(center = (400,200))

# Intro Title
intro_text_surf = pixel_font.render("FlameBOT", False, "orange")
intro_text_rect = intro_text_surf.get_rect(center = (400, 50))


# How to Start Game
start_text_surf = pixel_font.render("PRESS  SPACE  TO  RUN", False, "orange")
start_text_rect = intro_text_surf.get_rect(center = (320, 340))


while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:       
            # User Inputs
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom == 310:
                    player_gravity = -23
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom == 310:
                    player_gravity = -23
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                enemy_rect.left = 800
                start_time = pygame.time.get_ticks()
    
    if game_active:
        # Background and Floor
        screen.blit(bg_surface, (0,0))
        screen.blit(ground_surface, (0,300)) 
        score = display_score()

        # Ememy
        enemy_rect.right -= 6
        if enemy_rect.right < -100: enemy_rect.right = 800
        screen.blit(enemy_surf, enemy_rect)   

        # Player 
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 310: player_rect.bottom = 310
        # screen.blit(player_surf, player_rect)
        if player_rect.bottom == 310: 
            screen.blit(player_idle, player_idle_rect)
        else:
            screen.blit(player_surf, player_rect)
            
        # GameOver Collision
        if enemy_rect.colliderect(player_rect):
            game_active = False
    else: 
        screen.fill('gray18') 
        screen.blit(player_stand, player_stand_rect)
        
        score_message = pixel_font.render(f'Your Score: {score}' , False, 'orange')
        score_message_rect = score_message.get_rect(center = (400,340))
        screen.blit(intro_text_surf, intro_text_rect)
        
        if score == 0:
            screen.blit(start_text_surf, start_text_rect)
        else: 
            screen.blit(score_message, score_message_rect)
    

    pygame.display.update()
    clock.tick(60)