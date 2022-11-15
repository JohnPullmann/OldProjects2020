import pygame
import random
import sys
import time

pygame.font.init
pygame.init()
#images load
background = pygame.image.load('background.png')
object1 = pygame.image.load('1.png')
object2 = pygame.image.load('2.png')
object3 = pygame.image.load('3.png')
object4 = pygame.image.load('4.png')
object5 = pygame.image.load('5.png')
object6 = pygame.image.load('6.png')
object7 = pygame.image.load('7.png')
block1 = pygame.image.load('block1.png')
block2 = pygame.image.load('block2.png')
block3 = pygame.image.load('block3.png')
block4 = pygame.image.load('block4.png')
block5 = pygame.image.load('block5.png')
block6 = pygame.image.load('block6.png')
block7 = pygame.image.load('block7.png')
###
#settings
width = 700
height = 700
speed = 35
game = True
###
#other variables
types = [object1, object2, object3, object4, object5, object6, object7]
screen = pygame.display.set_mode((width, height))
fps = pygame.time.Clock()
time = 0
score1 = 0
my_fond = pygame.font.SysFont('monospace', 40)
blocks = []
move = False
playing = True
next_type = random.choice(types)
types_positions1 = {'object1':[[0, 0], [40, 0], [80, 0], [120, 0]], 'object2':[[0, 40], [40, 0], [40, 40], [80, 0]],'object3':[[0, 0], [40, 0], [80, 40], [40, 40]],'object4':[[0, 40], [40, 0], [40, 40], [80, 40]],'object5':[[0, 0], [0, 40], [40, 40], [80, 40]], 'object6':[[0, 40], [40, 40], [80, 40], [80, 0]],'object7':[[0, 0], [0, 40], [40, 0], [40, 40]]}
types_positions2 = {'object1':[[0, 0], [0, -40], [0, -80], [0, -120]],'object2':[[40, 40], [40, 0], [0, 0], [0, -40]], 'object3':[[0, 40], [0, 0], [40, 0], [40, -40]],'object4':[[0, 0], [40, 0], [0, 40], [0, -40]],'object5':[[0, 0], [0, 40], [0, -40], [40, -40]], 'object6':[[0, 0], [0, 40], [0, -40], [40, 40]],'object7':[[0, 0], [0, 40], [40, 0], [40, 40]]}
types_positions3 = {'object1':[[0, 0], [40, 0], [80, 0], [120, 0]], 'object2':[[0, 40], [40, 0], [40, 40], [80, 0]],'object3':[[0, 0], [40, 0], [80, 40], [40, 40]],'object4':[[0, 0], [40, 0], [80, 0], [40, 40]],'object5':[[0, 0], [40, 0], [80, 0], [80, 40]], 'object6':[[0, 0], [0, 40], [40, 0], [80, 0]], 'object7':[[0, 0], [0, 40], [40, 0], [40, 40]]}
types_positions4 = {'object1':[[0, 0], [0, -40], [0, -80], [0, -120]],'object2':[[40, 40], [40, 0], [0, 0], [0, -40]], 'object3':[[0, 40], [0, 0], [40, 0], [40, -40]],'object4':[[0, 0], [40, 0], [40, -40], [40, 40]],'object5':[[0, 40], [40, 40], [40, 0], [40, -40]], 'object6':[[0, -40], [40, -40], [40, 0], [40, 40]], 'object7':[[0, 0], [0, 40], [40, 0], [40, 40]]}
image_to_string = {object1: 'object1',object2: 'object2',object3: 'object3',object4: 'object4',object5: 'object5',object6: 'object6',object7: 'object7'}
tick1 = 0
mouse = pygame.mouse.get_pos()

