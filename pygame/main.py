import pygame
from sys import exit
from random import randint, choice

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_walk_1 = pygame.image.load('graphics/Player/walk.png').convert_alpha()
        player_walk_2 = pygame.image.load('graphics/Player/walk1.png').convert_alpha()
        self.player_walk = [player_walk_1,player_walk_2]
        self.player_index = 0
        self.jump = pygame.image.load('graphics/Player/jump.png').convert_alpha()
        
        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom = (90,310))
        self.gravity = 0
    
    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 310:
            self.gravity = -23
            
    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 310: self.rect.bottom = 310
        
    def player_animation(self):
        if self.rect.bottom < 310:
            self.image = self.jump
        else:
            self.player_index += 0.05
            if self.player_index >= len(self.player_walk): self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]
        
    def update(self):
        self.player_input()
        self.apply_gravity()
        self.player_animation()

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        
        if type == 'red':
            enemy_frame_1 = pygame.image.load('graphics/enemy/Red/red1.png').convert_alpha()
            enemy_frame_2 = pygame.image.load('graphics/enemy/Red/red2.png').convert_alpha()
            enemy_frame_3 = pygame.image.load('graphics/enemy/Red/red3.png').convert_alpha()
            enemy_frame_4 = pygame.image.load('graphics/enemy/Red/red4.png').convert_alpha()
            self.frames = [enemy_frame_1, enemy_frame_2, enemy_frame_3, enemy_frame_4]
            y_pos = 310
        else:
            flying_enemy_frame_1 = pygame.image.load('graphics/enemy/Blue/blue1.png').convert_alpha()
            flying_enemy_frame_2 = pygame.image.load('graphics/enemy/Blue/blue2.png').convert_alpha()
            flying_enemy_frame_3 = pygame.image.load('graphics/enemy/Blue/blue3.png').convert_alpha()
            flying_enemy_frame_4 = pygame.image.load('graphics/enemy/Blue/blue4.png').convert_alpha()
            self.frames = [flying_enemy_frame_1, flying_enemy_frame_2, flying_enemy_frame_3, flying_enemy_frame_4]
            y_pos = 200
        
        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (randint(900,1100), y_pos))
    def animation(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames): self.animation_index= 0
        self.image = self.frames[int(self.animation_index)]
    def update(self):
        self.animation()
        self.rect.x -= 6
        self.destroy()
        
    def destroy(self):
        if self.rect.x <= -100:
            self.kill()

# Score Card
def display_score():
    current_time = int((pygame.time.get_ticks() - start_time) / 1000)
    score_surf = pixel_font.render(f'Score: {current_time}', False, 'Cyan')
    score_rect = score_surf.get_rect(center = (400, 100))
    screen.blit(score_surf,score_rect)
    return current_time

# # Random Enemy Spawn Intervals 
# def obstacle_movement(obstacle_list):
#     if obstacle_list:
#         for obstacle_rect in obstacle_list:
#             obstacle_rect.x -= 5
            
#             if obstacle_rect.bottom == 310: 
#                 screen.blit(enemy_surf, obstacle_rect)
#             else: 
#                 screen.blit(flying_enemy_surf, obstacle_rect)
            
#         obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]
            
#         return obstacle_list
#     else: return []

# def collision(player, obstacles):
#     if obstacles:
#         for obstacle_rect in obstacles:
#             if player.colliderect(obstacle_rect): return False
#     return True
def collision_sprite():
    if pygame.sprite.spritecollide(player.sprite, obstacle_group, True):
        return False
    else: return True
    

# def player_animation():
    # global player_surf, player_index
    
    # if player_rect.bottom < 310:
    #     player_surf = player_jump
    # else:
    #     player_index += 0.05
    #     if player_index >= len(player_walk): player_index = 0
    #     player_surf = player_walk[int(player_index)]

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

player = pygame.sprite.GroupSingle()
player.add(Player())
obstacle_group = pygame.sprite.Group()


# Bg and Floor attributes
bg_surface = pygame.image.load('graphics/background.png').convert()
ground_surface = pygame.image.load('graphics/ground1.png').convert_alpha()
ground_rect = ground_surface.get_rect(bottomleft = (0,470))

# Enemy1 attributes
# enemy_frame_1 = pygame.image.load('graphics/enemy/Red/red1.png').convert_alpha()
# enemy_frame_2 = pygame.image.load('graphics/enemy/Red/red2.png').convert_alpha()
# enemy_frame_3 = pygame.image.load('graphics/enemy/Red/red3.png').convert_alpha()
# enemy_frame_4 = pygame.image.load('graphics/enemy/Red/red4.png').convert_alpha()
# enemy_frames = [enemy_frame_1, enemy_frame_2, enemy_frame_3, enemy_frame_4]
# enemy_index = 0
# enemy_surf = enemy_frames[enemy_index]

