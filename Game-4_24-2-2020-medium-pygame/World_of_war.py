import pygame
import random
import sys
import time

pygame.init()
pygame.display.init()
#settings
width = 1280
height = 720
screen = pygame.display.set_mode((width, height))
game = True
menu = True
game1 = False
game_over = ''
difficulty = ''
class c_a:
    def __init__(self, health, position, name, action, attack, walk_count, clock, attack_count, pa, ps, pw, m_health, bonus_h, stop):
        self.health = health
        self.position = position
        self.name = name
        self.action = action
        self.attack = attack
        self.walk_count = walk_count
        self.clock = clock
        self.attack_count = attack_count
        self.pa = pa
        self.ps = ps
        self.pw = pw
        self.m_health = m_health
        self.bonus_h = bonus_h
        self.stop = stop
class upgrade:
    def __init__(self, name, price, position1, position2, tn, tv, bonus):
        self.name = name
        self.price = price
        self.position1 = position1
        self.position2 = position2
        self.tn = tn
        self.tv = tv
        self.bonus = bonus

def menu_f(screen, menu, game, game1):
    global difficulty
    global game_over
    background_menu = pygame.image.load('backgrounds/background_menu.png')
    play = pygame.image.load('texts/play.png')
    play2 = pygame.image.load('texts/play2.png')
    controls = pygame.image.load('texts/controls.png')
    controls2 = pygame.image.load('texts/controls2.png')
    win = pygame.image.load('backgrounds/win.png')
    lost = pygame.image.load('backgrounds/lost.png')
    back1 = pygame.image.load('texts/back1.png')
    back2 = pygame.image.load('texts/back2.png')
    instructions = pygame.image.load('backgrounds/instructions.png')
    easy1 = pygame.image.load('texts/easy1.png')
    easy2 = pygame.image.load('texts/easy2.png')
    medium1 = pygame.image.load('texts/medium1.png')
    medium2 = pygame.image.load('texts/medium2.png')
    hard1 = pygame.image.load('texts/hard1.png')
    hard2 = pygame.image.load('texts/hard2.png')
    instructions_m = False
    difficulty_m = pygame.image.load('backgrounds/difficulty_m.png')
    difficulty_m_d = False
    while menu == True:
        mouse = pygame.mouse.get_pos()
        if game_over != '':
            if game_over == 'win':
                screen.blit(win, [0,0])
            if game_over == 'lost':
                screen.blit(lost, [0, 0])
            if mouse[0] > 550 and mouse[0] < 750 and mouse[1] > 500 and mouse[1] < 600:
                screen.blit(back2, [550, 500])
            else:
                screen.blit(back1, [550, 500])
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False
                    menu = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0]:
                        if mouse[0] > 550 and mouse[0] < 750 and mouse[1] > 500 and mouse[1] < 600:
                            game_over = ''
        elif instructions_m == True:
            screen.blit(instructions, [0, 0])
            if mouse[0] > 520 and mouse[0] < 720 and mouse[1] > 320 and mouse[1] < 420:
                screen.blit(back2, [520, 320])
            else:
                screen.blit(back1, [520, 320])
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False
                    menu = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0]:
                        if mouse[0] > 520 and mouse[0] < 720 and mouse[1] > 320 and mouse[1] < 420:
                            instructions_m = False
        elif difficulty_m_d == True:
            screen.blit(difficulty_m, [0,0])
            if mouse[0] > 540 and mouse[0] < 740 and mouse[1] > 580 and mouse[1] < 680:
                screen.blit(back2, [540, 580])
            else:
                screen.blit(back1, [540, 580])
            if mouse[0] > 545 and mouse[0] < 725 and mouse[1] > 230 and mouse[1] < 320:
                screen.blit(easy2, [535, 230])
            else:
                screen.blit(easy1, [535, 230])
            if mouse[0] > 535 and mouse[0] < 735 and mouse[1] > 320 and mouse[1] < 410:
                screen.blit(medium2, [535, 310])
            else:
                screen.blit(medium1, [535, 310])
            if mouse[0] > 545 and mouse[0] < 725 and mouse[1] > 410 and mouse[1] < 495:
                screen.blit(hard2, [535, 400])
            else:
                screen.blit(hard1, [535, 400])
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False
                    menu = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0]:
                        if mouse[0] > 540 and mouse[0] < 740 and mouse[1] > 580 and mouse[1] < 680:
                            difficulty_m_d = False
                        if mouse[0] > 545 and mouse[0] < 725 and mouse[1] > 230 and mouse[1] < 320:
                            difficulty = 'easy'
                            menu = False
                            game1 = True
                        if mouse[0] > 535 and mouse[0] < 735 and mouse[1] > 320 and mouse[1] < 410:
                            difficulty = 'medium'
                            menu = False
                            game1 = True
                        if mouse[0] > 545 and mouse[0] < 725 and mouse[1] > 410 and mouse[1] < 495:
                            difficulty = 'hard'
                            menu = False
                            game1 = True
        else:
            screen.blit(background_menu, [0,0])
            if mouse[0] > 420 and mouse[0] < 720 and mouse[1] > 320 and mouse[1] < 420:
                screen.blit(play2, [520, 320])
            else:
                screen.blit(play, [520, 320])
            if mouse[0] > 480 and mouse[0] < 760 and mouse[1] > 455 and mouse[1] < 530:
                screen.blit(controls2, [470, 430])
            else:
                screen.blit(controls, [470, 430])
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False
                    menu = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0]:
                        if mouse[0] > 520 and mouse[0] < 720 and mouse[1] > 320 and mouse[1] < 420:
                            difficulty_m_d = True
                        if mouse[0] > 520 and mouse[0] < 720 and mouse[1] > 455 and mouse[1] < 530:
                            instructions_m = True
        pygame.display.update()
    return menu, game, game1
