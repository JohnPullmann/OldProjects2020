import pygame
import random
import sys
import time

pygame.init()
wight = 1000
hight = 700
screen = pygame.display.set_mode((wight, hight))
pygame.display.set_caption('Piškvorky')
setting = pygame.image.load('images/SETTINGS.jpg')
board_clean = pygame.image.load('images/CLEAR.jpg')
T3x3_image_f = pygame.image.load('images/3x3.png')
T4x4_image_f = pygame.image.load('images/4x4.png')
T5x5_image_f = pygame.image.load('images/5x5.png')
T3x3_image_t = pygame.image.load('images/3x3g.png')
T4x4_image_t = pygame.image.load('images/4x4g.png')
T5x5_image_t = pygame.image.load('images/5x5g.png')
board_3x3 = pygame.image.load('images/3.jpg')
board_4x4 = pygame.image.load('images/4.jpg')
board_5x5 = pygame.image.load('images/5.jpg')
board_20x20 = pygame.image.load('images/6.png')
X1 = pygame.image.load('images/X.png')
O1 = pygame.image.load('images/O.png')
X2 = pygame.image.load('images/X2.png')
O2 = pygame.image.load('images/O2.png')
X3 = pygame.image.load('images/X3.png')
pygame.display.set_icon(board_3x3)
O3 = pygame.image.load('images/O3.png')
RESET = pygame.image.load('images/RESET.png')
RESET2 = pygame.image.load('images/RESET2.png')
up = pygame.image.load('images/up.png')
down = pygame.image.load('images/down.png')
O4 = pygame.image.load('images/O4.png')
X4 = pygame.image.load('images/X4.png')
T20x20_image_f = pygame.image.load('images/20x20.png')
T20x20_image_t = pygame.image.load('images/20x20g.png')
player1 = 0
player2 = 0
t3x3 = False
t3x3_pos =  [735, 350]
T3x3_ch = 0
t4x4 = False
t4x4_pos =  [860, 350]
T4x4_ch = 0
t5x5 = False
t5x5_pos =  [735, 425]
T5x5_ch = 0
t20x20 = False
t20x20_pos = [860, 425]
T20x20_ch = 0
movesX = []
movesO =  []
move = 'X'
moves = []
append = 0
myfond = pygame.font.SysFont('monospace', 40)
ch3x3 = {'00': '','10': '','20': '',
         '01': '','11': '','21': '',
         '02': '','12': '','22': ''}

ch4x4 = {'00': '','10': '','20': '','30': '',
         '01': '','11': '','21': '','31': '',
         '02': '','12': '','22': '','32': '',
         '03': '','13': '','23': '','33': '',}

ch5x5 = {'00': '','10': '','20': '','30': '','40': '',
         '01': '','11': '','21': '','31': '','41': '',
         '02': '','12': '','22': '','32': '','42': '',
         '03': '','13': '','23': '','33': '','43': '',
         '04': '','14': '','24': '','34': '','44': '',}
chmove = ''