# Enemy2 attributes
# flying_enemy_frame_1 = pygame.image.load('graphics/enemy/Blue/blue1.png').convert_alpha()
# flying_enemy_frame_2 = pygame.image.load('graphics/enemy/Blue/blue2.png').convert_alpha()
# flying_enemy_frame_3 = pygame.image.load('graphics/enemy/Blue/blue3.png').convert_alpha()
# flying_enemy_frame_4 = pygame.image.load('graphics/enemy/Blue/blue4.png').convert_alpha()
# flying_enemy_frames = [flying_enemy_frame_1, flying_enemy_frame_2, flying_enemy_frame_3, flying_enemy_frame_4]
# flying_enemy_index = 0
# flying_enemy_surf = flying_enemy_frames[flying_enemy_index]

# Obstacle Rectangle List
# obstacle_rect_list = []

# Player attributes
# player_walk_1 = pygame.image.load('graphics/player/walk.png').convert_alpha()
# player_walk_2 = pygame.image.load('graphics/player/walk1.png').convert_alpha()
# player_walk = [player_walk_1, player_walk_2]
# player_index = 0
# player_jump = pygame.image.load('graphics/Player/jump.png').convert_alpha()
# player_surf = player_walk[player_index]
# player_rect = player_surf.get_rect(midbottom = (80,310))
# player_gravity = 0

# Intro Flame
player_stand = pygame.image.load('graphics/enemy/Blue/blue1.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand,0,3)
player_stand_rect = player_stand.get_rect(center = (400,200))

# Intro Title
intro_text_surf = pixel_font.render("FlameBOT", False, "orange")
intro_text_rect = intro_text_surf.get_rect(center = (400, 50))

# Game Over
go_text_surf = pixel_font.render("You Died", False, "Red")
go_text_rect = intro_text_surf.get_rect(center = (400, 50))

# How to Start Game
start_text_surf = pixel_font.render("PRESS  SPACE  TO  RUN", False, "orange")
start_text_rect = intro_text_surf.get_rect(center = (320, 340))

# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

enemy_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(enemy_animation_timer , 500)

flying_enemy_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(flying_enemy_animation_timer , 200)


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
        if game_active:
            if event.type == obstacle_timer:
                obstacle_group.add(Obstacle(choice(['blue', 'red', 'red'])))
                # if randint(0,2):
                #     obstacle_rect_list.append(enemy_frame_1.get_rect(midbottom = (randint(900,1100), 310)))
                # else:
                #     obstacle_rect_list.append(flying_enemy_frame_1.get_rect(midbottom = (randint(900,1100), 200)))
            # if event.type == enemy_animation_timer:
            #     if enemy_index == 0: enemy_index = 3
            #     else: enemy_index = 0
            #     enemy_surf = enemy_frames[enemy_index]
            # if event.type == flying_enemy_animation_timer:
            #     if flying_enemy_index == 0: flying_enemy_index = 3
            #     else: flying_enemy_index= 0
            #     flying_enemy_surf = flying_enemy_frames[flying_enemy_index]

            
    
    if game_active:
        # Background and Floor
        screen.blit(bg_surface, (0,0))
        score = display_score()

        # ground movement
        ground_rect.right -= 2
        if ground_rect.right <= 800: ground_rect.right = 1600
        screen.blit(ground_surface, ground_rect) 
 
        
        # Obstacles
        # obstacle_rect_list = obstacle_movement(obstacle_rect_list)
            
        

        # Player 
        # player_gravity += 1
        # player_rect.y += player_gravity
        # if player_rect.bottom >= 310: player_rect.bottom = 310
        # player_animation()
        # screen.blit(player_surf,player_rect)
        player.draw(screen)
        player.update()
        
        obstacle_group.draw(screen)
        obstacle_group.update()
        
        # GameOver Collision
        game_active = collision_sprite()
        # game_active = collision(player_rect, obstacle_rect_list)
    else: 
        screen.fill('gray18') 
        screen.blit(player_stand, player_stand_rect)
        obstacle_rect_list.clear()
        player_rect.midbottom = (80 , 310)
        player_gravity = 0
        
        score_message = pixel_font.render(f'Your Score: {score}' , False, 'orange')
        score_message_rect = score_message.get_rect(center = (400,340))
        
        if score == 0:
            screen.blit(intro_text_surf, intro_text_rect)
            screen.blit(start_text_surf, start_text_rect)
        else: 
            screen.blit(go_text_surf, go_text_rect)
            screen.blit(score_message, score_message_rect)
    

    pygame.display.update()
    clock.tick(60)