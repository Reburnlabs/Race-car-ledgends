import pygame
import sys
from random import *
from pygame import mixer 
import time
# Starting the mixer 
mixer.init() 
pygame.font.init()
font = pygame.font.Font('freesansbold.ttf', 32)
death_text = font.render('you died', True, (255,255,255))
play_text = font.render('play again', True, (255,255,255))
s = pygame.display.set_mode((1100, 600))
center_x = 1100/2
center_y = 600/2
s.fill((0, 200, 0))
pygame.display.set_caption("racer")
pygame.display.flip()
x = 100
y = 100
vel = 3
drag = 0.3
dire = 0
line_y = 0
line1_y = 200
line2_y = 400
score = 0
unrun = False
score_adder = 1
main_enemy_y = line_y
list1 = [460, 560, 500, 450]
enemy_x1 = choice(list1)
enemy_x2 = choice(list1)
enemy_x3 = choice(list1)
died = False
run2 = False
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 18)
start = True
audio_start = True
already = False
while start:
    mouse = pygame.mouse.get_pos()
    mouse_rect = pygame.draw.rect(s, (0,0,0), (mouse[0], mouse[1], 10, 10))
    s.fill((0,0,0))
    bg = pygame.image.load("C:/Users/matth/Downloads/pixil-frame-0 (73).png")
    width = bg.get_rect().width
    height = bg.get_rect().height
    bg = pygame.transform.scale(bg, (width*2, height*2))
    s.blit(bg, (0,0))
    aduio_rect = pygame.draw.rect(s, (0,0,0), (20,20, 70, 30))
    audio = pygame.image.load("C:/Users/matth/Downloads/pixil-frame-0 (74).png")
    for event in pygame.event.get():
       if event.type == pygame.MOUSEBUTTONDOWN:
           if aduio_rect.colliderect(mouse_rect):
               if already == False:
                   audio_start = False
               else:
                   audio_start = True
               already = True
       if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    key = pygame.key.get_pressed()
    if key[pygame.K_a]:
        if audio_start == True:
              mixer.music.load("C:/Users/matth/Downloads/car-door-close,-start-engine-and-drive-sound-effect-made-with-Voicemod.mp3") 
              mixer.music.set_volume(0.7) 
              mixer.music.play()
        font = pygame.font.SysFont("Courier", 40)
        s.fill((0,0,0))
        txt = font.render("loading...", True, (255,255,255))
        s.blit(txt, (center_x-100, center_y-100))
        pygame.display.update()
        time.sleep(3)
        run = True
        start = False
    font = pygame.font.SysFont("Courier", 70)
    s.blit(audio, (-300, -380))
    main_text = font.render("racer 2d", True, (255,255,255))
    font = pygame.font.SysFont("Arial", 30)
    main_text2 = font.render("press  A  to  start", True, (255,255,255))
    img = pygame.image.load("C://Users/matth/downloads/pixil-frame-0 (19).png")
    width = img.get_rect().width
    height = img.get_rect().height
    img = pygame.transform.scale(img, (width/4, height/4))
    s.blit(img, (450,300))
    img_text = font.render("Made by Reburn Labs", True, (255,255,255))
    s.blit(img_text, (430, 500))
    s.blit(main_text, (400, 0))
    s.blit(main_text2, (450, 200))
    pygame.display.update()
while run:
    font = pygame.font.SysFont("Arial", 18)
    player_rect = pygame.draw.rect(s, (255,0,0), (x+425,y+345,30, 60))
    s.fill((0, 200, 0))
    list1 = [460, 560, 500, 450]
    fps = str(int(clock.get_fps()))
    pygame.display.set_caption("FPS:%s" % (fps))
    font = pygame.font.Font('freesansbold.ttf', 32)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    clock.tick(120)
    key = pygame.key.get_pressed()
    mouse = pygame.mouse.get_pos()
    if key[pygame.K_LEFT]:
        x -= vel
        dire = 1
    elif key[pygame.K_RIGHT]:
        x += vel
        dire = 2
    else:
        dire = 0
    s.fill((0, 200, 0))
    main_enemy_y = line_y
    if line_y < 600:
       line_y += (vel + 1)
       main_enemy_y = line_y
    else:
        line_y = 0
        main_enemy_y = line_y
        score += score_adder
        enemy_x1 = choice(list1)
        enemy_x2 = choice(list1)
        enemy_x3 = choice(list1)
    if line1_y < 600:
       line1_y += (vel + 1)
    else:
        line1_y = 0
    if line2_y < 600:
       line2_y += (vel + 1)
    else:
        line2_y = 0
    road = pygame.draw.rect(s, (0,0,0), (450, -100, 200, 800))
    score_text = font.render("score:%s" % (score), True, (255, 255, 255))
    s.blit(score_text, (0, 0))
    lines = pygame.draw.rect(s, (255,255,255), (530, line_y, 10, 70))
    enemy1 = pygame.draw.rect(s, (255,0,0), (enemy_x1,main_enemy_y,30,50))
    enemy2 = pygame.draw.rect(s, (255,0,0), (enemy_x2,main_enemy_y,30,50))
    enemy3 = pygame.draw.rect(s, (255,0,0), (enemy_x3,main_enemy_y,30,50))
    lines = pygame.draw.rect(s, (255,255,255), (530, line1_y, 10, 70))
    lines = pygame.draw.rect(s, (255,255,255), (530, line2_y, 10, 70))
    if dire == 0:
       player = pygame.image.load("C://Users/matth/downloads/pixil-frame-0 (68).png")
    if dire == 1:
       player = pygame.image.load("C://Users/matth/downloads/pixil-frame-0 (69).png")
    if dire == 2:
        player = pygame.image.load("C://Users/matth/downloads/pixil-frame-0 (70).png")
    s.blit(player, (x,y))
    pygame.display.update()
    if not player_rect.colliderect(road) or player_rect.colliderect(enemy1) or player_rect.colliderect(enemy2) or player_rect.colliderect(enemy3):
        run = False