game_over = False
def load_setting(setting, board_clean, t3x3, t4x4, t5x5, T3x3_image_t, T4x4_image_t, T5x5_image_t, T3x3_image_f, T4x4_image_f, T5x5_image_f, board_3x3, board_4x4, board_5x5, t3x3_pos, t4x4_pos, t5x5_pos, T3x3_ch, T4x4_ch, T5x5_ch,t20x20, T20x20_image_t, T20x20_image_f, board_20x20, T20x20_ch):
    screen.blit(setting, [700,0])
    if T3x3_ch == 10:
        T3x3_image_f = pygame.transform.scale(T3x3_image_f, (110, 60))
        T3x3_image_t = pygame.transform.scale(T3x3_image_t, (110, 60))
        t3x3_pos[0] -= 5
        t3x3_pos[1] -= 5
    if T4x4_ch == 10:
        T4x4_image_f = pygame.transform.scale(T4x4_image_f, (110, 60))
        T4x4_image_t = pygame.transform.scale(T4x4_image_t, (110, 60))
        t4x4_pos[0] -= 5
        t4x4_pos[1] -= 5
    if T5x5_ch == 10:
        T5x5_image_f = pygame.transform.scale(T5x5_image_f, (110, 60))
        T5x5_image_t = pygame.transform.scale(T5x5_image_t, (110, 60))
        t5x5_pos[0] -= 5
        t5x5_pos[1] -= 5
    if T20x20_ch == 10:
        T20x20_image_f = pygame.transform.scale(T20x20_image_f, (110, 60))
        T20x20_image_t = pygame.transform.scale(T20x20_image_t, (110, 60))
        t20x20_pos[0] -= 5
        t20x20_pos[1] -= 5
    if T4x4_ch == 10:
        pass
    if T5x5_ch == 10:
        pass
    if t3x3 == True:
        screen.blit(board_3x3, [0, 0])
    elif t4x4 == True:
        screen.blit(board_4x4, [0, 0])
    elif t5x5 == True:
        screen.blit(board_5x5, [0, 0])
    elif t20x20 == True:
        screen.blit(board_20x20, [0, 0])
    else:
        screen.blit(board_clean, [0,0])
    if t3x3 == False:
        screen.blit(T3x3_image_f, t3x3_pos)
    else:
        screen.blit(T3x3_image_t, t3x3_pos)
    if t4x4 == False:
        screen.blit(T4x4_image_f, t4x4_pos)
    else:
        screen.blit(T4x4_image_t, t4x4_pos)
    if t5x5 == False:
        screen.blit(T5x5_image_f, t5x5_pos)
    else:
        screen.blit(T5x5_image_t, t5x5_pos)
    if t20x20 == False:
        screen.blit(T20x20_image_f, t20x20_pos)
    else:
        screen.blit(T20x20_image_t, t20x20_pos)
def r3x3(t3x3, t4x4, t5x5, move, movesO, movesX, ch3x3):
    t3x3 = True
    t4x4 = False
    t5x5 = False
    move = 'X'
    movesO = []
    movesX = []
    ch3x3 = {'00': '', '10': '', '20': '',
             '01': '', '11': '', '21': '',
             '02': '', '12': '', '22': ''}
    return t3x3, t4x4, t5x5, move, movesO, movesX, ch3x3
