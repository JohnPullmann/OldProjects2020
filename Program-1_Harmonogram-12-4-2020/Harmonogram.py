
import pygame
import sys
import datetime
import json

pygame.init()
my_fond = pygame.font.SysFont('monospace', 28, True)
width = 900
height = 700
screen = pygame.display.set_mode((width, height))
running = True
move_scroll = 0
fps = pygame.time.Clock()
line_position = [-421, 190]
generate_position_rectange = pygame.Rect(645, 65, 125, 30)
save_position_rectange = pygame.Rect(100, 420, 175, 35)
load_position_rectange = pygame.Rect(100, 490, 175, 35)
exit_position_rectange = pygame.Rect(145, 575, 75, 40)
arrow_left_position_rectange = pygame.Rect(20, 172, 35, 80)
arrow_right_position_rectange = pygame.Rect(850, 172, 35, 80)

programing_hours_rectangle = pygame.Rect(240, 62, 20, 30)
rest_hours_rectangle = pygame.Rect(342, 62, 20, 30)
school_hours_rectangle = pygame.Rect(462, 62, 20, 30)
start_hours_rectangle = pygame.Rect(571, 66, 65, 30)
### load images
background = pygame.image.load('images/background.png')
background_second = pygame.image.load('images/background_second.png')
background_third = pygame.image.load('images/background_third.png')
arrow_left_active = pygame.image.load('images/arrow_left_active.png')
arrow_right_active = pygame.image.load('images/arrow_right_active.png')
generate_active = pygame.image.load('images/generate_active.png')
save_active = pygame.image.load('images/save_active.png')
load_active = pygame.image.load('images/load_active.png')
exit_active = pygame.image.load('images/exit_active.png')
line_image = pygame.image.load('images/line.png')
now_image = pygame.image.load('images/now_image.png')
programing = pygame.image.load('images/programing.png')
rest = pygame.image.load('images/rest.png')
school = pygame.image.load('images/school.png')
other = pygame.image.load('images/other.png')
nothing = pygame.image.load('images/nothing.png')
history_nothing = pygame.image.load('images/history_nothing.png')
history_rest = pygame.image.load('images/history_rest.png')
history_school = pygame.image.load('images/history_school.png')
history_other = pygame.image.load('images/history_other.png')
history_programing = pygame.image.load('images/history_programing.png')
history_cover = pygame.image.load('images/history_cover.png')

###
generate_activation = False
save_activation = False
load_activation = False
exit_activation = False
arrow_left_activation = False
arrow_right_activation = False
#
harmonogram = [[0,nothing],[1,nothing],[2,nothing],[3,nothing],[4,nothing],[5,nothing],
               [6,nothing],[7,nothing],[8,nothing],[9,nothing],[10,nothing],[11,nothing],
               [12,nothing],[13,nothing],[14,nothing],[15,nothing],[16,nothing],[17,nothing],
               [18,nothing],[19,nothing],[20,nothing],[21,nothing],[22,nothing],[23,nothing]]
harmonogram_types = [nothing, programing, school, rest, other]
#
programing_hours = 0
rest_hours = 0
school_hours = 0
start_hours = 8
#
def generate():
    global harmonogram
    p_h = programing_hours
    r_h = rest_hours
    s_h = school_hours

    harmonogram = [[0, nothing], [1, nothing], [2, nothing], [3, nothing], [4, nothing], [5, nothing],
                   [6, nothing], [7, nothing], [8, nothing], [9, nothing], [10, nothing], [11, nothing],
                   [12, nothing], [13, nothing], [14, nothing], [15, nothing], [16, nothing], [17, nothing],
                   [18, nothing], [19, nothing], [20, nothing], [21, nothing], [22, nothing], [23, nothing], ]
    after_school_break = True
    programing_serie = 0
    for hour in harmonogram:
        if start_hours <= hour[0]:
            if hour[0] == 12:
                hour[1] = other
                continue
            if s_h > 0:
                s_h -= 1
                hour[1] = school
                continue
            if r_h > 0 and after_school_break == True:
                after_school_break = False
                r_h -= 1
                hour[1] = rest
                continue
            if p_h > 0 and programing_serie != 3:
                p_h -= 1
                programing_serie += 1
                hour[1] = programing
                continue
            if programing_serie == 3 and r_h > 0:
                r_h -= 1
                hour[1] = rest
                programing_serie = 0
                continue
            if r_h > 0:
                r_h -= 1
                hour[1] = rest
                continue