text1 = str(score1)
label1 = my_fond.render(text1, 1, (255, 255, 255))
text2 = str(round(pygame.time.get_ticks() / 1000, 1))
label2 = my_fond.render(text2, 1, (255, 255, 255))
###
def testing_quit_and_keys():
    global game
    global move
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        mouse_type = pygame.mouse.get_pressed()
        if event.type == pygame.KEYDOWN or mouse_type[2] == 1:
            if mouse_type[2] == 1 or event.key == pygame.K_r:
                for block in blocks:
                    if block.moving_activation == True:
                        #test
                        rotation = True
                        for block in blocks:
                            if block.moving_activation == True:
                                moving_block = block
                                block_position = block.main_position
                                quit = False
                                for next_block in block.next_rotation:
                                    if next_block[0] + block_position[0] >= 450 or  next_block[0] + block_position[0] <= 0 or next_block[1] + block_position[1] >= 600 or  next_block[1] + block_position[1] <= 10 :
                                        rotation = False
                                        quit = True
                                        break
                        moving_block = block
                        block_position = block.main_position
                        quit = False
                        for next_block in block.next_rotation:
                            for block in blocks:
                                if block.moving_activation != True:
                                    for other_miny_block in block.miny_blocks_position:
                                        if next_block[0] +  block_position[0] == other_miny_block[0] + block.main_position[0] and next_block[1] +  block_position[1] == other_miny_block[1] + block.main_position[1]:

                                            rotation = False
                                            quit = True
                                            break
                                    if quit == True:
                                        break
                           
                        ###
                        if block.rotation == 4 and rotation == True:
                            block.rotation = 1
                        elif rotation == True:
                            block.rotation += 1
        mouse_type = pygame.mouse.get_pressed()
        move = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                move = True
                moving()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 5:
                move = True
                moving()

def creating():
    global next_type
    global moving_type
    global blocks
    global score1
    global game
    number_of_miny_blocks = 0
    for block in blocks:
        if len(block.miny_blocks_position) > 1:
            number_of_miny_blocks += 1
    if number_of_miny_blocks > 50:
        game = False

    score1 += 1
    moving_type = next_type
    next_type = random.choice(types)
    name_block = image_to_string[moving_type]
    miny_blocks_position = types_positions1[name_block]
    new_block = block_stats(moving_type, [170, 50], miny_blocks_position, True, False, 1, types_positions2[name_block], name_block)
    blocks.append(new_block)
def printing():
    screen.blit(background, [0, 0])
    screen.blit(label1, (560, 280))
    screen.blit(label2, (560, 380))
    if next_type == object7:
        next_position = [535, 120]
    elif next_type ==  object1:
        next_position = [515, 150]
    else:
        next_position = [515, 120]
    if next_type == object1:
        screen.blit(pygame.transform.scale(object1, (120, 30)), next_position)
    else:
        screen.blit(next_type, next_position)

    # docasne
    for block in blocks:
        for miny_block in block.miny_blocks_position:
            pygame.draw.rect(screen, (0, 0, 0), (miny_block[0]+block.main_position[0], miny_block[1]+block.main_position[1], 40, 40))
            if block.image == object1:
                screen.blit(block1, [miny_block[0]+block.main_position[0],miny_block[1]+block.main_position[1]])
            if block.image == object2:
                screen.blit(block2, [miny_block[0]+block.main_position[0],miny_block[1]+block.main_position[1]])
            if block.image == object3:
                screen.blit(block3, [miny_block[0]+block.main_position[0],miny_block[1]+block.main_position[1]])
            if block.image == object4:
                screen.blit(block4, [miny_block[0]+block.main_position[0],miny_block[1]+block.main_position[1]])
            if block.image == object5:
                screen.blit(block5, [miny_block[0]+block.main_position[0],miny_block[1]+block.main_position[1]])
            if block.image == object6:
                screen.blit(block6, [miny_block[0]+block.main_position[0],miny_block[1]+block.main_position[1]])
            if block.image == object7:
                screen.blit(block7, [miny_block[0]+block.main_position[0],miny_block[1]+block.main_position[1]])

def colision():
    global game
    #colision bottom
    for block in blocks:
        if block.moving_activation == True:
            bottom = False
            for miny_block in block.miny_blocks_position:
                if miny_block[1]+block.main_position[1] == 610:
                    bottom = True
            if bottom == True:
                block.moving_activation = False
                block.stop_activation = True
                number_of_miny_blocks = 0
                for block in blocks:
                    if len(block.miny_blocks_position) > 1:
                        number_of_miny_blocks += 1
                if number_of_miny_blocks > 50:
                    game = False
                creating()
    ###colision blocks
    for block in blocks:
        if game == False:
            break
        if block.moving_activation == True:
            moving_block = block
            block_position = block.main_position
            quit = False
            for moving_miny_block in block.miny_blocks_position:
                for block in blocks:
                    if block.moving_activation != True:
                        for other_miny_block in block.miny_blocks_position:
                            if moving_miny_block[0]+block_position[0] == other_miny_block[0]+block.main_position[0] and moving_miny_block[1]+block_position[1]+40 == other_miny_block[1]+block.main_position[1]:
                                moving_block.moving_activation = False
                                moving_block.stop_activation = True
                                creating()
                                quit = True
                                break
                        if quit == True:
                            break
                if quit == True:
                    break