def game1_f(width, height, screen, game1, menu, game):
    global difficulty
    global game_over
    player_army = []
    player_army_pos = []
    player_army = []
    money = 50
    enemy_army_pos = []
    enemy_army = []
    enemy_army_number = s1_attack_count = s1_walk_count = clock = xp = 0
    enemy_army_number = 0
    enemy_money = 50
    enemy_xp = 0
    #soldier
    s_health = 40
    s_attack = 10
    s_price = 20
    #archer
    a_health = 10
    a_attack = 10
    a_price = 25
    #tank
    t_health = 80
    t_attack = 5
    t_price = 30
    background = pygame.image.load('backgrounds/background.png')
    p_base = pygame.image.load('other/p_base1.png')
    e_base = pygame.image.load('other/e_base1.png')
    menu_g = pygame.image.load('backgrounds/menu_g.png')
    b_soldier = pygame.image.load('icons/b_soldier.png')
    b_archer = pygame.image.load('icons/b_archer.png')
    b_tank = pygame.image.load('icons/b_tank.png')
    b_soldier2 = pygame.image.load('icons/b_soldier2.png')
    b_archer2 = pygame.image.load('icons/b_archer2.png')
    b_tank2 = pygame.image.load('icons/b_tank2.png')
    b_building1 = pygame.image.load('icons/b_building1.png')
    b_building2 = pygame.image.load('icons/b_building2.png')
    b_building3 = pygame.image.load('icons/b_building3.png')
    s1_stand = pygame.image.load('soldier1/s1_stand.png')
    s1_walk = [pygame.image.load('soldier1/s1_walk1.png'), pygame.image.load('soldier1/s1_walk2.png'),
               pygame.image.load('soldier1/s1_walk3.png'), pygame.image.load('soldier1/s1_walk4.png')]
    s1_attack = [pygame.image.load('soldier1/s1_attack1.png'),pygame.image.load('soldier1/s1_attack2.png'),
                 pygame.image.load('soldier1/s1_attack3.png'),pygame.image.load('soldier1/s1_attack4.png'),
                 pygame.image.load('soldier1/s1_attack5.png'),pygame.image.load('soldier1/s1_attack6.png'),
                 pygame.image.load('soldier1/s1_attack7.png'),pygame.image.load('soldier1/s1_attack8.png'),
                 pygame.image.load('soldier1/s1_attack9.png'),pygame.image.load('soldier1/s1_attack10.png'),]
    a1_stand = pygame.image.load('archer1/a1_stand.png')
    a1_walk = [pygame.image.load('archer1/a1_walk1.png'), pygame.image.load('archer1/a1_walk2.png'),
               pygame.image.load('archer1/a1_walk3.png'), pygame.image.load('archer1/a1_walk4.png')]
    a1_attack = [pygame.image.load('archer1/a1_attack1.png'),pygame.image.load('archer1/a1_attack2.png'),
                 pygame.image.load('archer1/a1_attack3.png'),pygame.image.load('archer1/a1_attack4.png'),
                 pygame.image.load('archer1/a1_attack5.png'),pygame.image.load('archer1/a1_attack6.png'),
                 pygame.image.load('archer1/a1_attack7.png'),pygame.image.load('archer1/a1_attack8.png'),
                 pygame.image.load('archer1/a1_attack9.png'),pygame.image.load('archer1/a1_attack10.png'),]
    t1_stand = pygame.image.load('tank1/t1_stand.png')
    t1_walk = [pygame.image.load('tank1/t1_walk1.png'), pygame.image.load('tank1/t1_walk2.png'),
               pygame.image.load('tank1/t1_walk3.png'), pygame.image.load('tank1/t1_walk4.png')]
    t1_attack = [pygame.image.load('tank1/t1_attack1.png'), pygame.image.load('tank1/t1_attack2.png'),
                 pygame.image.load('tank1/t1_attack3.png'), pygame.image.load('tank1/t1_attack4.png'),
                 pygame.image.load('tank1/t1_attack5.png'), pygame.image.load('tank1/t1_attack6.png'),
                 pygame.image.load('tank1/t1_attack7.png'), pygame.image.load('tank1/t1_attack8.png'),
                 pygame.image.load('tank1/t1_attack9.png'), pygame.image.load('tank1/t1_attack10.png'), ]
    s_warrior = pygame.image.load('labels/s_warrior.png')
    s_archer = pygame.image.load('labels/s_archer.png')
    s_knight = pygame.image.load('labels/s_knight.png')
    sh1 = pygame.image.load('icons/sh1.png')
    sh2 = pygame.image.load('icons/sh2.png')
    sh3 = pygame.image.load('icons/sh3.png')
    sd1 = pygame.image.load('icons/sd1.png')
    sd2 = pygame.image.load('icons/sd2.png')
    sd3 = pygame.image.load('icons/sd3.png')
    ah1 = pygame.image.load('icons/ah1.png')
    ah2 = pygame.image.load('icons/ah2.png')
    ah3 = pygame.image.load('icons/ah3.png')
    ad1 = pygame.image.load('icons/ad1.png')
    ad2 = pygame.image.load('icons/ad2.png')
    ad3 = pygame.image.load('icons/ad3.png')
    kh1 = pygame.image.load('icons/kh1.png')
    kh2 = pygame.image.load('icons/kh2.png')
    kh3 = pygame.image.load('icons/kh3.png')
    kd1 = pygame.image.load('icons/kd1.png')
    kd2 = pygame.image.load('icons/kd2.png')
    kd3 = pygame.image.load('icons/kd3.png')
    hp1 = pygame.image.load('icons/hp1.png')
    hp2 = pygame.image.load('icons/hp2.png')
    hp3 = pygame.image.load('icons/hp3.png')
    income1 = pygame.image.load('icons/income1.png')
    income2 = pygame.image.load('icons/income2.png')
    income3 = pygame.image.load('icons/income3.png')
    b_us = pygame.image.load('labels/b_us.png')
    b_ua = pygame.image.load('labels/b_ua.png')
    b_uk = pygame.image.load('labels/b_uk.png')
    b_ui = pygame.image.load('labels/b_ui.png')
    b_uh = pygame.image.load('labels/b_uh.png')
    income_bonus = 0
    hp_bonus = 0
    income_u = 1
    hp_u = 1
    shu = 1
    sdu = 1
    ahu = 1
    adu = 1
    khu = 1
    kdu = 1
    kh_bonus = 0
    kd_bonus = 0
    ah_bonus = 0
    ad_bonus = 0
    sh_bonus = 0
    sd_bonus = 0
    background_position = [0, 0]
    p_base_position = [0, 380]
    e_base_position = [2600, 380]
    p_base_health = 100
    e_base_health = 100
    objects = [p_base_position, e_base_position, background_position]
    fps = pygame.time.Clock()
    myfond = pygame.font.SysFont('monospace', 30)
    range = 20
    range_b = 280
    range_b2 = 50
    max = 10
    upgrades = {'sh1': [40, [990, 10], [1040, 60], shu, 1, 0.25],
                'sh2': [50, [990, 10], [1040, 60], shu, 2, 0.50],
                'sh3': [60, [990, 10], [1040, 60], shu, 3, 0.75],
                'sd1': [40, [990, 65], [1040, 115], sdu, 1, 0.25],
                'sd2': [50, [990, 65], [1040, 115], sdu, 2, 0.50],
                'sd3': [60, [990, 65], [1040, 115], sdu, 3, 0.75],
                'ah1': [40, [1060, 10], [1110, 60], ahu, 1, 0.25],
                'ah2': [50, [1060, 10], [1110, 60], ahu, 2, 0.50],
                'ah3': [60, [1060, 10], [1110, 60], ahu, 3, 0.75],
                'ad1': [40, [1060, 65], [1110, 115], adu, 1, 0.25],
                'ad2': [50, [1060, 65], [1110, 115], adu, 2, 0.50],
                'ad3': [60, [1060, 65], [1110, 115], adu, 3, 0.75],
                'kh1': [40, [1130, 10], [1180, 60], khu, 1, 0.25],
                'kh2': [50, [1130, 10], [1180, 60], khu, 2, 0.50],
                'kh3': [60, [1130, 10], [1180, 60], khu, 3, 0.75],
                'kd1': [40, [1130, 65], [1180, 115], kdu, 1, 0.25],
                'kd2': [50, [1130, 65], [1180, 115], kdu, 2, 0.50],
                'kd3': [60, [1130, 65], [1180, 115], kdu, 3, 0.75],
                'income1': [50, [1200, 10], [1250, 60], income_u, 1, 0.25],
                'income2': [75, [1200, 10], [1250, 60], income_u, 2, 0.50],
                'income3': [100, [1200, 10], [1250, 60], income_u, 3, 0.75],
                'hp1': [30, [1200, 65], [1250, 115], hp_u, 1, 0.25],
                'hp2': [50, [1200, 65], [1250, 115], hp_u, 2, 0.50],
                'hp3': [70, [1200, 65], [1250, 115], hp_u, 3, 0.75]
                }
    upgradeT = []
    for key, value in upgrades.items():
        upgrade1 = upgrade(key, value[0], value[1], value[2], value[3], value[4], value[5])
        upgradeT.append(upgrade1)
    #docasna obtiaznost (zrusit)
    # difficulty = 'easy'
    while game1 == True:
        max = 10
        if difficulty == 'easy':
            # income
            bonus1 = 0
            # health
            bonus2 = 0
            # damage
            bonus3 = 0
        elif difficulty == 'medium':
            bonus1 = 0.05
            bonus2 = 0.05
            bonus3 = 0.05
        elif difficulty == 'hard':
            bonus1 = 0.08
            bonus2 = 0.10
            bonus3 = 0.10
        player_army_number = len(player_army)
        time = pygame.time.get_ticks() / 1000
        money += 0.060 + income_bonus
        enemy_money += 0.045 + bonus1
        mouse = pygame.mouse.get_pos()
        screen.blit(background, background_position)
        screen.blit(p_base, p_base_position)
        pygame.draw.rect(screen, (200, 0, 0),
                         (p_base_position[0] + 25, p_base_position[1] - 50, int(((p_base_health+ hp_bonus)*250)/(100+hp_bonus)), 30))
        screen.blit(e_base, e_base_position)
        pygame.draw.rect(screen, (200, 0, 0),
                         (e_base_position[0] + 25, e_base_position[1] - 50, int(2.5 * e_base_health), 30))
        for x in upgradeT:
            if str(str(list(x.name)[0]+list(x.name)[1])) == 'hp':
                x.tn = hp_u
            if str(str(list(x.name)[0]+list(x.name)[1])) == 'in':
                x.tn = income_u
            if str(str(list(x.name)[0]+list(x.name)[1])) == 'sh':
                x.tn = shu
            if str(str(list(x.name)[0]+list(x.name)[1])) == 'sd':
                x.tn = sdu
            if str(str(list(x.name)[0]+list(x.name)[1])) == 'ah':
                x.tn = ahu
            if str(str(list(x.name)[0]+list(x.name)[1])) == 'ad':
                x.tn = adu
            if str(str(list(x.name)[0]+list(x.name)[1])) == 'kh':
                x.tn = khu
            if str(str(list(x.name)[0]+list(x.name)[1])) == 'kd':
                x.tn = kdu
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game1 = False
                game = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game1 = False
                    menu = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    if len(player_army) < 10:
                        if range_b > 260:
                            range_b -= 2
                        else:
                            range_b = 280
                        if mouse[0] > 25 and mouse[0] < 75 and mouse[1] > 55 and mouse[1] < 105 and money - s_price > 0:
                            #soldier
                            name = 's'+ str(player_army_number +1) + 'p'
                            name = c_a(s_health + sh_bonus, [p_base_position[0]+range_b, p_base_position[1]+170], name, 'walk', s_attack + sd_bonus, s1_walk_count, clock, s1_attack_count,s1_attack,s1_stand,s1_walk, s_health, sh_bonus, False)
                            objects.append(name.position)
                            player_army_pos.append(name.position)
                            player_army.append(name)
                            money -= s_price
                        if mouse[0] > 85 and mouse[0] < 135 and mouse[1] > 55 and mouse[1] < 105 and money - a_price > 0:
                            #archer
                            name = 'a' + str(player_army_number + 1) + 'p'
                            name = c_a(a_health+ ah_bonus, [p_base_position[0] + range_b, p_base_position[1] + 170], name, 'walk',
                                       a_attack+ ad_bonus, s1_walk_count, clock, s1_attack_count, a1_attack, a1_stand, a1_walk, a_health, ah_bonus, False)
                            player_army_pos.append(name.position)
                            objects.append(name.position)
                            player_army.append(name)
                            money -= a_price
                        if mouse[0] > 145 and mouse[0] < 195 and mouse[1] > 55 and mouse[1] < 105 and money - t_price > 0:
                            #tank
                            name = 't' + str(player_army_number + 1) + 'p'
                            name = c_a(t_health+ kh_bonus, [p_base_position[0] + range_b, p_base_position[1] + 170], name, 'walk',
                                       t_attack+ kd_bonus, s1_walk_count, clock, s1_attack_count, t1_attack, t1_stand, t1_walk, t_health, kh_bonus, False)
                            player_army_pos.append(name.position)
                            objects.append(name.position)
                            player_army.append(name)
                            money -= t_price
                    if mouse[0] > 540 and mouse[0] < 590 and mouse[1] > 55 and mouse[1] < 105:
                        print('building1')
                    if mouse[0] > 600 and mouse[0] < 650 and mouse[1] > 55 and mouse[1] < 105:
                        print('building2')
                    if mouse[0] > 660 and mouse[0] < 710 and mouse[1] > 55 and mouse[1] < 105:
                        print('building3')
                    for x in upgradeT:
                        if mouse[0] > x.position1[0] and mouse[0] < x.position2[0] and mouse[1] > x.position1[1] and mouse[1] < x.position2[1] and x.tn == x.tv and money > x.price:
                            if str(str(list(x.name)[0]+list(x.name)[1])) == 'in':
                                income_u = x.tv +1
                                income_bonus = 0.06 * x.bonus
                            if str(str(list(x.name)[0]+list(x.name)[1])) == 'hp':
                                hp_u = x.tv +1
                                hp_bonus = p_base_health * x.bonus
                            if str(str(list(x.name)[0]+list(x.name)[1])) == 'sh':
                                shu = x.tv +1
                                sh_bonus = s_health * x.bonus
                            if str(str(list(x.name)[0]+list(x.name)[1])) == 'sd':
                                sdu = x.tv + 1
                                sd_bonus = s_attack * x.bonus
                            if str(str(list(x.name)[0]+list(x.name)[1])) == 'ah':
                                ahu = x.tv + 1
                                ah_bonus = a_health * x.bonus
                            if str(str(list(x.name)[0]+list(x.name)[1])) == 'ad':
                                adu = x.tv + 1
                                ad_bonus = a_attack * x.bonus
                            if str(str(list(x.name)[0]+list(x.name)[1])) == 'kh':
                                khu = x.tv + 1
                                kh_bonus = t_health * x.bonus
                            if str(str(list(x.name)[0]+list(x.name)[1])) == 'kd':
                                kdu = x.tv + 1
                                kd_bonus = t_attack * x.bonus
                            money -= x.price
                            break
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_LEFT] and p_base_position[0] < 0:
            for x in objects:
                x[0] += 20
        if key_pressed[pygame.K_RIGHT] and e_base_position[0] > 990:
            for x in objects:
                x[0] -= 20
        #player move
        for x in player_army:
            target = ''
            if mouse[0] > x.position[0] and mouse[0] < x.position[0]+100 and mouse[1] > x.position[1] and mouse[1] < x.position[1]+150:
                # pygame.draw.rect(screen, (200, 0, 0), (x.position[0]+5, x.position[1],int(x.health*70/x.m_health),5))
                pygame.draw.rect(screen, (200, 0, 0),(x.position[0]+5, x.position[1],int(((x.health) * 70) / (x.m_health  + x.bonus_h)), 5))
            if list(x.name)[0] == 'a':
                range = 160
            for y in objects:
                if x.position != y:
                    if x.position[0] + 100 - y[0] > -range-150 and x.position[0] + 100 - y[0] < 0:
                        if y == e_base_position:
                            x.action = 'attack'
                            target = 'e_base'
                            break
                        else:
                            x.action = 'walk'
                    if  (y != p_base_position and y != e_base_position and x.position[0] + 100 - y[0] > -range and x.position[0] + 100 - y[0] < 0 and y not in player_army_pos):
                        x.action = 'attack'
                        target = enemy_army[0]
                        break
                    else:
                        x.action = 'walk'
                else:
                    x.action = 'walk'
            if x.action == 'walk':
                go = 1
                for y in objects:
                    if x.position != y:
                        if x.position[0] +100 - y[0] > -20 and x.position[0] +100 - y[0] < 0:
                            go  = 0
                if go == 1 and x.stop == False:
                    x.position[0] += 2
                    x.clock +=1
                    if x.walk_count + 1 >= 5:
                        x.walk_count = 0
                    if x.clock > 6:
                        x.clock = 0
                        x.walk_count += 1
                    if x.walk_count + 1 >= 5:
                        x.walk_count = 0
                    screen.blit(x.pw[x.walk_count], x.position)
                else:
                    screen.blit(x.ps, x.position)
            elif x.action == 'attack':
                x.clock += 1
                if x.attack_count + 1 >= 11:
                    x.attack_count = 0
                    x.clock = -40
                if x.clock > 2:
                    x.clock = 0
                    x.attack_count += 1
                if x.attack_count + 1 >= 11:
                    x.attack_count = 0
                    x.clock = -40
                    if target == 'e_base':
                        e_base_health -= x.attack
                    else:
                        target.health -= x.attack
                screen.blit(x.pa[x.attack_count], x.position)
            range = 20
        ###
        for x in player_army:
            if x.position[0] > p_base_position[0] + 1200:
                max = 3
        #computer move
        typ = random.randint(0, 100)
        if enemy_money > 30 and len(enemy_army) < max:
            if range_b2 > 30:
                range_b2 -= 2
            else:
                range_b2 = 50
            if typ < 40 and enemy_money - s_price > 0:
                enemy_money -= s_price
                name = 's' + str(enemy_army_number + 1) + 'e'
                name = c_a(s_health + (s_health * bonus2), [e_base_position[0] - range_b2, e_base_position[1] + 170], name, 'walk', s_attack + (s_attack * bonus3),
                           s1_walk_count, clock, s1_attack_count, s1_attack, s1_stand, s1_walk, s_health + (s_health * bonus2), 0, False)
                enemy_army_pos.append(name.position)
                objects.append(name.position)
                enemy_army.append(name)
            elif typ > 75 and enemy_money - a_price > 0:
                enemy_money -= a_price
                name = 'a' + str(enemy_army_number + 1) + 'e'
                name = c_a(a_health + (a_health * bonus2), [e_base_position[0] - range_b2, e_base_position[1] + 170], name, 'walk', a_attack + (a_health * bonus3),
                           s1_walk_count, clock, s1_attack_count, a1_attack, a1_stand, a1_walk, a_health + (a_health * bonus2), 0, False)
                enemy_army_pos.append(name.position)
                objects.append(name.position)
                enemy_army.append(name)
            elif enemy_money - t_price > 0:
                enemy_money -= a_price
                name = 't' + str(enemy_army_number + 1) + 'e'
                name = c_a(t_health + (t_health * bonus2), [e_base_position[0] - range_b2, e_base_position[1] + 170], name, 'walk', t_attack + (t_health * bonus3),
                           s1_walk_count, clock, s1_attack_count, t1_attack, t1_stand, t1_walk, t_health + (t_health * bonus2), 0,  False)
                enemy_army_pos.append(name.position)
                objects.append(name.position)
                enemy_army.append(name)
        for x in enemy_army:
            if mouse[0] > x.position[0] and mouse[0] < x.position[0]+100 and mouse[1] > x.position[1] and mouse[1] < x.position[1]+150:
                pygame.draw.rect(screen, (200, 0, 0), (x.position[0]+20, x.position[1],int(x.health*70/x.m_health),5))
            target = ''
            if list(x.name)[0] == 'a':
                range = 140
            for y in objects:
                if x.position != y:
                    if x.position[0] - (y[0]+ 300) < range and x.position[0] - (y[0] + 300) > 0:
                        if y == p_base_position:
                            x.action = 'attack'
                            target = 'p_base'
                            break
                        else:
                            x.action = 'walk'
                    elif (y != p_base_position and y != e_base_position and x.position[0] - (y[0] + 100) < range and
                          x.position[0] - (y[0] + 100) > 0 and y not in enemy_army_pos):
                        x.action = 'attack'
                        target = player_army[0]
                        break
                    else:
                        x.action = 'walk'
                else:
                    x.action = 'walk'
            if x.action == 'walk':
                go = 1
                for y in objects:
                    if x.position != y:
                        if x.position[0] - (y[0] + 100) < 20 and x.position[0] - (y[0] +100) > 0:
                            go  = 0
                if go == 1 and x.stop == False:
                    x.position[0] -= 2
                    x.clock +=1
                    if x.walk_count + 1 >= 5:
                        x.walk_count = 0
                    if x.clock > 6:
                        x.clock = 0
                        x.walk_count += 1
                    if x.walk_count + 1 >= 5:
                        x.walk_count = 0
                    screen.blit(pygame.transform.flip(x.pw[x.walk_count], True, False), x.position)
                else:
                    screen.blit(pygame.transform.flip(x.ps, True, False), x.position)
            elif x.action == 'attack':
                x.clock += 1
                if x.attack_count + 1 >= 11:
                    x.attack_count = 0
                    x.clock = -45
                if x.clock > 3:
                    x.clock = 0
                    x.attack_count += 1
                if x.attack_count + 1 >= 11:
                    x.attack_count = 0
                    x.clock = -45
                    if target == 'p_base':
                        p_base_health -= x.attack
                    else:
                        target.health -= x.attack
                screen.blit(pygame.transform.flip(x.pa[x.attack_count], True, False), x.position)
            range = 20
        ###
        #death of soldiers
        for x in player_army:
            if x.health < 1:
                objects.remove(x.position)
                player_army_pos.remove(x.position)
                player_army.remove(x)
                enemy_money += 5
                for x in player_army:
                    x.clock = -10
                for x in enemy_army:
                    x.clock = -10
        for x in enemy_army:
            if x.health < 1:
                objects.remove(x.position)
                enemy_army_pos.remove(x.position)
                enemy_army.remove(x)
                money += 10
                for x in player_army:
                    x.clock = 0
                for x in enemy_army:
                    x.clock = 0
        ###
        #waiting
        for x in player_army:
            for y in player_army:
                if x.position[0] == y.position[0] and x.name != y.name:
                    x.position[0] -= random.randint(0,3)
                if y.position != x.position and x.position[0] < y.position[0] and x.position[0]+140 > y.position[0]:
                    x.stop = True
                    break
                else:
                    x.stop = False
        for x in enemy_army:
            for y in enemy_army:
                if x.position[0] == y.position[0] and x.name != y.name:
                    x.position[0] += random.randint(0,3)
                if y.position != x.position and x.position[0] > y.position[0] and x.position[0]-140 < y.position[0]:
                    x.stop = True
                    break
                else:
                    x.stop = False
        ###
        #END
        if p_base_health < 1 or e_base_health < 1:
            p_base = pygame.image.load('other/p_base2.png')
            e_base = pygame.image.load('other/e_base2.png')
            if p_base_health < 1:
                game_over = 'lost'
            else:
                game_over = 'win'
            game1 = False
            menu = True
        ###
        screen.blit(menu_g, [0, 0])
        # upgrades
        if shu == 1:
            screen.blit(sh1,[990,10])
        elif shu == 2:
            screen.blit(sh2, [990, 10])
        elif shu == 3:
            screen.blit(sh3, [990, 10])
        if sdu == 1:
            screen.blit(sd1,[990,65])
        elif sdu == 2:
            screen.blit(sd2, [990, 65])
        elif sdu == 3:
            screen.blit(sd3, [990, 65])
        #a
        if ahu == 1:
            screen.blit(ah1,[1060,10])
        elif ahu == 2:
            screen.blit(ah2, [1060, 10])
        elif ahu == 3:
            screen.blit(ah3, [1060, 10])
        if adu == 1:
            screen.blit(ad1,[1060,65])
        elif adu == 2:
            screen.blit(ad2, [1060, 65])
        elif adu == 3:
            screen.blit(ad3, [1060, 65])
        #k
        if khu == 1:
            screen.blit(kh1,[1130,10])
        elif khu == 2:
            screen.blit(kh2, [1130, 10])
        elif khu == 3:
            screen.blit(kh3, [1130, 10])
        if kdu == 1:
            screen.blit(kd1,[1130,65])
        elif kdu == 2:
            screen.blit(kd2, [1130, 65])
        elif kdu == 3:
            screen.blit(kd3, [1130, 65])
        #income + hp_base
        if income_u == 1:
            screen.blit(income1,[1200,10])
        elif income_u == 2:
            screen.blit(income2, [1200, 10])
        elif income_u == 3:
            screen.blit(income3, [1200, 10])
        if hp_u == 1:
            screen.blit(hp1,[1200,65])
        elif hp_u == 2:
            screen.blit(hp2, [1200, 65])
        elif hp_u == 3:
            screen.blit(hp3, [1200, 65])
        #stitky
        if mouse[0] > 990 and mouse[0] < 1040 and mouse[1] > 10 and mouse[1] < 60:
            screen.blit(b_us,[mouse[0]+10, mouse[1]+15])
        if mouse[0] > 990 and mouse[0] < 1040 and mouse[1] > 65 and mouse[1] < 115:
            screen.blit(b_us,[mouse[0]+10, mouse[1]+15])
        if mouse[0] > 1060 and mouse[0] < 1110 and mouse[1] > 10 and mouse[1] < 60:
            screen.blit(b_ua,[mouse[0]+10, mouse[1]+15])
        if mouse[0] > 1060 and mouse[0] < 1110 and mouse[1] > 65 and mouse[1] < 115:
            screen.blit(b_ua,[mouse[0]+10, mouse[1]+15])
        if mouse[0] > 1130 and mouse[0] < 1180 and mouse[1] > 10 and mouse[1] < 60:
            screen.blit(b_uk,[mouse[0]-200, mouse[1]+15])
        if mouse[0] > 1130 and mouse[0] < 1180 and mouse[1] > 65 and mouse[1] < 115:
            screen.blit(b_uk,[mouse[0]-200, mouse[1]+15])
        if mouse[0] > 1200 and mouse[0] < 1250 and mouse[1] > 10 and mouse[1] < 60:
            screen.blit(b_ui,[mouse[0]-200, mouse[1]+15])
        if mouse[0] > 1200 and mouse[0] < 1250 and mouse[1] > 65 and mouse[1] < 115:
            screen.blit(b_uh,[mouse[0]-200, mouse[1]+15])

        ###
        screen.blit(b_soldier, [25,55])
        screen.blit(b_archer, [85,55])
        screen.blit(b_tank, [145, 55])
        # screen.blit(b_building1, [540,55])
        # screen.blit(b_building2, [600,55])
        # screen.blit(b_building3, [660,55])
        text1 = str(int(round(money, 0)))
        label1 = myfond.render(text1, 1, (0, 0, 0))
        screen.blit(label1, (415, 15))
        if mouse[0] > 25 and mouse[0] < 75 and mouse[1] > 55 and mouse[1] < 105:
            screen.blit(b_soldier2, [25, 55])
            screen.blit(s_warrior, [mouse[0]+10, mouse[1]+15])
        if mouse[0] > 85 and mouse[0] < 135 and mouse[1] > 55 and mouse[1] < 105:
            screen.blit(b_archer2, [85, 55])
            screen.blit(s_archer, [mouse[0]+10, mouse[1]+15])
        if mouse[0] > 145 and mouse[0] < 195 and mouse[1] > 55 and mouse[1] < 105:
            screen.blit(b_tank2, [145, 55])
            screen.blit(s_knight, [mouse[0]+10, mouse[1]+15])
        fps.tick(60)
        pygame.display.update()
    return game, game1, menu
while game == True:
    if menu == False and game1 == False:
        game = False
    if menu == True:
        menu, game, game1 = menu_f(screen, menu, game, game1)
    if game1 == True:
        game, game1, menu = game1_f(width, height, screen, game1, menu, game)