unrun = True
while unrun:
    mouse = pygame.mouse.get_pos()
    mouserect = pygame.draw.rect(s, (0, 255, 0), (mouse[0], mouse[1], 10, 10))
    s.fill((0, 0, 0))
    again_rect = pygame.draw.rect(s, (0, 255, 0), (center_x-100, center_y, 170, 60))
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if again_rect.colliderect(mouserect):
                if audio_start == True:
                      mixer.music.load("C:/Users/matth/Downloads/car-door-close,-start-engine-and-drive-sound-effect-made-with-Voicemod.mp3") 
                      mixer.music.set_volume(0.7) 
                      mixer.music.play()
                else:
                      pass
                x = 100
                y = 100
                vel = 3
                drag = 0.3
                dire = 0
                line_y = 0
                score = 0
                line1_y = 200
                line2_y = 400
                main_enemy_y = line_y
                list1 = [460, 560, 500, 450]
                enemy_x1 = choice(list1)
                enemy_x2 = choice(list1)
                enemy_x3 = choice(list1)
                run2 = True
                unrun = False
    s.blit(death_text, (center_x-100, center_y-100))
    s.blit(play_text, (center_x-100, center_y))
    pygame.display.flip()
while run2:
    font = pygame.font.SysFont("Arial", 18)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    key = pygame.key.get_pressed()
    mouse = pygame.mouse.get_pos()
    if key[pygame.K_LEFT]:
        x -= vel
        dire = 1
    elif key[pygame.K_RIGHT]:
        x += vel
        dire = 2
    else:
        dire = 0
    s.fill((0, 200, 0))
    main_enemy_y = line_y
    if line_y < 600:
       line_y += (vel + 1)
    else:
        line_y = 0
        main_enemy_y = line_y
        score += score_adder
        enemy_x1 = choice(list1)
        enemy_x2 = choice(list1)
        enemy_x3 = choice(list1)
    if line1_y < 600:
       line1_y += (vel + 1)
    else:
        line1_y = 0
    if line2_y < 600:
       line2_y += (vel + 1)
    else:
        line2_y = 0
    player_rect = pygame.draw.rect(s, (255,0,0), (x+425,y+345,30, 60))
    s.fill((0, 200, 0))
    fps = str(int(clock.get_fps()))
    pygame.display.set_caption("FPS:%s" % (fps))
    font = pygame.font.Font('freesansbold.ttf', 32)
    clock.tick(120)
    road = pygame.draw.rect(s, (0,0,0), (450, -100, 200, 800))
    score_text = font.render("score:%s" % (score), True, (255, 255, 255))
    s.blit(score_text, (0, 0))
    lines = pygame.draw.rect(s, (255,255,255), (530, line_y, 10, 70))
    enemy1 = pygame.draw.rect(s, (255,0,0), (enemy_x1,main_enemy_y,30,50))
    enemy2 = pygame.draw.rect(s, (255,0,0), (enemy_x2,main_enemy_y,30,50))
    enemy3 = pygame.draw.rect(s, (255,0,0), (enemy_x3,main_enemy_y,30,50))
    lines = pygame.draw.rect(s, (255,255,255), (530, line1_y, 10, 70))
    lines = pygame.draw.rect(s, (255,255,255), (530, line2_y, 10, 70))
    if dire == 0:
       player = pygame.image.load("C://Users/matth/downloads/pixil-frame-0 (68).png")
    if dire == 1:
       player = pygame.image.load("C://Users/matth/downloads/pixil-frame-0 (69).png")
    if dire == 2:
        player = pygame.image.load("C://Users/matth/downloads/pixil-frame-0 (70).png")
    s.blit(player, (x,y))
    pygame.display.update()
    if not player_rect.colliderect(road) or player_rect.colliderect(enemy1) or player_rect.colliderect(enemy2) or player_rect.colliderect(enemy3):
           run2 = False
unrun2 = True
already = False
while unrun2:
           if already == False:
              pygame.display.quit()
              s2 = pygame.display.set_mode((1100, 600))
              pygame.display.set_caption("game over")
           already = True
           pygame.font.init()
           s2.fill((0,0,0))
           death2_text = font.render('game over', True, (255,255,255))
           s2.blit(death2_text, (center_x, center_y))
           pygame.display.update()
pygame.quit()
