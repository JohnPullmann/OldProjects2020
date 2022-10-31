from typing import List

import pygame
import sys
import random
pygame.init()
#settings
width = 800
height = 600
number_enemy = 8
enemy_list = []
fps = pygame.time.Clock()
g = 1
score = 0
time = pygame.time.get_ticks
b_type = 'w'
num_b = 0
num_l = []
ww = 0
color_b = (250, 250, 3)
wb_n = 0
tb_n = 0
#colurs
blue = (0, 255 , 0)
red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)
background_colour = black
#player
player_movement_speed = 35
player_size = [50, 50]
player_x = width / 2
player_y = height - player_size[1] - 20
player_position = [player_x, player_y]
#enemy
enemy_size = [20, 50]
enemy_position = [random.randint(0, width - enemy_size[0]), random.randint(0, 50)]
enemy_movement_speed = 3
default_s = enemy_movement_speed
#text
myfond = pygame.font.SysFont('monospace', 35)
#create enemy
class c_enemy:
    def __init__(self, name, enemy_size, enemy_position, enemy_movement_speed):
        self.name = name
        self.p = enemy_position
        self.s = enemy_size
        self.m = enemy_movement_speed
class boost:
    def __init__(self, colour, position, radius, type):
        self.colour = colour
        self.position = position
        self.radius = radius
        self.type = type
def create_e(g, enemy_size, enemy_movement_speed):
    if random.randint(1, 1000) < 30:
        a = g
        a = 'e' + str(a)
        a = c_enemy(a, enemy_size, [random.randint(0, width - enemy_size[0]), 0], enemy_movement_speed)
        enemy_list.append(a)
        return True
#speed increasing
def dificulty(score, enemy_movement_speed, default_s):
    enemy_movement_speed = (score+(default_s*25))/25
    return enemy_movement_speed

#function of detection
def colision(player_position, enemy_position, player_size, enemy_size):
    e_x = enemy_position[0]
    e_y = enemy_position[1]
    if True == (e_y + enemy_size[0] >= player_y and e_y + enemy_size[0] <= player_y + player_size[1]) and True == (e_x + enemy_size[0] >= player_x and e_x <= player_x + player_size[0]):
        return True
#create boosts
def col_boost(boost_name, player_position, boost_position, player_size, radius, type, list_boost, ww, tb_n, wb_n):
    b_x = boost_position[0]
    if True == (player_x > b_x - radius - 10 / 2 and player_x < b_x + radius + 10 / 2) or True == (player_x + player_size[0] < b_x + radius + 10 / 2 and player_x + player_size[0] > b_x - radius - 10 / 2):
        list_boost.remove(boost_name)
        if boost_name.type == 'w':
            if ww != 1:
                ww = 1
                tb_n = 0
                player_size[0] = 65
        if boost_name.type == 't':
            if ww == 1:
                ww = 0
                wb_n = 0
                player_size[0] = 35
    return list_boost, player_size, ww, tb_n, wb_n



game_over = False
screen = pygame.display.set_mode((width, height))
while not game_over:
    for event in pygame.event.get():
        #detection of keys
        if event.type == pygame.QUIT:
            sys.exit()
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_LEFT or event.key == pygame.K_a:
        #         if player_x - player_size[0] > 0:
        #             player_x -= player_movement_speed
        #         else:
        #             player_x = 0
        #     elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        #         if player_x + player_size[0] < wight - 50:
        #             player_x += player_movement_speed
        #         else: player_x = wight - player_size[0]
    key_pressed = pygame.key.get_pressed()
    if key_pressed[pygame.K_LEFT]:
        player_x -= 3
    if key_pressed[pygame.K_RIGHT]:
        player_x += 3
    player_position = [player_x, player_y]
    screen.fill(background_colour)
    enemy_movement_speed = dificulty(score, enemy_movement_speed, default_s)
    if g < number_enemy + 1:
        if True == create_e(g, enemy_size, enemy_movement_speed):
            g += 1
    #enemy movement + player movement
    for c in enemy_list:
        if c.p[1] >= 0 and c.p[1] < width:
            c.p[1] += enemy_movement_speed
        else:
            c.p[0] = random.randint(0, width - c.s[0])
            c.p[1] = random.randint(0, 50)
            score += 1
        if colision(player_position, c.p, player_size, c.s):
            game_over = True
            print('your score was: ' + str(score))
            print('your time was: ' + str(round(pygame.time.get_ticks()/ 1000, 1)))

            break
    text1 = 'Score: ' + str(score)
    label = myfond.render(text1, 1, white)
    screen.blit(label, (width - 240, height - 40))

    text2 = 'Time: ' + str(round(pygame.time.get_ticks()/ 1000, 1))
    label2 = myfond.render(text2, 1, white)
    screen.blit(label2, (40, height - 40))
    if random.randint(1, 200) < 10:
        if random.randint(1, 100) <= 50 and ww != 1 and wb_n != 1:
            color_b = (30, 125, 200)
            b_type = 'w'
            wb_n = 1
        if random.randint(1, 100) > 50 and ww == 1 and tb_n != 1:
            color_b = (122, 26, 122)
            b_type = 't'
            tb_n = 1
        if color_b != (250, 250, 3):
            num_b += 1
            num_b_r = str(num_b) + 'b'
            num_b_r = boost(color_b, (random.randint(50, width - 50), height - 40), 13, b_type)
            num_l.append(num_b_r)
        color_b = (250, 250, 3)
    for x in num_l:
        pygame.draw.circle(screen, x.colour, x.position, x.radius)
    for z in num_l:
        num_l, player_size, ww, tb_n, wb_n = col_boost(z, player_position, z.position, player_size, z.radius, z.type, num_l, ww, tb_n, wb_n)
    for b in enemy_list:
        pygame.draw.rect(screen, red, (b.p[0], b.p[1], b.s[0], b.s[1]))
    pygame.draw.rect(screen, blue, (player_position[0], player_position[1], player_size[0], player_size[1]))
    #speed (fps)
    fps.tick(60)
    pygame.display.update()