def save_pattern():
    harmonogram_json = harmonogram
    for list in harmonogram_json:
        for image in list:
            if image == nothing:
                list[1] = 'nothing'
            if image == other:
                list[1] = 'other'
            if image == school:
                list[1] = 'school'
            if image == rest:
                list[1] = 'rest'
            if image == programing:
                list[1] = 'programing'
    file = open('..\\Program-1_Harmonogram-12-4-2020\\patterns\\pattern.txt', 'w')
    json.dump(harmonogram_json, file)
    file.close()
    for list in harmonogram_json:
        for image in list:
            if image == 'nothing':
                list[1] = nothing
            if image == 'other':
                list[1] = other
            if image == 'school':
                list[1] = school
            if image == 'rest':
                list[1] = rest
            if image == 'programing':
                list[1] = programing
def save_history():
    global harmonogram
    harmonogram_json = harmonogram
    for list in harmonogram_json:
        for image in list:
            if image == nothing:
                list[1] = 'nothing'
            if image == other:
                list[1] = 'other'
            if image == school:
                list[1] = 'school'
            if image == rest:
                list[1] = 'rest'
            if image == programing:
                list[1] = 'programing'
    file = open('..\\Program-1_Harmonogram-12-4-2020\\history\\'+'%d-%d-%d' % (now_date.day, now_date.month, now_date.year,) +  '.txt', 'w')
    json.dump(harmonogram_json, file)
    file.close()
def load_history():
    global harmonogram, history_harmonograms
    try:
        now_date = datetime.datetime.now()
        file = open('..\\Program-1_Harmonogram-12-4-2020\\history\\'+'%d-%d-%d' % (now_date.day, now_date.month, now_date.year,) +  '.txt', 'r')
        harmonogram_json = json.load(file)
        for list in harmonogram_json:
            for image in list:
                if image == 'nothing':
                    list[1] = nothing
                if image == 'other':
                    list[1] = other
                if image == 'school':
                    list[1] = school
                if image == 'rest':
                    list[1] = rest
                if image == 'programing':
                    list[1] = programing
        harmonogram = harmonogram_json
        file.close()
    except:
        pass
    history_harmonograms = []
    for number2 in range(12):
        for number in range(30):
            if number != now_date.day:
                try:
                    now_date = datetime.datetime.now()
                    file = open(
                        '..\\Program-1_Harmonogram-12-4-2020\\history\\' + str(number) +'-'+ str(number2) +'-%d' % (now_date.year,) + '.txt', 'r')
                    harmonogram_json = json.load(file)
                    for list in harmonogram_json:
                        for image in list:
                            if image == 'nothing':
                                list[1] = history_nothing
                            if image == 'other':
                                list[1] = history_other
                            if image == 'school':
                                list[1] = history_school
                            if image == 'rest':
                                list[1] = history_rest
                            if image == 'programing':
                                list[1] = history_programing
                    file.close()
                    history_harmonograms.append(harmonogram_json)
                except:
                    pass
    history_harmonograms.reverse()
def load_pattern():
    global harmonogram
    try:
        now_date = datetime.datetime.now()
        file = open('..\\Program-1_Harmonogram-12-4-2020\\patterns\\pattern.txt', 'r')
        harmonogram_json = json.load(file)
        for list in harmonogram_json:
            for image in list:
                if image == 'nothing':
                    list[1] = nothing
                if image == 'other':
                    list[1] = other
                if image == 'school':
                    list[1] = school
                if image == 'rest':
                    list[1] = rest
                if image == 'programing':
                    list[1] = programing
        harmonogram = harmonogram_json
        file.close()
    except:
        pass
def exit():
    save_history()
    pygame.quit()
    sys.exit()
def arrow_left():
    if line_position[0] != 59:
        line_position[0] += 60
def arrow_right():

    if line_position[0] != -601:
        line_position[0] -= 60
def buttons_activaction():
    global generate_activation, save_activation, load_activation, exit_activation, arrow_left_activation, arrow_right_activation, mouse, click
    if generate_position_rectange.collidepoint(mouse):
        generate_activation = True
        if click == True:
            generate()
    else:
        generate_activation = False
    if save_position_rectange.collidepoint(mouse):
        save_activation = True
        if click == True:
            save_pattern()
    else:
        save_activation = False
    if load_position_rectange.collidepoint(mouse):
        load_activation = True
        if click == True:
            load_pattern()
    else:
        load_activation = False
    if exit_position_rectange.collidepoint(mouse):
        exit_activation = True
        if click == True:
            exit()
    else:
        exit_activation = False
    if arrow_left_position_rectange.collidepoint(mouse):
        arrow_left_activation = True
        if click == True:
            arrow_left()
    else:
        arrow_left_activation = False
    if arrow_right_position_rectange.collidepoint(mouse):
        arrow_right_activation = True
        if click == True:
            arrow_right()
    else:
        arrow_right_activation = False
