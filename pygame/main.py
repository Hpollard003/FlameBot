import pygame
from sys import exit
from random import randint

# Score Card
def display_score():
    current_time = int((pygame.time.get_ticks() - start_time) / 1000)
    score_surf = pixel_font.render(f'Score: {current_time}', False, 'Cyan')
    score_rect = score_surf.get_rect(center = (400, 100))
    screen.blit(score_surf,score_rect)
    return current_time

# Random Enemy Spawn Intervals 
def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5
            
            if obstacle_rect.bottom == 310: 
                screen.blit(enemy_surf, obstacle_rect)
            else: 
                screen.blit(flying_enemy_surf, obstacle_rect)
            
        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]
            
        return obstacle_list
    else: return []

def collision(player, obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect): return False
    return True
    

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

# Enemy1 attributes
enemy_surf = pygame.image.load('graphics/enemy/Red/red1.png').convert_alpha()
# Enemy2 attributes
flying_enemy_surf = pygame.image.load('graphics/enemy/Blue/blue1.png').convert_alpha()


obstacle_rect_list = []

# Player attributes
player_idle = pygame.image.load('graphics/player/walk.png')
player_idle_rect = player_idle.get_rect(midbottom = (80, 310))
player_surf = pygame.image.load('graphics/Player/jump.png').convert_alpha()
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

# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)


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
                start_time = pygame.time.get_ticks()
        if event.type == obstacle_timer and game_active:
            if randint(0,2):
                obstacle_rect_list.append(enemy_surf.get_rect(midbottom = (randint(900,1100), 310)))
            else:
                obstacle_rect_list.append(flying_enemy_surf.get_rect(midbottom = (randint(900,1100), 200)))
                
            
    
    if game_active:
        # Background and Floor
        screen.blit(bg_surface, (0,0))
        screen.blit(ground_surface, (0,300)) 
        score = display_score()

        # # Ememy
        # flying_enemy_rect.right -= 6
        # if flying_enemy_rect.right < -100: flying_enemy_rect.right = 800
        # screen.blit(flying_enemy_surf, flying_enemy_rect)   
        
        # Obstacles
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)
            
        

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
        game_active = collision(player_rect, obstacle_rect_list)

    else: 
        screen.fill('gray18') 
        screen.blit(player_stand, player_stand_rect)
        obstacle_rect_list.clear()
        player_rect.midbottom = (80 , 310)
        player_gravity = 0
        
        score_message = pixel_font.render(f'Your Score: {score}' , False, 'orange')
        score_message_rect = score_message.get_rect(center = (400,340))
        screen.blit(intro_text_surf, intro_text_rect)
        
        if score == 0:
            screen.blit(start_text_surf, start_text_rect)
        else: 
            screen.blit(score_message, score_message_rect)
    

    pygame.display.update()
    clock.tick(60)