def moving():
    global tick1
    global move
    if tick1 == speed or move == True:
        move = False
        tick1 = 0
        for x in blocks:
            if x.moving_activation == True:
                x.main_position[1] += 40
                end()
    move_width = False
    ### testing moving aria
    for x in blocks:
        if x.moving_activation == True:
            if mouse[0] > 50 and mouse[0] < 450 and mouse[1] > 50 and mouse[1] < 650:
                move_width = True
                for miny_block in x.miny_blocks_position:
                    if miny_block[0]+((mouse[0] - 50) // 40) * 40 + 50 == 450 or miny_block[0]+((mouse[0] - 50) // 40) * 40 + 50 == 10:
                        move_width = False
    ### width blocking test
    for block in blocks:
        if block.moving_activation == True:
            moving_block = block
            block_position = block.main_position
            quit = False
            for moving_miny_block in block.miny_blocks_position:
                for block in blocks:
                    if block.moving_activation != True:
                        for other_miny_block in block.miny_blocks_position:
                            if moving_miny_block[0]+((mouse[0] - 50) // 40) * 40 + 50 == other_miny_block[0]+block.main_position[0] and moving_miny_block[1]+ block_position[1] == other_miny_block[1]+block.main_position[1]:
                                move_width = False
                                quit = True
                                break
                        if quit == True:
                            break
                if quit == True:
                    break
    ###
    if move_width == True:
        x.main_position[0] = ((mouse[0] - 50) // 40) * 40 + 50
    ###rotation
    types_positions1 = {'object1': [[0, 0], [40, 0], [80, 0], [120, 0]],
                        'object2': [[0, 40], [40, 0], [40, 40], [80, 0]],
                        'object3': [[0, 0], [40, 0], [80, 40], [40, 40]],
                        'object4': [[0, 40], [40, 0], [40, 40], [80, 40]],
                        'object5': [[0, 0], [0, 40], [40, 40], [80, 40]],
                        'object6': [[0, 40], [40, 40], [80, 40], [80, 0]],
                        'object7': [[0, 0], [0, 40], [40, 0], [40, 40]]}
    types_positions2 = {'object1': [[0, 0], [0, -40], [0, -80], [0, -120]],
                        'object2': [[40, 40], [40, 0], [0, 0], [0, -40]],
                        'object3': [[0, 40], [0, 0], [40, 0], [40, -40]],
                        'object4': [[0, 0], [40, 0], [0, 40], [0, -40]],
                        'object5': [[0, 0], [0, 40], [0, -40], [40, -40]],
                        'object6': [[0, 0], [0, 40], [0, -40], [40, 40]],
                        'object7': [[0, 0], [0, 40], [40, 0], [40, 40]]}
    types_positions3 = {'object1': [[0, 0], [40, 0], [80, 0], [120, 0]],
                        'object2': [[0, 40], [40, 0], [40, 40], [80, 0]],
                        'object3': [[0, 0], [40, 0], [80, 40], [40, 40]],
                        'object4': [[0, 0], [40, 0], [80, 0], [40, 40]],
                        'object5': [[0, 0], [40, 0], [80, 0], [80, 40]], 'object6': [[0, 0], [0, 40], [40, 0], [80, 0]],
                        'object7': [[0, 0], [0, 40], [40, 0], [40, 40]]}
    types_positions4 = {'object1': [[0, 0], [0, -40], [0, -80], [0, -120]],
                        'object2': [[40, 40], [40, 0], [0, 0], [0, -40]],
                        'object3': [[0, 40], [0, 0], [40, 0], [40, -40]],
                        'object4': [[0, 0], [40, 0], [40, -40], [40, 40]],
                        'object5': [[0, 40], [40, 40], [40, 0], [40, -40]],
                        'object6': [[0, -40], [40, -40], [40, 0], [40, 40]],
                        'object7': [[0, 0], [0, 40], [40, 0], [40, 40]]}
    for block in blocks:
        if block.moving_activation == True:
            if block.rotation == 1:
                block.miny_blocks_position = types_positions1[block.name]
                block.next_rotation = types_positions2[block.name]
            if block.rotation == 2:
                block.miny_blocks_position = types_positions2[block.name]
                block.next_rotation = types_positions3[block.name]
            if block.rotation == 3:
                block.miny_blocks_position = types_positions3[block.name]
                block.next_rotation = types_positions4[block.name]
            if block.rotation == 4:
                block.miny_blocks_position = types_positions4[block.name]
                block.next_rotation = types_positions1[block.name]
                
def stats():
    global label1
    global label2
    global tick1
    global mouse
    global time
    global score2
    text1 = str(score1)
    score2 = str(score1)
    label1 = my_fond.render(text1, 1, (255, 255, 255))
    tick1 += 1
    mouse = pygame.mouse.get_pos()
    text2 = str(int(round(pygame.time.get_ticks() / 1000, 0)))
    time =  str(int(round(pygame.time.get_ticks() / 1000, 0)))
    label2 = my_fond.render(text2, 1, (255, 255, 255))

def end():
    global game
    for block in blocks:
        if block.moving_activation != True:
            for miny_block in block.miny_blocks_position:
                if miny_block[1]+block.main_position[1] == 170:
                    game = False
def ending():
    global playing
    global text1
    global time
    global score2
    global game
    label1 = my_fond.render(score2, 1, (0, 0, 0))
    label2 = my_fond.render(time, 1, (0, 0, 0))
    end_menu = True
    background_end = pygame.image.load('background_end.png')
    back = pygame.image.load('back.png')
    back2 = pygame.image.load('back2.png')
    while end_menu == True:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end_menu = False
                playing = False
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse[0] > 500 and mouse[0] < 650 and mouse[1] > 300 and mouse[1] < 400:
                    end_menu = False
                    game = True
        screen.blit(background_end, (0,0))
        if mouse[0] > 500 and mouse[0] < 650 and mouse[1] > 300 and mouse[1] < 400:
            screen.blit(back2, (0, 0))
        else:
            screen.blit(back, (0, 0))
        screen.blit(label1, (325, 310))
        screen.blit(label2, (325, 370))
        pygame.display.update()

def score():
    global score1
    rows = [50,90,130,170,210,250,290,330,370,410,450,490,530,570,610]
    move = False
    quit = False
    for row in rows:
        block_in_row = 0
        for block in blocks:
            if block.moving_activation != True:
                for miny_block in block.miny_blocks_position:
                    if miny_block[1] + block.main_position[1] == row:
                        block_in_row += 1
                        if block_in_row == 10:
                            block_in_row = 0
                            for block in blocks:
                                if block.moving_activation != True:
                                    for miny_block in block.miny_blocks_position:
                                        if miny_block[1] + block.main_position[1] == row:
                                            block.miny_blocks_position.remove(miny_block)
                                            for block in blocks:
                                                if block.moving_activation != True:
                                                    for miny_block in block.miny_blocks_position:
                                                        if miny_block[1] + block.main_position[1] == row:
                                                            block.miny_blocks_position.remove(miny_block)
                                                            move = True
                                                            quit = True
                                                            row_move = row
                            if quit == True:
                                break
                if quit == True:
                    break
        if quit == True:
            break
    if move == True:
        score1 += 20
        for block in blocks:
            if block.moving_activation != True and block.main_position[1] < row_move or (block.moving_activation != True and block.main_position[1] <= row_move and block.name == block1):
                block.main_position[1] += 40
    # for block in blocks:
    #     if block.moving_activation != True:
    #         for miny_block in block.miny_blocks_position:
    #             for block2 in blocks:
    #                 if block.moving_activation != True and block2 != block:
    #                     for miny_block2 in block2.miny_blocks_position:
    #                         if miny_block[0]+ block.main_position[0] == miny_block2[0]+ block2.main_position[0] and miny_block[0]+ block.main_position[0]
def stats_start():
    global time
    global score1
    global blocks
    global move
    global next_type
    time = 0
    score1 = 0
    blocks = []
    move = False
    next_type = random.choice(types)
    creating()
class block_stats:
    def __init__(self, image, main_position, miny_blocks_position, moving_activation, stop_activation, rotation, next_rotation, name):
        self.image = image
        self.main_position = main_position
        self.miny_blocks_position = miny_blocks_position
        self.moving_activation = moving_activation
        self.stop_activation = stop_activation
        self.rotation = rotation
        self.next_rotation = next_rotation
        self.name = name
creating()
while playing == True:
    if game == True:
        stats_start()
    while game == True:
        testing_quit_and_keys()
        printing()
        colision()
        moving()
        stats()
        score()
        fps.tick(100)
        pygame.display.update()
    if game == False and playing == True:
        ending()