def events():
    global running, move_scroll
    global generate_activation, save_activation, load_activation, exit_activation, arrow_left_activation, arrow_right_activation, mouse, click, now, label, now_date, label_programing, label_rest, label_school, label_start, programing_hours, rest_hours, school_hours, start_hours
    # time
    now_date = datetime.datetime.now()
    now = '%d:%d:%d %d-%d-%d ' % (now_date.hour, now_date.minute, now_date.second, now_date.day, now_date.month, now_date.year,) + datetime.datetime.today().strftime('%A')
    label = my_fond.render(now, 1, (0, 0, 0))
    label_programing = my_fond.render(str(programing_hours), 1, (0, 0, 0))
    label_rest = my_fond.render(str(rest_hours), 1, (0, 0, 0))
    label_school = my_fond.render(str(school_hours), 1, (0, 0, 0))
    label_start = my_fond.render(str(start_hours)+':00', 1, (0, 0, 0))
    #
    mouse = pygame.mouse.get_pos()
    click = False
    click_right = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_history()
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                click =True
            if event.button == 3:
                click_right =True
            if event.button == 4:
                if (390 + len(history_harmonograms)*35)+move_scroll > 570:
                    move_scroll -= 20
            elif event.button == 5:
                if move_scroll < 0:
                    move_scroll += 20
    for hour in harmonogram:
        hour_rectangle = pygame.Rect(line_position[0]+(harmonogram.index(hour)*60)-3, line_position[1]+5, 60, 15)
        if hour_rectangle.collidepoint(mouse):
            if click_right == True and mouse[0] > 60 and mouse[0] < 840:
                if harmonogram_types.index(hour[1])+1 == 5:
                    hour[1] = harmonogram_types[0]
                else:
                    hour[1] = harmonogram_types[harmonogram_types.index(hour[1])+1]
            if click == True and mouse[0] > 60 and mouse[0] < 840:
                if harmonogram_types.index(hour[1])-1 == -1:
                    hour[1] = harmonogram_types[4]
                else:
                    hour[1] = harmonogram_types[harmonogram_types.index(hour[1])-1]
    if click == True:
        if programing_hours_rectangle.collidepoint(mouse):
            if programing_hours != 8:
                programing_hours += 1
            else:
                programing_hours = 0
        if rest_hours_rectangle.collidepoint(mouse):
            if rest_hours != 8:
                rest_hours += 1
            else:
                rest_hours = 0
        if school_hours_rectangle.collidepoint(mouse):
            if school_hours != 8:
                school_hours += 1
            else:
                school_hours = 0
        if start_hours_rectangle.collidepoint(mouse):
            if start_hours != 12:
                start_hours += 1
            else:
                start_hours = 5
    if click_right == True:
        if programing_hours_rectangle.collidepoint(mouse):
            if programing_hours != 0:
                programing_hours -= 1
            else:
                programing_hours = 8
        if rest_hours_rectangle.collidepoint(mouse):
            if rest_hours != 0:
                rest_hours -= 1
            else:
                rest_hours = 8
        if school_hours_rectangle.collidepoint(mouse):
            if school_hours != 0:
                school_hours -= 1
            else:
                school_hours = 8
        if start_hours_rectangle.collidepoint(mouse):
            if start_hours != 5:
                start_hours -= 1
            else:
                start_hours = 12

    buttons_activaction()
def printing():
    global now_date
    screen.blit(background, (0,0))
    history()
    ### harmonogram
    for hour in harmonogram:
        screen.blit(hour[1], [line_position[0]+(harmonogram.index(hour)*60), line_position[1]+5])
    ###
    screen.blit(line_image, line_position)
    screen.blit(now_image, [line_position[0]+(now_date.hour*60+now_date.minute)-30, line_position[1]-39])
    screen.blit(background_second, (0, 0))
    screen.blit(label, (160, 277))
    screen.blit(label_programing, (240, 62))
    screen.blit(label_rest, (342, 62))
    screen.blit(label_school, (462, 62))
    screen.blit(label_start, (566, 66))

    if generate_activation == True:
        screen.blit(generate_active, (0, 0))
    if save_activation == True:
        screen.blit(save_active, (0, 0))
    if arrow_left_activation == True:
        screen.blit(arrow_left_active, (0, 0))
    if arrow_right_activation == True:
        screen.blit(arrow_right_active, (0, 0))
    if load_activation == True:
        screen.blit(load_active, (0, 0))
    if exit_activation == True:
        screen.blit(exit_active, (0, 0))
    #
def history():
    move = 0
    for history_harmonogram in history_harmonograms:
        move +=  35
        for list in history_harmonogram:
            screen.blit(list[1], (390+(list[0]*16)+8, 450 + move + move_scroll))
        screen.blit(history_cover, (390, 450 + move + move_scroll))
    screen.blit(background_third, (0, 0))
load_history()
while running:
    events()
    printing()
    fps.tick(100)
    pygame.display.update()