while game_over ==  False:
    X = X1
    O = O1
    moves.extend(movesX)
    moves.extend(movesO)
    screen.fill((0, 0, 0))
    mouse = pygame.mouse.get_pos()
    if mouse[0] > 735 and mouse[0] < 835 and mouse[1] > 350 and mouse[1] < 400:
        T3x3_ch = 10
    if mouse[0] > 860 and mouse[0] < 960 and mouse[1] > 350 and mouse[1] < 400:
        T4x4_ch = 10
    if mouse[0] > 735 and mouse[0] < 835 and mouse[1] > 425 and mouse[1] < 475:
        T5x5_ch = 10
    if mouse[0] > 860 and mouse[0] < 960 and mouse[1] > 425 and mouse[1] < 475:
        T20x20_ch = 10
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if mouse[0] > 750 and mouse[0] < 950 and mouse[1] > 550 and mouse[1] < 625:
                    movesO = []
                    movesX = []
                    move = 'X'
                    ch3x3 = {'00': '', '10': '', '20': '',
                             '01': '', '11': '', '21': '',
                             '02': '', '12': '', '22': ''}

                    ch4x4 = {'00': '', '10': '', '20': '', '30': '',
                             '01': '', '11': '', '21': '', '31': '',
                             '02': '', '12': '', '22': '', '32': '',
                             '03': '', '13': '', '23': '', '33': '', }

                    ch5x5 = {'00': '', '10': '', '20': '', '30': '', '40': '',
                             '01': '', '11': '', '21': '', '31': '', '41': '',
                             '02': '', '12': '', '22': '', '32': '', '42': '',
                             '03': '', '13': '', '23': '', '33': '', '43': '',
                             '04': '', '14': '', '24': '', '34': '', '44': '', }
                if mouse[0] > 735 and mouse[0] < 835 and mouse[1] > 350 and mouse[1] < 400:
                    t3x3 = True
                    t4x4 = False
                    t5x5 = False
                    t20x20 = False
                    move = 'X'
                    movesO = []
                    movesX = []
                    ch3x3 = {'00': '', '10': '', '20': '',
                             '01': '', '11': '', '21': '',
                             '02': '', '12': '', '22': ''}
                if mouse[0] > 860 and mouse[0] < 960 and mouse[1] > 350 and mouse[1] < 400:
                    t3x3 = False
                    t4x4 = True
                    t5x5 = False
                    t20x20 = False
                    move = 'X'
                    movesO = []
                    movesX = []
                    ch4x4 = {'00': '', '10': '', '20': '', '30': '',
                             '01': '', '11': '', '21': '', '31': '',
                             '02': '', '12': '', '22': '', '32': '',
                             '03': '', '13': '', '23': '', '33': '', }
                if mouse[0] > 735 and mouse[0] < 835 and mouse[1] > 425 and mouse[1] < 475:
                    t3x3 = False
                    t4x4 = False
                    t5x5 = True
                    t20x20 = False
                    move = 'X'
                    movesO = []
                    movesX = []
                    ch5x5 = {'00': '', '10': '', '20': '', '30': '', '40': '',
                             '01': '', '11': '', '21': '', '31': '', '41': '',
                             '02': '', '12': '', '22': '', '32': '', '42': '',
                             '03': '', '13': '', '23': '', '33': '', '43': '',
                             '04': '', '14': '', '24': '', '34': '', '44': '', }
                if mouse[0] > 860 and mouse[0] < 960 and mouse[1] > 425 and mouse[1] < 475:
                    t3x3 = False
                    t4x4 = False
                    t5x5 = False
                    t20x20 = True
                    move = 'X'
                    movesO = []
                    movesX = []
                mouse = list(mouse)
                if mouse[0] > 760 and mouse[0] < 790 and mouse[1] > 80 and mouse[1] < 110 and player1 < 9:
                    player1 += 1
                if mouse[0] > 910 and mouse[0] < 930 and mouse[1] > 80 and mouse[1] < 110 and player2 < 9:
                    player2 += 1
                if mouse[0] > 760 and mouse[0] < 790 and mouse[1] > 110 and mouse[1] < 140:
                    if player1 > 0:
                        player1 -= 1
                if mouse[0] > 910 and mouse[0] < 930 and mouse[1] > 110 and mouse[1] < 140:
                    if player2 > 0:
                        player2 -= 1
                if mouse[0] < 690:
                    if t3x3 == True:
                        mouse[0] = mouse[0] // 230 * 230 + 20
                        mouse[1] = mouse[1] // 230 * 230 + 20
                        chmove = str(mouse[0] // 230) + str(mouse[1] // 230)
                    if t4x4 == True:
                        mouse[0] = mouse[0] // 173 * 173 + 6
                        mouse[1] = mouse[1] // 173 * 173 + 9
                        chmove = str(mouse[0] // 173) + str(mouse[1] // 173)
                    if t5x5 == True:
                        mouse[0] = mouse[0] // 138 * 138 + 6
                        mouse[1] = mouse[1] // 138 * 138 + 6
                        chmove = str(mouse[0] // 138) + str(mouse[1] // 138)
                    if t20x20 == True:
                        mouse[0] = mouse[0] // 35 * 35 + 4
                        mouse[1] = mouse[1] // 35 * 35 + 4
                        chmove = str(mouse[0] // 35) + str(mouse[1] // 35)
                    append = 0
                    for x in moves:
                        if x == mouse:
                            append = 1
                    if append == 0:
                        if move == 'X':
                            movesX.append(mouse)
                            move = 'O'
                            if t3x3 == True:
                                ch3x3[chmove] = 'X'
                            if t4x4 == True:
                                ch4x4[chmove] = 'X'
                            if t5x5 == True:
                                ch5x5[chmove] = 'X'

                        else:
                            movesO.append(mouse)
                            move = 'X'
                            if t3x3 == True:
                                ch3x3[chmove] = 'O'
                            if t4x4 == True:
                                ch4x4[chmove] = 'O'
                            if t5x5 == True:
                                ch5x5[chmove] = 'O'


    load_setting(setting, board_clean, t3x3, t4x4, t5x5, T3x3_image_t, T4x4_image_t, T5x5_image_t, T3x3_image_f, T4x4_image_f, T5x5_image_f, board_3x3, board_4x4, board_5x5, t3x3_pos, t4x4_pos, t5x5_pos, T3x3_ch, T4x4_ch, T5x5_ch, t20x20, T20x20_image_t, T20x20_image_f, board_20x20, T20x20_ch)
    if t3x3 == True:
        X = X1
        O = O1
    if t4x4 == True:
        X = X2
        O = O2
    if t5x5 == True:
        X = X3
        O = O3
    if t20x20 == True:
        X = X4
        O = O4
    if t3x3 == True or t4x4 == True or t5x5 == True or t20x20 == True:
        for x in movesX:
            screen.blit(X, x)
        for y in movesO:
            screen.blit(O, y)
    # check end 3x3
    if t3x3 == True:
        if ch3x3['00'] == 'X' and ch3x3['01'] == 'X' and ch3x3['02'] == 'X':
            t3x3, t4x4, t5x5, move, movesO, movesX, ch3x3 = r3x3(t3x3, t4x4, t5x5, move, movesO, movesX, ch3x3)
            player1 += 1
        if ch3x3['00'] == 'O' and ch3x3['01'] == 'O' and ch3x3['02'] == 'O':
            t3x3, t4x4, t5x5, move, movesO, movesX, ch3x3 = r3x3(t3x3, t4x4, t5x5, move, movesO, movesX, ch3x3)
            player2 += 1
        if ch3x3['10'] == 'X' and ch3x3['11'] == 'X' and ch3x3['12'] == 'X':
            t3x3, t4x4, t5x5, move, movesO, movesX, ch3x3 = r3x3(t3x3, t4x4, t5x5, move, movesO, movesX, ch3x3)
            player1 += 1
        if ch3x3['10'] == 'O' and ch3x3['11'] == 'O' and ch3x3['12'] == 'O':
            t3x3, t4x4, t5x5, move, movesO, movesX, ch3x3 = r3x3(t3x3, t4x4, t5x5, move, movesO, movesX, ch3x3)
            player2 += 1
        if ch3x3['20'] == 'X' and ch3x3['21'] == 'X' and ch3x3['22'] == 'X':
            t3x3, t4x4, t5x5, move, movesO, movesX, ch3x3 = r3x3(t3x3, t4x4, t5x5, move, movesO, movesX, ch3x3)
            player1 += 1
        if ch3x3['20'] == 'O' and ch3x3['21'] == 'O' and ch3x3['22'] == 'O':
            t3x3, t4x4, t5x5, move, movesO, movesX, ch3x3 = r3x3(t3x3, t4x4, t5x5, move, movesO, movesX, ch3x3)
            player2 += 1
        if ch3x3['00'] == 'X' and ch3x3['10'] == 'X' and ch3x3['20'] == 'X':
            t3x3, t4x4, t5x5, move, movesO, movesX, ch3x3 = r3x3(t3x3, t4x4, t5x5, move, movesO, movesX, ch3x3)
            player1 += 1
        if ch3x3['00'] == 'O' and ch3x3['10'] == 'O' and ch3x3['20'] == 'O':
            t3x3, t4x4, t5x5, move, movesO, movesX, ch3x3 = r3x3(t3x3, t4x4, t5x5, move, movesO, movesX, ch3x3)
            player2 += 1
        if ch3x3['01'] == 'X' and ch3x3['11'] == 'X' and ch3x3['21'] == 'X':
            t3x3, t4x4, t5x5, move, movesO, movesX, ch3x3 = r3x3(t3x3, t4x4, t5x5, move, movesO, movesX, ch3x3)
            player1 += 1
        if ch3x3['01'] == 'O' and ch3x3['11'] == 'O' and ch3x3['21'] == 'O':
            t3x3, t4x4, t5x5, move, movesO, movesX, ch3x3 = r3x3(t3x3, t4x4, t5x5, move, movesO, movesX, ch3x3)
            player2 += 1
        if ch3x3['02'] == 'X' and ch3x3['12'] == 'X' and ch3x3['22'] == 'X':
            t3x3, t4x4, t5x5, move, movesO, movesX, ch3x3 = r3x3(t3x3, t4x4, t5x5, move, movesO, movesX, ch3x3)
            player1 += 1
        if ch3x3['02'] == 'O' and ch3x3['12'] == 'O' and ch3x3['22'] == 'O':
            t3x3, t4x4, t5x5, move, movesO, movesX, ch3x3 = r3x3(t3x3, t4x4, t5x5, move, movesO, movesX, ch3x3)
            player2 += 1
        if ch3x3['00'] == 'X' and ch3x3['11'] == 'X' and ch3x3['22'] == 'X':
            t3x3, t4x4, t5x5, move, movesO, movesX, ch3x3 = r3x3(t3x3, t4x4, t5x5, move, movesO, movesX, ch3x3)
            player1 += 1
        if ch3x3['00'] == 'O' and ch3x3['11'] == 'O' and ch3x3['22'] == 'O':
            t3x3, t4x4, t5x5, move, movesO, movesX, ch3x3 = r3x3(t3x3, t4x4, t5x5, move, movesO, movesX, ch3x3)
            player2 += 1
        if ch3x3['20'] == 'X' and ch3x3['11'] == 'X' and ch3x3['02'] == 'X':
            t3x3, t4x4, t5x5, move, movesO, movesX, ch3x3 = r3x3(t3x3, t4x4, t5x5, move, movesO, movesX, ch3x3)
            player1 += 1
        if ch3x3['20'] == 'O' and ch3x3['11'] == 'O' and ch3x3['02'] == 'O':
            t3x3, t4x4, t5x5, move, movesO, movesX, ch3x3 = r3x3(t3x3, t4x4, t5x5, move, movesO, movesX, ch3x3)
            player2 += 1
        if ch3x3['00'] == 'X' and ch3x3['11'] == 'X' and ch3x3['22'] == 'X':
            t3x3, t4x4, t5x5, move, movesO, movesX, ch3x3 = r3x3(t3x3, t4x4, t5x5, move, movesO, movesX, ch3x3)
            player1 += 1
        if ch3x3['00'] == 'O' and ch3x3['11'] == 'O' and ch3x3['22'] == 'O':
            t3x3, t4x4, t5x5, move, movesO, movesX, ch3x3 = r3x3(t3x3, t4x4, t5x5, move, movesO, movesX, ch3x3)
            player2 += 1
        if len(moves) == 9:
            t3x3, t4x4, t5x5, move, movesO, movesX, ch3x3 = r3x3(t3x3, t4x4, t5x5, move, movesO, movesX, ch3x3)
        # for key, value in ch3x3.items():
        #     if value == 'O':
        #         if key == '11' or key == '10' or key == '01' or key == '12' or key == '21':
        #             print('y')
        #     if value == 'X':
        #         if key == '11' or key == '10' or key == '01' or key == '12' or key == '21':
        #             print('y')
    # check end 4x4
    # check end 5x5
    text1 = str(round(pygame.time.get_ticks() / 1000, 1))
    label1 = myfond.render(text1, 1, (0,0,0))
    screen.blit(label1, (811, 220))
    text2 = str(player1) + ' : ' + str(player2)
    label2 = myfond.render(text2, 1, (0, 0, 0))
    screen.blit(label2, (790, 85))
    t3x3_pos = [735, 350]
    T3x3_ch = 0
    t4x4_pos = [860, 350]
    T4x4_ch = 0
    t5x5_pos = [735, 425]
    T5x5_ch = 0
    t20x20_pos = [860, 425]
    T20x20_ch = 0
    screen.blit(up, [760, 80])
    screen.blit(up, [910, 80])
    screen.blit(down, [760, 110])
    screen.blit(down, [910, 110])
    screen.blit(RESET,(750, 550))
    if mouse[0] > 750 and mouse[0] < 950 and mouse[1] > 550 and mouse[1] < 625:
        screen.blit(RESET2, (750, 550))
    moves = []
    pygame.display.update()
